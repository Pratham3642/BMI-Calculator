from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry("850x600+500+250")
root.title("BMI CALCULATOR BY PRATHAMESH MAVALKAR")
root.configure(bg="lightblue")
F = ("Century", 30 , "bold")
f = ("Century", 20 , "bold")

labtitle = Label(root,text="BMI CALCULATOR",font=F,bg="lightblue")
labtitle.place(x=230,y=30)


def age():
	try:
		age = entage.get()
		if age == "":
			raise ValueError("Please enter Age")
		if not (age.replace(".","").isdigit() or age[1:].replace(".","").isdigit()):
			raise ValueError("Age cannot be text or special characters")
		age = int(age)
		if age < 0:
			raise ValueError("Age cannot be negative")
		if age > 120:
			raise ValueError("Enter valid age")
		return age
	except (ValueError,Exception) as e:
		showerror("ERROR!!",e)
		entage.delete(0,END)


def height():
	try:
		height = entheight.get().strip()
		if height == "":
			raise ValueError("Please enter height")
		if not (height.replace(".","").isdigit() or height[1:].replace(".","").isdigit()):
			raise ValueError("Height cannot be text or speical characters")
		height = float(height)
		if height < 0:
			raise ValueError("Height cannot be negative")
		return height
	except (ValueError,Exception) as e:
		showerror("ERROR!!",e)
		entheight.delete(0,END)


def weight():
	try:
		weight = entweight.get().strip()
		if weight == "":
			raise ValueError("Please enter weight")
		if not (weight.replace(".","").isdigit() or weight[1:].replace(".","").isdigit()):
			raise ValueError("Weight cannot be text or speical characters")
		weight = float(weight)
		if weight < 0:
			raise ValueError("Height cannot be negative")
		return weight
	except (ValueError,Exception) as e:
		showerror("ERROR!!",e)
		entweight.delete(0,END)

def calculate():
	a = age()
	h = height()
	w = weight()
	if a is not None and h is not None and w is not None:
		bmi = calculatebmi(h,w)
		if bmi <= 15.0:
			res = "Your BMI is"+str(bmi)+"\nRemarks :Very severely underweight!"
		elif 16 <bmi <= 18.5:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Underweight!"
		elif 18.5 < bmi <= 25.0:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Normal!"
		elif 25.0 < bmi <= 30.0:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Overweight!"
		elif 30.0 < bmi <=35.0:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Moderately obese!" 
		elif 35.0 < bmi <= 40:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Severely obese!"
		else:
			res = "Your BMI is "+ str(bmi) +"\nRemarks :Super obese!"

		labbmi.configure(text=res)


def calculatebmi(height,weight):
		height = height/100.0
		bmi = weight/(height**2)
		bmi = round(bmi,2)
		return bmi

def clear():
	entage.delete(0,END)
	entheight.delete(0,END)
	entweight.delete(0,END)
	labbmi.configure(text="")
	entage.focus()


def exit():
	root.destroy()


labgender = Label(root,text="Gender :",font=f,bg="lightblue")
labgender.place(x=150,y=100)

c = IntVar()
c.set(1)
rdbtnmale = Radiobutton(root,text="Male",font=f,bg="lightblue", variable = c, value = 1)
rdbtnmale.place(x=300,y=100)
rdbtnfemale = Radiobutton(root,text="Female",font=f,bg="lightblue", variable = c, value = 2)
rdbtnfemale.place(x=450,y=100)

labage = Label(root,text="Age :",font=f,bg="lightblue")
labage.place(x=210,y=180)
entage = Entry(root,font=f,width=10)
entage.place(x=300,y=185)

labheight = Label(root,text="Height (in cms) :",font=f,bg="lightblue")
labheight.place(x=25,y=260)
entheight = Entry(root,font=f,width=10)
entheight.place(x=300,y=260)

labweight = Label(root,text="Weight (in kg) :",font=f,bg="lightblue")
labweight.place(x=40,y=330)
entweight = Entry(root,font=f,width=10)
entweight.place(x=300,y=330)

btnclear = Button(root,text="Clear",bg="skyblue",font=f,command=clear)
btnclear.place(x=150,y=400)

btncalculate = Button(root,text="Calculate",font=f,bg="skyblue",command=calculate)
btncalculate.place(x=300,y=400)

btnexit = Button(root,text="Exit",bg="skyblue",font=f,command=exit)
btnexit.place(x=520,y=400)

labbmi = Label(root,text="",font=f,bg="lightblue")
labbmi.place(x=230,y=490)






root.mainloop()