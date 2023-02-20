#สร้างภาพวาดสี่เหลี่ยมจตุรัส

size = int(input("Insert number : "))

print('ขนาดที่ต้องการ คือ ', size, 'x', size)

for i in range (1,size+1):
    for j in range (1,size+1):
        print('x', end = '')
    
    print(' ')
