import wget
version = "1.2"
url_auto_upgrade = "https://raw.githubusercontent.com/Kaver0/easypip.github.io/main/code1-2.py"

with open("auto_install_pip.txt", "w") as file:
	file.write(url_auto_upgrade)

input_start = "==>>> "
upgradePIPstring = "upgrade"

def removed():
	print("--- PIP успешно обновился! ---\nЧтоб применить изменения перезапустите программу!")

def main(user_input):
	if user_input == "version":
		print("-> PIP " + version)
		return True
	elif user_input == "help":
		print("==================== Помощь ====================\n-> Для скачивания введите 'install', а потом введите название инсталятора.\n-> Для обновления программы введите 'upgrade'.\n-> Для проверки установленной версии введите 'version'.\n================================================")
		return True
	elif user_input == "install":
		install_input = input("INSTALL >>> ")
		try:
			wget.download("https://raw.githubusercontent.com/Kaver0/easypip.github.io/main/modules/" + install_input + ".py", out="installer.py")
			print("\n-> Вы скачали инсталятор {0}!\n-> Чтоб скачать необходимые модули перенесите файл 'installer.py' в необходимую папку, а затем откройте этот файл.\n-> После загрузки модулей, файл-инсталятор можно удалить.".format(install_input))
			return True
		except Exception as _ex:
			print("==================== Ошибка ====================\n-> Неизвестный модуль!\n-> Пожалуйста проверьте название модуля!\n================================================")
			return True
