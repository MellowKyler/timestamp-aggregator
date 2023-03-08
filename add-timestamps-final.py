import re
import datetime

userInput = input("Artist Name: ")
inputFile = open("timestamps.txt")
outputFile = open("finalTimestamps.txt", "w")

tempTime = datetime.timedelta(hours=0, minutes=0, seconds=0)

for line in inputFile:
	if line.startswith(userInput):
		outputFile.write(line)
	elif line.startswith('End time: '):
		x = line.split(' ')
		(h, m, s) = x[2].split(':')
		d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
		tempTime = d + tempTime
		#x[2] = (str(tempTime) + "\n\n")
		#joined = ' '.join(x)
		#outputFile.write(joined)
		outputFile.write("\n")
	elif re.match(r'^[0-9]', line):
		x = line.split(' ')
		(h, m, s) = x[0].split(':')
		d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
		c = d + tempTime
		x[0] = str(c)
		joined = ' '.join(x)
		outputFile.write(joined)
	