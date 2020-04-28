from os import system as sys
from termcolor import colored
print(sys("figlet TEAM PYCODERS"))
print()
msg=colored("Developer : Team Pycoders    https://linkedin.com/in/whytedork","red")
print(sys("cowsay {}".format(msg)))
print()

print("""Enter 1  : to login as root user
Enter 2  : to see date & time 
Enter 3  : to open calculator
Enter 4  : to create new user
Enter 5  : to install new software or tool
Enter 6  : to open new terminal 
Enter 7  : to open text-editor
Enter 8  : to update whole system
Enter 9  : to launch python
Enter 10 : to scan website using nmap
Enter 11 : to check ip address
Enter 12 : to ping
Enter 13 : to configure web server
Enter 14 : to create banners
Enter 15 : to run any command
Enter 16 : to launch browser
Enter 17 : to search file or tool
Enter 18 : to exit
	""")

choice =int(input("Enter Your Choice : "))


if(choice==1):
	sys("sudo bash")
elif choice==2:
	sys("date")
elif choice==3:
	sys("bc")
elif choice==4:
	print("Enter user name : ",end="")
	create_user=input()
	sys("useradd {}".format(create_user))
elif choice==5:
	print("Enter software name : ",end="")
	software_name=input()
	sys("sudo apt-get install {}".format(software_name))
elif choice ==6:
	sys("gnome-terminal")
elif choice ==7:
	sys("gnome-text-editor")
elif choice==8:
	sys("sudo apt-get update")
elif choice==9:
	sys("python")
elif choice==10:
	print("Enter Website or IP : ",end="")
	website=input()
	sys("nmap {}".format(website))
elif choice==11:
	sys("ifconfig")
elif choice==12:
	print("Enter Website or IP : ",end="")
	website=input()
	sys("ping {}".format(website))
elif choice==13:
	sys("yum install httpd")
elif choice==14:
	print("enter banner name : ",end="")
	banner_name=input()
	sys("figlet {}".format(banner_name))
elif choice==15:
	print("enter command : ",end="")
	new_cmd=input()
	sys("{}".format(new_cmd))
elif choice==16:
	sys("firefox")
elif choice==17:
	printf("Enter name : ",end="")
	s_file=input()
	sys("loacte {}".format(s_file))
elif choice==18:
	sys("exit")
else :
	print("Invalid Choice!")