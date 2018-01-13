arr=[]
fp = open("db_q1.txt.txt","r")

lines = fp.readlines()
print(lines)
for line in lines:
    "".join(line)
    line = line.split()
    arr.append([line[0],line[1],line[2]])
 	
fp.close()
print(arr)

field = input("Enter field to be added : ")

val =0
if(field=="ID"):
    for i in range(0,len(arr)):
        #for j in i:
        k = int(arr[i][0])
        print(k)
        val = val+k
        
    print(val)
elif(field=="Status"):
    print("Error:Cannot Sum String Values")
elif(field=="Price"):
    for i in range(0,len(arr)):
        k = float(arr[i][2])
        val = val+k
    print(val)
    
    

