# vgmdb_bkcrawler
根据专辑网址ID抓取其Booklet

##### requirements: 使用 python3 以上的版本，安装好 requests 和 bs4 模块

## 准备工作：
  1. 将 .py 程序和 config.ini 一同放在不需要管理员权限的目录下
  2. 使用你的账号密码登陆 Vgmdb.net
  3. 在浏览器中查看网站保存的 cookies，找到 vgmuserid 和 vgmpassword 为标题的 cookies，复制它们的值
  4. 打开 config.ini，在 [oathcks] 选项下，替换对应的 uid 和 pwd 的值
  5. 在 [albumno] 选项下，更改 id 对应的值为准备抓取的专辑页面的网址的最后一串数字
  6. （可选）在 [Paths] 选项下，将下载目录复制到 down_dir 后
  
## 使用
完成准备工作后，直接运行 vgmdb_bkcrawler.py 即可
