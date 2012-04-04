"""
try_except.py
=====
Follow the instructions in the comments.

Example Output:
that key doesn't exist
that index doesn't exist
you tried to divide by 0!
incorrect type!
foo isn't defined
"""

# create a dictionary named d with key 'color', value 'red'
d ={"color":"red"}
# print out the value at key 'shape'
try:
		print d['shape']
except KeyError:
		print " That thing in that thing doesn't exist"
# what kind of error occurs? Keep that in mind so that you can...
#=-=-=-=-=-=-=- KeyError: 'shape' -==-=-=-=-=-==-=-==
# go back and add a try except block around it... make sure to catch the right kind of error!
# print out your own message regarding the error



# create a list named numbers and set it equal to a range(10)
numbers = range(10)
# print out the value at index 20
try:
		print numbers[20]
except IndexError:
		print "You listed a key thats out of range!!"
# what kind of error occurs? Keep that in mind so that you can...
#-=-=-=-=-===IndexError: list index out of range=-=-==-=-=-=
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try dividing 9 by 0
try:
		9 / 0
except ZeroDivisionError:
		print "learn devison"
# what kind of error occurs? Keep that in mind so that you can...
#-=-=-=-=-=-=-==-=-=-=-==-=-=-= ZeroDivisionError -=-=-=-=-=-=
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try dividing 9 by "a string"
try:
		9 / "sd;lfaskjfasd;lfjads"
except TypeError:
		print "dumb"
# what kind of error occurs? Keep that in mind so that you can...
#-=-=-=-==-=-=-=-= TYPE ERRORRR-=-=-=-==-=-=
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try calling a function that doesn't exist... for example, just type foo()
try:
		foo()
except NameError:
		print "not here"
# what kind of error occurs? Keep that in mind so that you can...
#-=-=-=-==-=-=-=-=-=-=NameError: name 'foo' is not defined-=-=-=-=-=--=-=
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error
