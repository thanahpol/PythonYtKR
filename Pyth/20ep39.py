#สร้างตารางหมากฮอส

size = int(input("Insert number : "))

# print('ขนาดที่ต้องการ คือ ', size, 'x', size)

for i in range (1,size+1):
    if i%2 != 0:
        for j in range (1,size+1):
            if j%2 == 0:
                print('o', end = '')
            else:
                print('x', end = '')
    else:
        for j in range (1,size+1):
            if j%2 == 0:
                print('x', end = '')
            else:
                print('o', end = '')
    
    print(' ')
