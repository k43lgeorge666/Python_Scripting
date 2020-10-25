#!/usr/bin/python

def Create_File(file_name):

	list1 = []
	numbers = input("How many elements you want to enter:? ")
	for i in range(numbers):
		text = raw_input("Enter the text number " + str(i) + " : ")
		list1.append(text)

		files  = open(file_name, "w")

	for line in list1:
		files.write(line)
		files.write("\n")
	files.close()

	read = open(file_name, "r")
	read_lines = list(read)
	print(read_lines)
	read.close()

	edit = open(file_name, "ab")
	add_text = raw_input("Write the text you want to add: ")
	text = edit.write(add_text)
	edit.close()

def main():
	file = raw_input("Enter the file name: ")
	Create_File(file)

if __name__ == '__main__':
	main()




