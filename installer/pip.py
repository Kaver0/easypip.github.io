import os
import wget
import time

try:
	with open("auto_install_pip.txt", "r") as file:
		url = file.read()
except Exception as _ex:
	print("    **** WARNING ****  \n  ** Auto installer not found **  ")
	url = "** Auto installer not found! **"

try:
	import codePIP
except:
	no_inst = input("** PIP not installed! **\n  Please enter url PIP installer or enter 'auto' for automatic mode: ")
	if no_inst == "auto":
		try:
			print("The PIP is installed from the link: " + url)
			wget.download(url, out='codePIP.py')
			print("\n")
		except Exception as _ex:
			while True == True:
				input("Auto mode does not work! Please restart the program and enter the link! ")
	elif no_inst == "pip":
		wget.download("https://raw.githubusercontent.com/Kaver0/easypip.github.io/main/code1-0.py", out='codePIP.py')
		print("\nPIP 1.0 downloaded!")
	elif no_inst == 'version':
		download_version = input("Download via version: ")
		try:
			wget.download("https://raw.githubusercontent.com/Kaver0/easypip.github.io/main/code" + download_version +".py", out='codePIP.py')
			print("\nPIP " + download_version + " downloaded!")
		except Exception as _ex:
			while True == True:
				input("Please check your version! You may have set '.' instead of '-'! Restart program to repeat. ")
	else:
		try:
			print("The PIP is installed from the link: " + no_inst)
			wget.download(no_inst, out='codePIP.py')
			print("\n")
		except Exception as _ex:
			while True == True:
				input("Please check your link! Restart program to repeat. ")
		

	import codePIP

stop = False
while stop == False:

	user_input = input(codePIP.input_start)

	if user_input == codePIP.upgradePIPstring:
		os.remove('codePIP.py')
		codePIP.removed()
	elif codePIP.main(user_input) == False:
		print("** ERROR in PIP **\nThis program will close in 10 seconds!")
		time.sleep(10)
		stop = True
		break