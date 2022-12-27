print("Enter 1 for copy, 2 for cut, 3 for paste ")
num = int(input())
file1 = open("select.txt","r+")
filestore = file1.readlines()

if(num==1):
    print("Enter the line number you want to copy")
    num1 =  int(input())
    if num1>=0 and num1<=len(filestore):
        line = filestore[num1-1]
        print("Enter starting index")
        num2 =  int(input())
        print("Enter ending index")
        num3 =  int(input())
        file2 = open("clipboard.txt","w")
        if num2>=0 and num2<len(line) and num3>=0 and num3<len(line):
            file2.write(line[num2:num3+1])
        else:
            print("Invalid index \n")
        file2.close()

elif(num==2):
    print("Enter the line number you want to cut")
    num1 =  int(input())
    if num1>=0 and num1<=len(filestore):
        line = filestore[num1-1]
        n = len(line)
        print("Enter starting index")
        num2 =  int(input())
        print("Enter ending index")
        num3 =  int(input())
        file2 = open("clipboard.txt","w")
        if num2>=0 and num2<len(line) and num3>=0 and num3<len(line):
            file2.write(line[num2:num3+1])
            text=line[0:num2]+" "+line[num3+1:n]
            filestore[num1-1] = text
            file3 = open("select.txt","w")
            for line in filestore:
                file3.write(line)
            file3.close()
        else:
            print("Invalid index \n")
        file2.close()
elif(num==3):
    file2 = open("clipboard.txt","r")
    file2.close()
else:
    print("Invalid Number \n")

file1.close()