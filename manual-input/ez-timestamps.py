import re
import datetime

inputTime = input("Time to add: ")
(iH, iM, iS) = inputTime.split(':')
inputDT = datetime.timedelta(hours=int(iH), minutes=int(iM), seconds=int(iS))
inputFile = open("tempfile.txt")
outputFile = open("outputTimestamps.txt", "w")

for line in inputFile:
	if re.match(r'^[0-9]', line):
		x = line.split(' ')
		(h, m, s) = x[0].split(':')
		d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
		c = d + inputDT
		x[0] = str(c)
		joined = ' '.join(x)
		outputFile.write(joined)
	
	