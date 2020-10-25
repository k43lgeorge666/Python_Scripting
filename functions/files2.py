#!/usr/bin/python

import os

def Add_Text(file_name):

	list1 =[]
	quantity = input("How many lines you want to add?: ")
	for i in range(quantity):
		text = raw_input("Enter the text for the line number " + str(i) + " : ")
		list1.append(text)

		files = open (file_name,"w")

	for lines in list1:
		files.write(lines)
		files.write("\n")
	files.close()
	print ""

def Read_Text(file):

	read = open (file, "r")
	read_lines = list(read)
	print ""
	print(" ----- The Text in the file --------")
	print ""
	print(read_lines)
	read.close()


def Edit_File(file_id):

	edit = open(file_id, "ab")
	text_added = raw_input("Enter the text you want to add: ")
	edit_file = edit.write(text_added)
	edit.close()
	print ""


def Delete_File(file_name):

	if os.path.exists(file_name):
		os.remove(file_name)
		print("The file has been deleted")
	else:
		print("The file does not exist")
	print ""


def main():

	opc = 0

	while True:

		print ""
		print "--------------------------------------"
		print "[1] Create a file and add text        |"
		print "[2] Read the text in the file         |"
		print "[3] Add a text at the end of the file |"
		print "[4] Delete a file                     |"
		print "[5] Exit Program                      |"
		print "---------------------------------------"
		print ""

		opc = input("Select an option from the menu: ")

		if opc == 1:
			name = raw_input("Enter the file name: ")
			Add_Text(name)

		elif opc == 2:
			file_name = raw_input("Enter the file name to read: ")
			Read_Text(file_name)

		elif opc == 3:
			file = raw_input("Enter the file name to edit: ")
			Edit_File(file)

		elif opc == 4:
			element = raw_input("Enter the file name to delete: ")
			Delete_File(element)

		elif opc == 5:
			print "Exit Program...."
			print ""
			exit(0)

		else:
			print "The option selected does not exist"

if __name__ == '__main__':
	main()