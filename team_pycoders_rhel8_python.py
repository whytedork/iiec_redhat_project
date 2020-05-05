#Option 9 function
def what_py(x):
	if x == 1:
		sys('python3')
	elif x == 2 :
		fn=input("Enter file name to start writing code :")
		sys("gedit {0}".format(fn))
	elif x == 3 :
		pth = input("Enter name of the file you want to run :")
		sys("python3 {0}".format(pth))
	elif x == 4 :
		nm = input ("Enter package name :")
		sys("pip3 install {0}".format(nm))
	else :
		print("Invalid input !!!")
	return


#code for banner and designs
from os import system as sys
import getpass
from termcolor import colored
print(sys("figlet TEAM PYCODERS"))
print()
msg=colored("Developer : Team Pycoders ","red")
print(sys("cowsay {}".format(msg)))
print()

#read password from file
f=open("password.txt",'r')
password=f.readline()

#password setup
x=getpass.getpass("Enter Your Password : ")
if x==password:
	print(colored("LogIn Successfull !","red"))
	print()
else :
	print(colored("Password is Incorrect !","red"))

print("Where you like to perform the task: local or remote ? ", end="")
location = input()
print(location)

if location == 'remote':
    ip = input("Enter your IP : ")

if location == 'local':
	#menu-bar

	if x==password:
		while True:
			print("""Enter 1  : to login as root user
	Enter 2  : to see date & time 
	Enter 3  : to open calculator
	Enter 4  : to create new user
	Enter 5  : to install new software or tool
	Enter 6  : to open new terminal 
	Enter 7  : to open text-editor
	Enter 8  : to update whole system
	Enter 9  : to Python operations
	Enter 10 : to scan website using nmap
	Enter 11 : to check ip address
	Enter 12 : to ping
	Enter 13 : to configure web server
	Enter 14 : to create banners
	Enter 15 : to run any command
	Enter 16 : to launch browser
	Enter 17 : to search file or tool
        Enter 18 : to pull a docker image
	Enter 19 : to launch the docker container centos
	Enter 20 : to check the docker images
	Enter 21 : to exit
	""")
			choice =int(input("Enter Your Choice : "))


			if choice==1:
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
				print('''What you wanna do : 
	1 :launch python 
	2 :Create or edit a python code 
	3 :Run your python file
	4 :Install a package''')
				X=int(input("Enter your choice :"))
				what_py(X)
			elif choice==10:
				print("Enter Website or IP : ",end="")
				website=input()
				sys("nmap {0}".format(website))
			elif choice==11:
				sys("ifconfig")
			elif choice==12:
				print("Enter Website or IP : ",end="")
				website=input()
				sys("ping {0}".format(website))
			elif choice==13:
				sys("yum install httpd")
			elif choice==14:
				print("enter banner name : ",end="")
				banner_name=input()
				sys("figlet {0}".format(banner_name))
			elif choice==15:
				print("enter command : ",end="")
				new_cmd=input()
				sys("{0}".format(new_cmd))
			elif choice==16:
				sys("firefox")
			elif choice==17:
				printf("Enter name : ",end="")
				s_file=input()
				sys("locate {0}".format(s_file))    
			elif choice==18:
                                print("Enter the name of docker image", end="")
                                docker_img = input()
                                sys("docker pull {0}".format(docker_img)) 
                        elif choice==19:
				print("Please enter the container name:", end="")
				container_name = input()
				sys("docker container run -it --name {0} centos:7".format(container_name))  
			elif choice==20:
				sys("docker images")
			elif choice==21:
				sys("exit")
				print(colored("Thanks For Using","red"))
				break
			else :
				print(colored("Invalid Choice","red"))

elif location == 'remote':

        #menu-bar

	if x==password:
		while True:
			print("""Enter 1  : to login as root user
	Enter 2  : to see date & time 
	Enter 3  : to open calculator
	Enter 4  : to create new user
	Enter 5  : to install new software or tool
	Enter 6  : to open new terminal 
	Enter 7  : to open text-editor
	Enter 8  : to update whole system
	Enter 9  : to scan website using nmap
	Enter 10 : to check ip address
	Enter 11 : to ping
	Enter 12 : to configure web server
	Enter 13 : to create banners
	Enter 14 : to run any command
	Enter 15 : to launch browser
	Enter 16 : to search file or tool
        Enter 17 : to pull a docker image
	Enter 18 : to launch the docker container centos
	Enter 19 : to check the docker images
	Enter 20 : to exit
	""")
			choice =int(input("Enter Your Choice : "))


			if(choice==1):
				sys("ssh {0} sudo bash".format(ip))
			elif choice==2:
				sys("ssh {0} date".format(ip))
			elif choice==3:
				sys("ssh {0} bc".format(ip))
			elif choice==4:
				print("Enter user name : ",end="")
				create_user=input()
				sys("ssh {0} useradd {1}".format(ip,create_user))
			elif choice==5:
				print("Enter software name : ",end="")
				software_name=input()
				sys("ssh {0} sudo apt-get install {1}".format(ip,software_name))
			elif choice ==6:
				sys("ssh {0} gnome-terminal".format(ip))
			elif choice ==7:
				sys("ssh {0} gnome-text-editor".format(ip))
			elif choice==8:
				sys("ssh {0} sudo apt-get update".format(ip))
			elif choice==9:
				print("Enter Website or IP : ",end="")
				website=input()
				sys("ssh {0} nmap {1}".format(ip,website))
			elif choice==10:
				sys("ssh {0} ifconfig".format(ip))
			elif choice==11:
				print("Enter Website or IP : ",end="")
				website=input()
				sys("ssh {0} ping {1}".format(ip,website))
			elif choice==12:
				sys("ssh {0} yum install httpd".format(ip))
			elif choice==13:
				print("enter banner name : ",end="")
				banner_name=input()
				sys("ssh {0} figlet {1}".format(ip,banner_name))
			elif choice==14:
				print("enter command : ",end="")
				new_cmd=input()
				sys("ssh {0} {1}".format(ip,new_cmd))
			elif choice==15:
				sys("ssh {0} firefox".format(ip))
			elif choice==16:
				printf("Enter name : ",end="")
				s_file=input()
				sys("ssh {0} locate {1}".format(ip,s_file))
			elif choice==17:
                                print("Enter the name of docker image", end="")
                                docker_img = input()
                                sys("ssh {0}docker pull {1}".format(ip,docker_img))
                        elif choice==18:
				print("Please enter the container name:", end="")
				container_name = input()
				sys("ssh {0} docker container run -it --name {1} centos:7".format(ip,container_name))
			elif choice==19:
				sys("ssh {0} docker images".format(ip))
			elif choice==20:
				sys("ssh {0} exit".format(ip))
				print(colored("Thanks For Using","red"))
				break
			else :
				print(colored("Invalid Choice","red"))
else:

    print("Location not found")
