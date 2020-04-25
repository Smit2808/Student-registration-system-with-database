from tkinter import *
from PIL import ImageTk,Image #for image or icon
import sqlite3

# for making window 
root = Tk()
root.title("form application")
root.iconbitmap("icon.ico")


# creating form

# frame
frame = LabelFrame(root, text="Student registration form", padx=30, pady=30)
frame.pack(padx=10, pady=10)

#submit function
def submit():

	#create a database connection
	conn = sqlite3.connect("base.db")

	# create cursor
	c = conn.cursor()

	# when you are runing for first time then you have to create table, for runing 2nd time you have to comment the whole create part because now no need of creating table.
	#c.execute("""CREATE TABLE reg(
	#first_name text,
	#last_name text,
	#age integer,
	#gender text,
	#student_class text)""")


	# insert into table
	c.execute("INSERT INTO reg VALUES (:f_name, :l_name, :age, :gender, :student_class)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'age': age.get(),
				'gender': gender.get(),
				'student_class': student_class.get()
			}

		)

	# commit changes
	conn.commit()

	#close connection
	conn.close()

	# clear the text box for another record
	f_name.delete(0, END)
	l_name.delete(0, END)
	age.delete(0, END)
	gender.delete(0, END)
	student_class.delete(0, END)

# query button function
def query():

	#create a database connection
	conn = sqlite3.connect("base.db")

	# create cursor
	c = conn.cursor()

	c.execute("SELECT *, oid FROM reg")
	records = c.fetchall()
	print(records)

	#loop for results
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(frame, text=print_records)
	query_label.grid(row=7, column=0, columnspan=2)

	# commit changes
	conn.commit()

	#close connection
	conn.close()
	
# for entry
f_name = Entry(frame,width=30)
f_name.grid(row=0,column=1,padx=10)
l_name = Entry(frame,width=30)
l_name.grid(row=1,column=1,padx=10)
age = Entry(frame,width=30)
age.grid(row=2,column=1,padx=10)
gender = Entry(frame,width=30)
gender.grid(row=3,column=1,padx=10)
student_class = Entry(frame,width=30)
student_class.grid(row=4,column=1,padx=10)

# for label
f_name_label=Label(frame,text="First name: ")
f_name_label.grid(row=0,column=0)
l_name_label=Label(frame,text="Last name: ")
l_name_label.grid(row=1,column=0)
age_label=Label(frame,text="Age: ")
age_label.grid(row=2,column=0)
gender_label=Label(frame,text="Gender: ")
gender_label.grid(row=3,column=0)
student_class_label=Label(frame,text="Branch : ")
student_class_label.grid(row=4,column=0)

# submit button
submit_btn = Button(frame,text=" SUBMIT ", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# show query button
submit_btn = Button(frame,text=" SHOW RECORDS ", command=query)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=78)


root.mainloop()