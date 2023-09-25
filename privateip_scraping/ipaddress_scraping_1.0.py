# Coding: UTF-8

import socket
import subprocess
import re

class IPaddressScraping:
	def get_host_ipaddress_lists():
		_, _, ipaddress_lists = socket.gethostbyname_ex(socket.gethostname())
		private_ipaddress = re.compile(	r'(^10.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){2}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
				 		r'(^172.((1[6-9]|2[0-9]|3[0-1])\.)(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)|'\
						r'(^192.168.(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$)')
		scraping_ipaddress = []

		for host_ipaddress in ipaddress_lists:
			if private_ipaddress.fullmatch(host_ipaddress) != None:
				IPaddressScraping.append_list(scraping_ipaddress, host_ipaddress)
		return scraping_ipaddress
	
	def append_list(list, ipaddress):
		list.append('.'.join(ipaddress.split('.')[0:3][i] for i in range(3)) + '.')
		return list

	def ipaddress_screping(ipaddress_lists):
		print(f'\nGet Local IPaddress {ipaddress_lists}')
		for scraping_ipaddress in ipaddress_lists:

			# IPaddress Scraping START
			scraping_execution_decide = input(f'\n   Do you want to execution IPscraping of {scraping_ipaddress} (y or other) : ')
			if scraping_execution_decide.casefold() == 'y':
				print('---------------------------------')
				print(f'Target IPaddress:{scraping_ipaddress}')
				print('---------------------------------')
				scraping_ipaddress_list = [scraping_ipaddress+str(i) for i in range(1,255)]
				ipaddress_true_list = [subprocess.run(['ping','-n','1','-w','1',ipaddress], stdout=subprocess.DEVNULL).returncode for ipaddress in scraping_ipaddress_list]
				ipaddress_result_list = '\n'.join(f'  PING Connection OK:  {ipaddress}' for ipaddress, ipaddress_true in zip(scraping_ipaddress_list, ipaddress_true_list) if ipaddress_true == 0)
				print(ipaddress_result_list)

IPaddressScraping.ipaddress_screping(IPaddressScraping.get_host_ipaddress_lists())
