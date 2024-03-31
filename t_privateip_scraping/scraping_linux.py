# Coding: UTF-8
from subprocess import Popen, PIPE
from re import compile, split
from sys import exit, exc_info
from traceback import format_exception_only
from tping.tping import PingSocket
from scapy.layers.inet import IP

class IPaddressScraping:
	try:
		def get_private_ipaddress_lists():
			scraping_ipaddress = []
			
			# Abbreviated Word (省略単語)
			# Network Interface         == net_if
			# Network Interface Command == net_if_cmd
			# IPaddress Command         == ip_cmd
			
            		# Get Network Interface
			# ネットワークインターフェース取得
			net_if_cmd        = "ls /sys/class/net"
			net_if_cmd_result = Popen(net_if_cmd, shell=True, stdout = PIPE, encoding="UTF-8").stdout.readlines()
			net_if_list_tmp   = [result_value.rstrip("\n") for result_value in net_if_cmd_result]
			net_if_list_len   = len(net_if_list_tmp)
			print(f'\n  ### Network Interface ###')
			[print(f'    {net_if_list_tmp[len_value]}') for len_value in range(net_if_list_len)]
			
			# Variables Definition
			# IP Command Output Results
			# Delete Unnecessary Output Results
			# Store in List
			# 変数定義
			# ipコマンドの出力結果
			# 不要な出力結果を削除
			# リストに格納
			net_if             = input("\n Please Select an Network Interface: ")
			ip_cmd             = "ip a | grep -w " + net_if + " | grep 'inet'"
			ip_cmd_result      = Popen(ip_cmd, shell=True, stdout = PIPE)
			ip_cmd_result_list = split('[ inet /]', str(ip_cmd_result.communicate()))
			
			# Private IPaddress Search
			# Store in List Private IPaddress Only
			# Class A: 10.0.0.0    - 10.255.255.255
			# Class B: 172.16.0.0  - 172.31.255.255
			# Class C: 192.168.0.0 - 192.168.255.255
			# プライベートIPアドレス検索
			# プライベートIPアドレスのみリストに格納
			# クラスA: 10.0.0.0    - 10.255.255.255
			# クラスB: 172.16.0.0  - 172.31.255.255
			# クラスC: 192.168.0.0 - 192.168.255.255
			search_ipaddress = compile(r'(^10.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){2}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
									   r'(^172.((1[6-9]|2[0-9]|3[0-1])\.)(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
									   r'(^192.168.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)')
			match_ipaddr_list = [data_list for data_list in ip_cmd_result_list if search_ipaddress.fullmatch(data_list) != None]

			# Get IPaddress up to 3rd Octet
			# Delete Duplicate Value is Only One
			# IPアドレスを第３オクテットまで取得
			# 重複した値は１つになるように削除
			for match_ip in match_ipaddr_list:
				IPaddressScraping.append_list(scraping_ipaddress, match_ip)
			return set(scraping_ipaddress)

		
		# Split String with Decimal Point Separator and Create List
		# Get 3 Divided Values
		# Convert to String and add Decimal Point
		# 小数点区切りで文字列を分割しリスト化
		# 分割した値を３つまで取得
		# 文字列に変換し小数点を追加
		def append_list(list, ipaddress):
			list.append('.'.join(ipaddress.split('.')[0:3][i] for i in range(3)) + '.')
			return list


		# Private IPaddress Screping
		# プライベートIPアドレス スクレイピング
		def private_ipaddress_screping(ipaddress_lists):
			timeout = 1

			# Scraping 1-255 Private IPaddress with ICMP Packet
			# Check Source IPaddress from Contents Responded ICMP Packet
			# Display Source IPaddress on CLI
			# 1-255のプライベートIPアドレスをICMPパケットでスクレイピング
			# 応答したICMPパケットの中身から送信元IPアドレスを確認
			# 送信元IPアドレスをCLI上で表示
			print(f'\nGet Private IPaddress {ipaddress_lists}')
			for scraping_ipaddress in ipaddress_lists:
					print('---------------------------------')
					print(f'Target IPaddress:{scraping_ipaddress}')
					print('---------------------------------')
					scraping_ipaddress_list = [scraping_ipaddress+str(i) for i in range(1,255)]
					receive_result          = [PingSocket(ipaddr, timeout).ping_socket() for ipaddr in scraping_ipaddress_list]
					icmp_true_iplist        = [IP(list_value[0]).src for list_value in receive_result if list_value != ('Timeout', None)]
					print(f'  {icmp_true_iplist}\n')	
	except KeyboardInterrupt:
		print(f'\nProcess Interrupted\n')
		exit(1)
	except:
		exc_type, exc_message, _ = exc_info()
		exc_list                 = format_exception_only(exc_type, exc_message)
		err_message              = ''.join(exc_message for exc_message in exc_list)
		print(f'{err_message}')
		exit(1)
