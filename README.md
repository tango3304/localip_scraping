# Outline
Private IPaddress Scraping Module (Windows Version / Linux Version)<br>
※Check Execution on Windows10 and Manjaro<br>

# Install
pip install git+https://github.com/tango3304/t_privateip_scraping_linux.git<br>

# Execution (Linux Version)
Run with Administrator Authority<br>
<p>◇ Import Modules<br>
from t_privateip_scraping.scraping_linux import IPaddressScraping</p>
<p>◇ Execution Function<br>
IPaddressScraping.private_ipaddress_screping(IPaddressScraping.get_private_ipaddress_lists())</p>

<p>◇Select Network Interface After Execution<br>
Ex:
<br>&emsp;### Network Interface ###<br>
&emsp;&emsp;aaaaaaaaa<br>
&emsp;&emsp;bbbbbbbbb<br>
<br>
&emsp;Please Select an Network Interface: bbbbbbbbb</p>

# Execution (Windows Version)
Run with Administrator Authority<br>
<p>◇ Import Modules<br>
from t_privateip_scraping.scraping_windows import IPaddressScraping</p>

<p>◇ Execution Function<br>
IPaddressScraping.ipaddress_screping(IPaddressScraping.get_host_ipaddress_lists())</p>

<p>◇Select Private IPaddress After Execution<br>
Ex:
<br>Get Private IPaddress ['aaa.bbb.ccc.', 'ddd.eee.fff.', 'ggg.hhh.iii.']<br>
&emsp;Do you want to execution IPscraping of aaa.bbb.ccc. (y or other) : n<br>
&emsp;Do you want to execution IPscraping of ddd.eee.fff. (y or other) : n<br>
&emsp;Do you want to execution IPscraping of ggg.hhh.iii. (y or other) : y<br>
---------------------------------<br>
Target IPaddress:ggg.hhh.iii.<br>
---------------------------------<br>
&emsp;PING Connection OK:  ggg.hhh.iii.x<br>
&emsp;PING Connection OK:  ggg.hhh.iii.xx<br>
&emsp;PING Connection OK:  ggg.hhh.iii.xxx<br>
  
---
# 概要
プライベートIPアドレス スクレイピングモジュール (Windows版 / Linux版)<br>
※Windows10 と Manjaroで実行確認<br>

# インストール
pip install git+https://github.com/tango3304/t_privateip_scraping_linux.git<br>

# 実行 (Linux版)
管理者権限で実行<br>
<p>◇ モジュールをインポート<br>
from t_privateip_scraping.scraping_linux import IPaddressScraping</p>
<p>◇ 実行関数<br>
IPaddressScraping.private_ipaddress_screping(IPaddressScraping.get_private_ipaddress_lists())</p>

<p>◇実行後にネットワークインターフェースを選択<br>
例:
<br>&emsp;### Network Interface ###<br>
&emsp;&emsp;aaaaaaaaa<br>
&emsp;&emsp;bbbbbbbbb<br>
<br>
&emsp;Please Select an Network Interface: bbbbbbbbb</p>

# 実行 (Windows版)
管理者権限で実行<br>
<p>◇ モジュールをインポート<br>
from t_privateip_scraping.scraping_windows import IPaddressScraping</p>

<p>◇ 実行関数<br>
IPaddressScraping.ipaddress_screping(IPaddressScraping.get_host_ipaddress_lists())</p>

<p>◇実行後にプライベートIPアドレスを選択<br>
例:
<br>Get Private IPaddress ['aaa.bbb.ccc.', 'ddd.eee.fff.', 'ggg.hhh.iii.']<br>
&emsp;Do you want to execution IPscraping of aaa.bbb.ccc. (y or other) : n<br>
&emsp;Do you want to execution IPscraping of ddd.eee.fff. (y or other) : n<br>
&emsp;Do you want to execution IPscraping of ggg.hhh.iii. (y or other) : y<br>
---------------------------------<br>
Target IPaddress:ggg.hhh.iii.<br>
---------------------------------<br>
&emsp;PING Connection OK:  ggg.hhh.iii.x<br>
&emsp;PING Connection OK:  ggg.hhh.iii.xx<br>
&emsp;PING Connection OK:  ggg.hhh.iii.xxx<br>
