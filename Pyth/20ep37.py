#ตัวเลขขั้นบันได

last = int(input("Insert number : "))

for i in range (1,last+1):
    for j in range (1,i+1):
        print(j, end = '')
    
    print(' ')
