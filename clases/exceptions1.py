#!/usr/bin/python



try:
	while True:
		print "Hello World"
#except NameError:
	#print "l is not defined"
except KeyboardInterrupt:
	print "The program was closed"

finally:
	print "The program execution has finished"