# vgmdb_bkcrawler
根据专辑网址ID抓取其Booklet

#### requirements: Python 3.3 must be installed

## 准备工作：
  1. 将.py程序和config.ini一同放在不需要管理员权限的目录下
  2. 使用你的账号密码登陆 Vgmdb.net
  3. 在浏览器中查看网站保存的 cookies，找到 vgmuserid和 vgmpassword为标题的cookies，复制它们的值
  4. 打开config.ini，在[oathcks]选项下，替换对应的uid和pwd的值
  5. 在[albumno]选项下，更改id对应的值为准备抓取的专辑页面的网址的最后一串数字
  6. （可选）在[Paths]选项下，将下载目录复制到 down_dir后
  
##使用
完成准备工作后，直接运行vgmdb_bkcrawler.py即可
