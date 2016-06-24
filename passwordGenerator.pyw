# -*- coding: utf-8 -*-

#PYTHON 2.4


import random
import math
from Tkinter import *
import tkFont

global letters
global numbers
global characters
global mode
global length
global password

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
characters= ["!","@","#","$","%","&","","(",")","=","?","¿","¡",":",";","-","_","^","*"]
mode=0
length=0
password=""

def generateRandom(array): #Generates a random number between 0 and the size of the array.
	return random.randint(0, len(array)-1)

def randomizeArray(array): #Randomizes the elements of the array.
	return ''.join(random.sample(array,len(array)))

def simple(n): #Returns a password wich contains only letters. The length of the password depends of n.
	res = ""
	for i in range(n):
		rand = generateRandom(letters)
		res+=letters[rand]
	return res	

def common(n): #Returns a password with letters and numbers. The length of the password depends of n. 
	length=math.floor(n/2)
	res = ""
	for i in range(int(length)+(n%2)):
		rand = generateRandom(letters)
		res+=letters[rand]
	for i in range(int(length)):
		rand = generateRandom(numbers)
		res+=numbers[rand]
	return randomizeArray(res)	

def complex(n): #Returns a password with letters, numbers and ASCII characters. The length of the password depends of n.
	length=math.floor(n/3)
	res = ""
	for i in range(int(length)+(n%3)):
		rand = generateRandom(letters)
		res+=letters[rand]
	for i in range(int(length)):
		rand = generateRandom(numbers)
		res+=numbers[rand]
	for i in range(int(length)):
		rand = generateRandom(characters)
		res+=characters[rand]		
	return randomizeArray(res)		


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def changeMode(value):    
    mode = value

def changeLength(value):    
    length = value   

def update_Stringvar(new,stringvar):
    stringvar.set(new)    

def copyClipboard(text):
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(text)
	r.destroy()

def window():
	window=Tk()
	window.config(bg="honeydew3")
	window.resizable(0,0)
	w = 400 # width for the Tk root
	h = 450 # height for the Tk root
	ws = window.winfo_screenwidth() # width of the screen
	hs = window.winfo_screenheight() # height of the screen
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))
	buttons={"mode": 1, "length": 1}

	font1 = tkFont.Font(family="Times New Roman", size=12)
	text = Text(window, bg="honeydew3", bd=0, width=80, height=6, font= font1)
	text.pack()
	text.insert('1.0', "\n   Password generator. Please, select the type of your password.\n\n\t [1] Simple, with just letters. \n\t [2] Common, with letters and numbers. \n\t [3] Complex, also with ASCII characters.")
	
	text2 = Text(window, bg="honeydew3", bd=0, width=80, height=6, font= font1)
	text2.pack()
	text2.place(x=0, y=180)
	text2.insert('1.0', "\n   Please, select the length of your password.\n   It must be higher than 7.")

	modeText=StringVar()
	mode=StringVar()
	lengthText=StringVar()
	lengthEntry=StringVar()
	passwordText=StringVar()

	label1=Label(window,textvariable=modeText)
	label1.pack()
	label1.config(bg="honeydew3",width=5, height=3)
	label1.place(x=190,y=308)

	label2=Label(window,textvariable=lengthText)
	label2.pack()
	label2.config(bg="honeydew3", width=3, height=2)
	label2.place(x=288,y=315)
	
	entry1=Entry(window,textvar=lengthEntry)
	entry1.pack()
	entry1.place(x=100, y=260)

	b1=Button(window, text="MODE 1",command=lambda *args: combine_funcs(changeMode(1),update_Stringvar("1",modeText)))
	b1.pack()
	b1.place(x=80, y=150)
	b2=Button(window, text="MODE 2",command=lambda *args: combine_funcs(changeMode(2),update_Stringvar("2",modeText)))
	b2.pack()
	b2.place(x=160, y=150)
	b3=Button(window, text="MODE 3",command=lambda *args: combine_funcs(changeMode(3),update_Stringvar("3",modeText)))
	b3.pack()
	b3.place(x=240, y=150)

	b4=Button(window, text="Send", command=lambda *args: combine_funcs(changeLength(int(lengthEntry.get())), update_Stringvar(lengthEntry.get(),lengthText)))
	b4.pack()
	b4.place(x=240, y=258)

	text3 = Text(window, bg="honeydew3", bd=0, width=25, height=2, font= font1)
	text3.pack()
	text3.place(x=0, y=300)
	text3.insert('1.0', "\n   Generate password with mode:", " and length: ") 

	text4 = Text(window, bg="honeydew3", bd=0, width=9, height=1, font= font1)
	text4.pack()
	text4.place(x=216, y=319)
	text4.insert('1.0', " and length:") 

	def selectType(n, m):
		global password
		if(n==1 and m>7):
			password = simple(m)
		elif(n==2 and m>7):
			password = common(m)	
		elif(n==3 and m>7):
			password = complex(m)
		else:
			password=" Invalid lenght"
		return password							

	label3=Label(window,textvariable=passwordText)
	label3.pack()
	label3.config(bg="honeydew3", width=16, height=2)
	label3.place(x=190,y=370)				

	b5=Button(window, text="Generate", command=lambda *args: combine_funcs(selectType(int(modeText.get()), int(lengthText.get())), update_Stringvar(password,passwordText)))
	b5.pack()
	b5.place(x=328, y=318)


	text5 = Text(window, bg="honeydew3", bd=0, width=9, height=1, font= font1)
	text5.pack()
	text5.place(x=110, y=375)
	text5.insert('1.0', " Password:") 

	b6=Button(window, text="Copy", command=lambda *args: copyClipboard(password))
	b6.pack()
	b6.place(x=300, y=372)

	

	window.mainloop()


window()


''' ######################  ON CONSOLE: #########################

mode=input("Password generator. Please, select the type of your password. It can be: \n\n\t [1]-> Simple, with just letters. \n\t [2]-> Common, with letters and numbers. \n\t [3]-> Complex, also with ASCII characters.\n\n\t MODE: ")
length=input("\nPlease, select the length of your password, It must be higher than 7.\n\n\t Length: ")
if(mode==1):
	print("\n\tPassword: %s" % simple(length))
elif(mode==2):
	print("\n\tPassword: %s" % common(length))
elif(mode==3):
	print("\n\tPassword: %s" % complex(length))
else:
	print("\n\tThe length must be higher than 7.")	

'''



''' ######################  TEST: #########################

for i in range(8, 17):
	print("Length: %d" %i)
	print("Simple password: %s length: %d " % (simple(i), len(simple(i))))
	print("Common password: %s length: %d " % (common(i), len(common(i))))
	print("Complex password: %s length: %d \n" % (complex(i), len(complex(i))))

'''






#exit = raw_input("\n\n\nPress enter to exit.")