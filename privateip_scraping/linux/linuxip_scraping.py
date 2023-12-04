# Coding: UTF-8
from subprocess import Popen, PIPE
from re import compile, split
from sys import exit, exc_info
from traceback import format_exception_only
from tping.tping import PingSocket
from scapy.layers.inet import IP

class IPaddressScraping:
	try:
		def get_host_ipaddress_lists():
			# Variables Definition [変数定義]
			interface = input("\n Source Interface [送信元インターフェース]: ")
			scraping_ipaddress = []

			# ip command Output Results [ipコマンドの出力結果]
			# Delete Unnecessary Output Results [不要な出力結果を削除]
			# Store in list [リストに格納]
			ip_command = "ip a | grep -w " + interface + " | grep 'inet'"
			process = Popen(ip_command, shell=True, stdout = PIPE)
			output_data = split('[ inet /]', str(process.communicate()))

			# Private IPaddress Search [プライベートIPアドレス検索]
			# Store in List Private IPaddress Only [プライベートIPアドレスのみリストに格納]
			search_ipaddress = compile(r'(^10.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){2}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
									r'(^172.((1[6-9]|2[0-9]|3[0-1])\.)(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
									r'(^192.168.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)')
			match_ipaddr_list = [data_list for data_list in output_data if search_ipaddress.fullmatch(data_list) != None]

			# Get IPaddress up to 3rd Octet[IPアドレスを第３オクテットまで取得]
			# Delete Duplicate Value is Only One [重複した値は１つになるように削除]
			for match_ip in match_ipaddr_list:
				IPaddressScraping.append_list(scraping_ipaddress, match_ip)
			return set(scraping_ipaddress)

		
		# Split String with Decimal Point Separator and Create List [小数点区切りで文字列を分割しリスト化]
		# Get 3 Divided Values [分割した値を３つまで取得]
		# Convert to String and add Decimal Point [文字列に変換し小数点を追加]
		def append_list(list, ipaddress):
			list.append('.'.join(ipaddress.split('.')[0:3][i] for i in range(3)) + '.')
			return list


		# Private IPaddress Screping [プライベートIPアドレス スクレイピング]
		def ipaddress_screping(ipaddress_lists):
			# Variables Definition [変数定義]
			timeout = 1

			# Scraping 1-255 Private IPaddress with ICMP Packet [1-255のプライベートIPアドレスをICMPパケットでスクレイピング]
			# Check Source IPaddress from Contents Responded ICMP Packet [応答したICMPパケットの中身から送信元IPアドレスを確認]
			# Display Source IPaddress on CLI [送信元IPアドレスをCLI上で表示]
			print(f'\nGet Private IPaddress {ipaddress_lists}')
			for scraping_ipaddress in ipaddress_lists:
				scraping_execution_decide = input(f'\n   Do you want to execution IPscraping of {scraping_ipaddress} (y or other) : ')
				if scraping_execution_decide.casefold() == 'y':
					print('---------------------------------')
					print(f'Target IPaddress:{scraping_ipaddress}')
					print('---------------------------------')
					scraping_ipaddress_list = [scraping_ipaddress+str(i) for i in range(1,255)]
					receive_result = [PingSocket(ipaddr, timeout).ping_socket() for ipaddr in scraping_ipaddress_list]
					icmp_true_iplist = [IP(list_value[0]).src for list_value in receive_result if list_value != ('Timeout', None)]
					print(f'  {icmp_true_iplist}\n')
	except KeyboardInterrupt:
		print(f'\nProcess Interrupted [処理を中断しました]\n')
		exit(1)
	except:
		exc_type, exc_message, _ = exc_info()
		exc_list = format_exception_only(exc_type, exc_message)
		err_message = ''.join(exc_message for exc_message in exc_list)
		print(f'{err_message}')
		exit(1)
