import os
import time


def mainInterface():
	metadataList = []
	inp = open("metadata_2016029.txt", "r")
	for i in inp:
		i.rstrip("\n\t")
		metadataList.append(i.split())
	#	print (metadataList)
	inp.close()
	clearingVar = ''
	if os.name == "nt":
		clearingVar = "cls"
	if os.name == "posix":
		clearingVar = "clear"
	while True:
		unused = os.system(clearingVar)
		print ("\t\t\t\t\t\tDATABASE INTERFACE\n\n\n")
		print ("\t1 : Display the database")
		print ("\t2 : Write to the database")
		print ("\t3 : Field Summation")
		print ("\t4 : exit")
		inputChoice = int(input())
		if inputChoice == 1:
			#1
			unused = os.system(clearingVar)
			print ("\t\t\t\t\t\tDATABASE CONTENT")
			inp = open("database.txt", "r")
			for i in inp:
				print (i, end="")
			inp.close()
			input()
		elif inputChoice == 2:
			#2
			print ()
		elif inputChoice == 3:
			#3
			print ()
		elif inputChoice == 4:
			break
		else:
			print ("Wrong Input")
			time.sleep(1)

if __name__ == "__main__":
	mainInterface()