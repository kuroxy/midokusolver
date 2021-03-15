import time
 
 
def printer(agrid): # speciale print functie voor een leesbaar antwoord  
    for i in agrid:
        for j in i:
            print(j,end=" ")
        print()
 
 
 
grid = [[0,0,0 ,0,0,0 ,0,0,0],
        [0,0,0 ,0,0,0 ,0,0,0],
        [0,0,0 ,0,0,0 ,0,0,0],
        
        [0,0,0 ,0,0,0 ,0,0,0],
        [0,0,1 ,0,0,0 ,0,0,0],
        [0,0,0 ,0,0,0 ,2,0,0],
        
        [0,0,0 ,0,0,0 ,0,0,0],
        [0,0,0 ,0,0,0 ,0,0,0],
        [0,0,0 ,0,0,0 ,0,0,0]]
 
allknight = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
 
#functie om de coördinaten van paardsprong te krijgen
def knight_moves(y,x):	
    returnlist = []
    for i in allknight:
        newx = i[0] + x
        newy = i[1] + y
        if newx >= 0 and newx < 9 and newy >= 0 and newy < 9:
            returnlist.append((newy,newx))
    return returnlist
 
#functie om de coördinaten van de koning te krijgen
def king_moves(y,x):
    returnlist = []
    for newy in range(y-1,y+2):
        for newx in range(x-1,x+2):
            if newy >= 0 and newy < 9 and newx >= 0 and newx < 9:
                returnlist.append((newy,newx))
    return returnlist
 
allorthomoves = [(-1,0),(1,0),(0,-1),(0,1)]
#functie om de coördinaten die er naast zitten te krijgen
def ortho_moves(y,x):
    returnlist = []
    for i in allorthomoves:
        newx = i[0] + x
        newy = i[1] + y
        if newx >= 0 and newx < 9 and newy >= 0 and newy < 9:
            returnlist.append((newy,newx))
    return returnlist
 
# deze functie checkt of dat een getal in een vakje klopt
def possible(y,x,n):
    global grid
    for i in range (0,9):       # verticale lijn check
        if grid[y][i] ==n:
            return False
        
    for i in range(0,9):        # horizontale lijn check
        if grid[i][x] ==n:  
            return False
        
    x0 = (x//3)*3               # subgrid check
    y0 = (y//3)*3   
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
 
    for i in knight_moves(y,x):  # paardsprong check
        y0,x0 = i
        if grid[y0][x0] == n:
            return False
 
    for i in king_moves(y,x):  # rondom check
        y0,x0 = i
        if grid[y0][x0] == n:
            return False
 
    for i in ortho_moves(y,x):  # orthogonaal aangrenzende check
        y0,x0 = i
        if grid[y0][x0] != 0:
            if abs(grid[y0][x0]-n) == 1:
                return False
    return True
 
# oplos functie door middel van backtracking
def solve():	
    global grid
    global latesttime
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    printer(grid)
    print("endtime",time.time())
	
 
print("begintime",time.time())
solve()
