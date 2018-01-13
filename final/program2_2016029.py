"""
ID Status Price lol
1 a 1.0 1
2 a 5.0 111
3 na 2.0 11111


Price Status ID lol
1.0 a 1 1
5.0 a 2 111
2.0 na 3 11111
5.0 a 10 wa
10.0 a 122 a

lol C 10
Price P 10
Status C 20
ID I 5
w


"""
import os
import time


def databaseModifier(l):
	for i in range(len(l)):
		l[i] = l[i][0]			#list of order in metadata
	newDatabase = [" ".join(l)]
	inp = open("database.txt", "r")
	dl = inp.readline().rstrip("\n\t")
	dl = dl.split()							#list of currently stored order
	nl=[]
	if "".join(l)!="".join(dl):
		for i in inp:
			if i==dl:
				continue
			i = i.rstrip("\n\r").split()
			j = i[:]
			for k in range(len(l)):
				j[k] = i[dl.index(l[k])]
			newDatabase.append(" ".join(j))
		inp.close()
	
		# with open("database.txt", "w") as output:
		# 	for i in newDatabase:
		# 		output.write(i+"\n")

def mainInterface():
	metadataList = []
	actualOrder=[]
	inp = open("metadata_2016029.txt", "r")
	for i in inp:
		i.rstrip("\n\t")
		metadataList.append(i.split())
	inp.close()
	#print (metadataList)
	met = metadataList[:]
	databaseModifier(metadataList)
	clearingVar = ''
	if os.name == "nt":
		clearingVar = "cls"
	if os.name == "posix":
		clearingVar = "clear"
	
	while True:
		#unused = os.system(clearingVar)
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
			l = []
			for i in range(len(metadataList)):
				l.append(input(metadataList[i]+":"))
			output = open("database.txt", "a")
			l = " ".join(l)
			l = l+"\n"
			output.write(l)
			output.close()
		elif inputChoice == 3:
			field = input("Enter the field name:")
			inp = open("database.txt", "r")
			tmp=[]
			for i in inp:
				tmp.append(i.split())
			inp.close()
			index = tmp[0].index(field)
			#print(met)
			flag = 1
			for i in met:
				if i[0] == field:
					if i[1] == 'C':
						print("Invalid input")
						flag = 0
			value = 0
			if flag != 0:
				# print(tmp)
				# print(index)
				for i in range(1, len(tmp)):
					value += float(tmp[i][index])
				print(value)


		elif inputChoice == 4:
			break
		else:
			print ("Wrong Input")
			time.sleep(1)

if __name__ == "__main__":
	mainInterface()