#!/usr/bin/env python

"""DESCRIPTION: This script creates a template python file with headers."""
"""USAGE: make_python.py author, progName, status(0-Prototype, 1-Development, 2-Production), email"""

__author__ = "Andrey Miroshnikov"
__copyright__ = "Copyright (C) 2018 Andrey Miroshnikov"
__license__ = "GPL"
__date__ = "Wed 25/04/2018 22:25:26 GMT-08"
__version__ = "1.0.1"
__maintainer__ = "Andrey Miroshnikov"
__email__ = "----"
__status__ = "Development"
__credits__ = "Andrey Miroshnikov"

#------------Imports------------
import sys
import os
import time
#------------Defines------------
YEAR = 0
MONTH = 1
DAY = 2
HOUR = 3
MINUTE = 4
SECOND = 5
WEEKDAY = 6
SKELETON_STRING = ("#------------Imports------------", "", "#------------Defines------------",
				   "", "#------------Variables------------", "", "#------------Functions------------",
				   "", "#------------Classes------------",
				   "", "#------------MAIN------------", "print(\"Hello World!\")")
#------------Variables------------
#author = "Andrey Miroshnikov"
#progName = "test_script"
#email = "abc@def.com"
#statusType = 1
#------------Functions------------
def checkArgs(args):
	if (len(args) < 1):
		print("USAGE: make_python.py author, progName, status, email")
	return 0
def convWeekday(intWeekday):
    weekdays = {0 : "Mon",
                1 : "Tue",
                2 : "Wed",
                3 : "Thu",
                4 : "Fri",
                5 : "Sat",
                6 : "Sun"
                }
    return weekdays[intWeekday]
def getTimeZone(timeZone):
	timeZone = (time.timezone)/(60*60)
	if (timeZone > 0):
		return "GMT-{:02.0f}".format(timeZone)
	else:
		return "GMT+{02.0f}".format(-1*timeZone)
def getStatus(statusType):
	status = {0 : "Prototype",
              1 : "Development",
              2 : "Production"
             }
	return status[statusType]
def writeStr(file, printString):
	for i in range(0, len(printString)):
		file.write(printString[i]+"\n")
def printStr(printString):
	for i in range(0, len(printString)):
		print(printString[i])
	
	
#------------MAIN------------
if (len(sys.argv) < 2):
	print(len(sys.argv))
	sys.exit("USAGE: make_python.py author, progName, status, email")
else:
	print(sys.argv[1])
	print(sys.argv[2])
	print(sys.argv[3])
	print(sys.argv[4])
	author = sys.argv[1]
	progName = sys.argv[2]
	statusType = int(sys.argv[3])
	email = sys.argv[4]
	
localTime = time.localtime(time.time())
year = localTime[YEAR]
timeZone = getTimeZone(time.timezone)
date = "{:s} {:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d} {:s}".format(convWeekday(localTime[WEEKDAY]), localTime[DAY], localTime[MONTH], localTime[YEAR], localTime[HOUR], localTime[MINUTE], localTime[SECOND], timeZone)
status = getStatus(statusType)
HEADER_STRING = ("#!/usr/bin/env python", "", "\"\"\"USAGE: "+progName+".py -ARGS\"\"\"",
				 "\"\"\"Description: -ADD DESCRIPTION HERE!-\"\"\"", "",
				 "__author__ = \""+author+"\"", "__copyright__ = \"Copyright (C) "+str(year)+" "+author+"\"",
				 "__license__ = \"GPL\"", "__date__ = \""+date+"\"", "__version__ = \"1.0.0\"",
				 "__maintainer__ = \""+author+"\"", "__email__ = \""+email+"\"",
				 "__status__ = \""+status+"\"", "__credits__ = \"ADD PEOPLE TO CREDIT\"", "")
#printStr(HEADER_STRING)
#printStr(SKELETON_STRING)
#------------File Operations------------
os.mkdir(progName)
file = open(progName+"/{:s}.py".format(progName), "w+")
writeStr(file, HEADER_STRING)
writeStr(file, SKELETON_STRING)
file.close()
	
