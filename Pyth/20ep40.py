#สร้างขอบตาราง

size = int(input("Insert number : "))

# print('ขนาดที่ต้องการ คือ ', size, 'x', size)

for i in range (1,size+1):
    if i == 1 or i == size:
        for j in range (1,size+1):
            print('x', end = '')
    else:
        for j in range (1,size+1):
            if j == 1 or j == size:
                print('x', end = '')
            else:
                print(' ', end = '')
    
    print(' ')
