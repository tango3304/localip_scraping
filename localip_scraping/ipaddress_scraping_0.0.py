# Coding: UTF-8

import socket
import subprocess

class IPaddressScraping:
	def get_host_ipaddress_lists():
		_, _, ipaddress_lists = socket.gethostbyname_ex(socket.gethostname())
		private_ipaddress = '192.168.'
		scraping_ipaddress = []

		for host_ipaddress in ipaddress_lists:
			if private_ipaddress in host_ipaddress:
				IPaddressScraping.append_list(scraping_ipaddress, host_ipaddress)
		return scraping_ipaddress
	
	def append_list(list, ipaddress):
		list.append('.'.join(ipaddress.split('.')[0:3][i] for i in range(3)) + '.')
		return list

	def ipaddress_screping(ipaddress_lists):
		print(f'\nGet Local IPaddress {ipaddress_lists}\n')
		for scraping_ipaddress in ipaddress_lists:

			# IPaddress Scraping START
			scraping_execution_decide = input(f'   Do you want to execution IPscraping of {scraping_ipaddress} (y or other) : ')
			if scraping_execution_decide.casefold() == 'y':
				print('---------------------------------')
				print(f'Target IPaddress:{scraping_ipaddress}')
				print('---------------------------------')
				scraping_ipaddress_list = [scraping_ipaddress+str(i) for i in range(1,255)]
				ipaddress_true_list = [subprocess.run(['ping','-n','1','-w','1',ipaddress], stdout=subprocess.DEVNULL).returncode for ipaddress in scraping_ipaddress_list]
				ipaddress_result_list = '\n'.join(f'  PING Connection OK:  {ipaddress}' for ipaddress, ipaddress_true in zip(scraping_ipaddress_list, ipaddress_true_list) if ipaddress_true == 0)
				print(ipaddress_result_list)

IPaddressScraping.ipaddress_screping(IPaddressScraping.get_host_ipaddress_lists())