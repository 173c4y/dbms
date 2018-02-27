"""
ID Status Price lol
1 a 1.0 1
2 a 5.0 111
3 na 2.0 11111


lol Price Status ID
1 1.0 a 1
111 5.0 a 2
11111 2.0 na 3
wa 5.0 a 10
a 10.0 a 122
p 10.5 na 234


lol C 10
Price P 10
Status C 20
ID I 5



"""
import os
import time


def databaseModifier(l):
	length = []
	dType = []
	# print (l)
	for i in range(len(l)):
		dType.append(l[i][1])
		length.append(l[i][2])
		l[i] = l[i][0]	#list of order in metadata
	newDatabase = [" ".join(l)]
	inp = open("database.txt", "r")
	dl = inp.readline().rstrip("\n\t")
	dl = dl.split()							#list of currently stored order
	nl=[]
	# print(length)
	# print (l)
	# print(dl)
	if "".join(l)!="".join(dl):
		for i in inp:
			if i==dl:
				continue
			i = i.rstrip("\n\r").split()
			j = i[:]
			for k in range(len(l)):
				j[k] = i[dl.index(l[k])]
				# print(k)
			j = j[:len(l)]
			print(j)
			for i in range(len(j)):
				j[i] = j[i][:int(length[i])]
				if dType[i] == "P" and j[i][-1] == ".":
					j[i] = j[i][:-1]
			print(j)
			newDatabase.append(" ".join(j))
		inp.close()
	
		with open("database.txt", "w") as output:
			for i in newDatabase:
				print(i+'\n')
				output.write(i+"\n")

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
	met2 = met[:]
	databaseModifier(metadataList)
	length = []
	dType = []
	# print (l)
	# print(metadataList)
	for i in range(len(met2)):
		dType.append(met2[i][1])
		length.append(met2[i][2])
	print(length)
	print(dType)
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
			print(l)
			for i in range(len(l)):
				print(length[i])
				l[i] = l[i][:int(length[i])]
				if dType[i] == "P" and l[i][-1] == ".":
					l[i] = l[i][:-1]
			l = " ".join(l)
			l = l+"\n"
			output.write(l)
			output.close()
			# databaseModifier(metadataList)
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