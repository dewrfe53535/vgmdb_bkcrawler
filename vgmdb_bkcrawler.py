# -*- coding:utf-8 -*- 
import os
import configparser
import requests
import bs4

class vgmdb_bkcrawler:
    '''根据专辑网址ID抓取其Booklet'''


    def __init__(self):
        '''初始化进程'''
        self.cp = configparser.ConfigParser(allow_no_value = True)
        self.__vs = requests.session()  #vgmdb_session

    def _set_up(self):
        '''读取设置，如果没找到抛出异常'''
        if self.cp.read('config.ini'):
            self.__vs.headers.update({'User-Agent': 'Mozilla/5.0 (compatible)'})
            self.__vs.cookies.update({'vgmuserid': self.cp.get('oathcks', 'uid'),
                                      'vgmpassword': self.cp.get('oathcks', 'pwd')
                                     })
            self.__aid = self.cp.get('albumno', 'id')
        else:
            raise FileNotFoundError('没找到设置文件\n请将config.ini和程序一起放在同一目录下')

    def _get_bkurls(self):
        '''加载专辑页面，得到Booklet图片名称对应其网址的字典'''
        response = self.__vs.get(self.cp.get('album', 'url') + self.__aid)
        return {i.string: self.cp.get('fullimg', 'url') + i['href'].split("=")[2] for i in self._quarry_tags(response.text)}

    def _quarry_tags(self, html_doc):
        '''使用bs4处理html内容'''
        soup = bs4.BeautifulSoup(html_doc, 'html.parser')
        return soup.select('a[href^="/db/covers.php"]')

    def _ensure_dir(self, dpath):
        '''确认下载目录'''
        try:
            os.makedirs(dpath, exist_ok = True)
        except Exception:
            print('错误的文件夹名\n将下载到当前目录下')
            os.mkdir('./' + self.__aid)
            return os.path.abspath('./' + self.__aid)
        return dpath

    def _save_img(self, content, dstpath):
        '''保存图片'''
        with open(dstpath, 'wb') as f:
            f.write(content)

    def down_images(self):
        '''下载图片'''
        self._set_up()
        img_pth = self._ensure_dir(os.path.join(self.cp.get('Paths', 'down_dir'), self.__aid))
        for name, url in self._get_bkurls().items():
            img_res = self.__vs.get(url)
            img_ext = '.' + img_res.headers['Content-Type'][6:]
            self._save_img(img_res.content, os.path.join(img_pth, name + img_ext))

if __name__ == '__main__':
    try:
        vb = vgmdb_bkcrawler()
        vb.down_images()
    except Exception as EXCEPT:
        print(EXCEPT)