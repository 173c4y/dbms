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




ans = True

while ans:
    print("""\n 1. Print Database \n 2. Find Summation of Fields \n 3. Exit\n""")
    option = input("Enter Option Number : ")
    if(option=="1"):
        print(arr)
    elif(option=="2"):
        field = input("\nEnter field to be added : ")
        val =0
        if(field=="ID"):
            for i in range(0,len(arr)):
                #for j in i:
                k = int(arr[i][0])
                print(k)
                val = val+k
            print(val)
        elif(field=="Status"):
            print("\nError : Cannot Sum String Values")
        elif(field=="Price"):
            for i in range(0,len(arr)):
                k = float(arr[i][2])
                val = val+k
            print(val)
    elif(option=="3"):
        ans=None
    else:
        print("\n Not Valid Choice Try Again")
        
        
        
          






    

