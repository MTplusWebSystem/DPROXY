import socket
import ipcalc,re
import threading
import keyboard
from os import system 
bg=''

logo = """

██████╗░██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝
██║░░██║██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░
██║░░██║██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░
██████╔╝██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""
G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'

print(G+'''
\tSCAN WEBSOCKET
\tEditado Por: MTPLUSWEBSYSTEM 
\tEsse é bem rápido, o resultado final ficará na mesma pasta que você salvou esse arquivo com o nome (PROXYon.txt), e os ips quederem resposta na PRE_LIMPA.txt'''+GR)

ipranges={"LISTA UM": ["104.16.0.0/16", "104.17.0.0/16", "104.18.0.0/16"], 
 "LISTA DOIS": ['120.52.22.96/27', '205.251.249.0/24', '180.163.57.128/26', '204.246.168.0/22', '18.160.0.0/15', '205.251.252.0/23', '54.192.0.0/16', '204.246.173.0/24', '54.230.200.0/21', '120.253.240.192/26', '116.129.226.128/26', '130.176.0.0/17', '108.156.0.0/14', '99.86.0.0/16', '205.251.200.0/21', '223.71.71.128/25', '13.32.0.0/15', '120.253.245.128/26', '13.224.0.0/14', '70.132.0.0/18', '15.158.0.0/16', '13.249.0.0/16', '18.238.0.0/15', '18.244.0.0/15', '205.251.208.0/20', '65.9.128.0/18', '130.176.128.0/18', '58.254.138.0/25', '54.230.208.0/20', '116.129.226.0/25', '52.222.128.0/17', '18.164.0.0/15', '64.252.128.0/18', '205.251.254.0/24', '54.230.224.0/19', '71.152.0.0/17', '216.137.32.0/19', '204.246.172.0/24', '18.172.0.0/15', '120.52.39.128/27', '118.193.97.64/26', '223.71.71.96/27', '18.154.0.0/15', '54.240.128.0/18', '205.251.250.0/23', '180.163.57.0/25', '52.46.0.0/18', '223.71.11.0/27', '52.82.128.0/19', '54.230.0.0/17', '54.230.128.0/18', '54.239.128.0/18', '130.176.224.0/20', '36.103.232.128/26', '52.84.0.0/15', '143.204.0.0/16', '144.220.0.0/16', '120.52.153.192/26', '119.147.182.0/25', '120.232.236.0/25', '54.182.0.0/16', '58.254.138.128/26', '120.253.245.192/27', '54.239.192.0/19', '18.64.0.0/14', '120.52.12.64/26', '99.84.0.0/16', '130.176.192.0/19', '52.124.128.0/17', '204.246.164.0/22', '13.35.0.0/16', '204.246.174.0/23', '36.103.232.0/25', '119.147.182.128/26', '118.193.97.128/25', '120.232.236.128/26', '204.246.176.0/20', '65.8.0.0/16', '65.9.0.0/17', '108.138.0.0/15', '120.253.241.160/27', '64.252.64.0/18', '13.113.196.64/26', '13.113.203.0/24', '52.199.127.192/26', '13.124.199.0/24', '3.35.130.128/25', '52.78.247.128/26', '13.233.177.192/26', '15.207.13.128/25', '15.207.213.128/25', '52.66.194.128/26', '13.228.69.0/24', '52.220.191.0/26', '13.210.67.128/26', '13.54.63.128/26', '99.79.169.0/24', '18.192.142.0/23', '35.158.136.0/24', '52.57.254.0/24', '13.48.32.0/24', '18.200.212.0/23', '52.212.248.0/26', '3.10.17.128/25', '3.11.53.0/24', '52.56.127.0/25', '15.188.184.0/24', '52.47.139.0/24', '18.229.220.192/26', '54.233.255.128/26', '3.231.2.0/25', '3.234.232.224/27', '3.236.169.192/26', '3.236.48.0/23', '34.195.252.0/24', '34.226.14.0/24', '13.59.250.0/26', '18.216.170.128/25', '3.128.93.0/24', '3.134.215.0/24', '52.15.127.128/26', '3.101.158.0/23', '52.52.191.128/26', '34.216.51.0/25', '34.223.12.224/27', '34.223.80.192/26', '35.162.63.192/26', '35.167.191.128/26', '44.227.178.0/24', '44.234.108.128/25', '44.234.90.252/30'],'LISTA TRÊS':['157.240.0.0/20','104.16.0.0/22','103.21.244.0/22','103.22.200.0/22','103.31.4.0/22','104.16.0.0/22','104.24.0.0/22','108.162.0.0/22','131.0.72.0/22','141.101.0.0/22','162.158.0.0/20','172.64.0.0/22','173.245.0.0/20','188.114.96.0/20','190.93.240.0/20','197.234.240.0/22','198.41.128.0/20'], 'Flont_vivo1':['179.191.0.0/16','157.240.0.0/16'],'Flont_vivo2':['162.159.0.0/16','104.24.0.0/16','172.64.0.0/16','104.16.0.0/16','104.17.0.0/16','104.18.0.0/16','104.19.0.0/16'],'Flont_vivo3':['142.251.0.0/16']}
 
lista=ipranges["LISTA TRÊS"]
lista2=ipranges["Flont_vivo1"]
lista3=ipranges["Flont_vivo2"]
lista4=ipranges["Flont_vivo3"]
frstarray=ipranges["LISTA UM"]
secondarray=ipranges["LISTA DOIS"]
	

def scanner(host):
	sock=socket.socket()
	sock.settimeout(5)
	try:
		sock.connect((str(host),80))
		payload=f'GET wss://{host} HTTP/1.1\r\nHost: {host}\r\n\r\n'
		sock.send(payload.encode())
		response=sock.recv(1024).decode('utf-8','ignore')
		for data in response.split('\r\n'):
			data=data.split(':')
			if re.match(r'HTTP/\d(\.\d)?' ,data[0]):
				print('response status : {}{}{}'.format(O,data[0],GR))
				with open('PRE_LIMPA.txt','a') as fll:
				   fll.write(str(data[0])+f" ->> {host}"+'\n')
				   fll.close()
			if data[0]=='Server':
				try:
					if data[1] ==' cloudflare':
						print('{}server : {}\nFound working {}..'.format(G,host,GR))
						with open('PROXYon.txt','a') as fl:
							fl.write(str(host)+'\n'+'=> cloudflare')
							fl.close()
				except Exception as e:
					print(e)
			elif data[0]=='Server':
				try:
					if data[1] ==' CloudFront':
						print('{}server : {}\nFound working {}..'.format(G,host,GR))
						with open('PROXYon.txt','a') as fl:
							fl.write(str(host)+'\n'+'=> CloudFront')
							fl.close()
				except Exception as e:
					print(e)
	except Exception as e:print(e)

def Main():
	for k,v in ipranges.items():
		print('{',k,' : ',v,'}',end='\n')
	dicts=[frstarray,secondarray,lista,lista2 ,lista3,lista4]
	choose = int(input('\033[1;31;3m\n'*30+logo+'\033[1;32;3m \n\n MTPLUSWEBSYSTEM agradece! Selecione os ipranges cloudflare \n 1 ->> Lista 1\n 2 ->> lista 2 \n 3 ->> lista 3\n 4 ->> lista 4 Flont\n 5 ->> lista 5 Flont\n 6 ->> lista 6 Flont: '.title()))-1
	cidrs_list = dicts[choose]
	for cidr in cidrs_list:
			iprange=[]
			for ip in ipcalc.Network(cidr):
				iprange.append(ip)
			for index in range(len(iprange)):			
					try:
						print("{}[INFO] Sacaneando... ({}/{}) [{}]{}".format(
						R,index+1,len(iprange),iprange[index],GR))
						sc=threading.Thread(target=scanner,args=(iprange[index],))
						sc.start()
					except KeyboardInterrupt:
						print('{}Scan aborted by user!{}'.format(R,GR))
						break
Main()				
