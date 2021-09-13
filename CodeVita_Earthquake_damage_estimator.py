

list1 = []
list2 = []

N = int(input("Enter the size of grid:"))

for i in range(0, N):
    t = []
    for j in range(0, N):
        t.append(int(input()))
        
    list1.append(t)
    
    
a, b = map(int, input("Enter the epicenter's co-ordinate:").split())
M = float(input("Enter the intensity of earthquake: "))

for i in range(0, N):
    t1 = []
    for j in range(0, N):
        t1.append(0)
        
    list2.append(t1)
    
    
def ways(row, col, Mag):
    
    if Mag <= 3.0:
        
        if row < 0 or row > (N-1) or col < 0 or col > (N-1):
            return
        
        elif list1[row][col] == 0:
            return
        
        elif list2[row][col] != 0:
            return
        
        else:
            list2[row][col] = 2
            
            
    elif Mag > 3.0 and Mag <= 5.0:
        
        list3 = [a-1-1, a-1, a-1+1]
        list4 = [b-1-1, b-1, b-1+1]
        
        if row < 0 or row > (N-1) or col < 0 or col > (N-1):
            return
        
        elif list1[row][col] == 0:
            return
        
        elif list2[row][col] != 0:
            return
        
        elif row in list3 and col in list4:
            list2[row][col] = 3
            
        else:
            list2[row][col] = 2
            
            
    elif Mag > 5.0 and Mag <= 8.0:
        
        list5 = [a-1-3, a-1-2, a-1-1, a-1, a-1+1, a-1+2, a-1+3]
        list6 = [b-1-3, b-1-2, b-1-1, b-1, b-1+1, b-1+2, b-1+3]
        
        
        if row < 0 or row > (N-1) or col < 0 or col > (N-1):
            return
        
        elif list1[row][col] == 0:
            return
        
        elif list2[row][col] != 0:
            return
        
        elif row in list5 and col in list6:
            list2[row][col] = 3
            
        else:
            list2[row][col] = 2
            
            
            
            
    elif Mag > 8.0:
        
        if row < 0 or row > (N-1) or col < 0 or col > (N-1):
            return
        
        elif list1[row][col] == 0:
            return
        
        elif list2[row][col] != 0:
            return
        
        else:
            
            list2[row][col] = 3
            
            
            
    ways(row+1, col+1, Mag)
    ways(row-1, col-1, Mag)
    ways(row+1, col-1, Mag)
    ways(row-1, col+1, Mag)
    ways(row+1, col, Mag)
    ways(row-1, col, Mag)
    ways(row, col+1, Mag)
    ways(row, col-1, Mag)
            
            

ways(a-1, b-1, M)


for i in range(0, len(list1)):
    e = len(list1[i])
    for j in range(0, e):
        if list1[i][j] == 1 and list2[i][j] == 0:
            list2[i][j] = 1
            
print(list2)
