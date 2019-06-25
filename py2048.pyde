import random
import math

grid = []
score = 0

def addnewnumber(grid):
    emptyfields = findemptyfields(grid)
    if len(emptyfields) == 0:
        println("GAME ENDED")
    else:
        field = random.choice(emptyfields)
        grid[field[0]][field[1]] = 2 if random.randint(1,10)<10 else 4 #90% chance of 2  
        

def findemptyfields(grid):
    emptyfields = []
    for x in range(4):
        for y in range(4):
            if grid[x][y] == 0:
                emptyfields.append([x,y])
    return emptyfields

def showGrid():
    for x in range(4):
        for y in range(4):
            if grid[x][y]==0:
                fill(0,0,60) #gray
            else:
                fill(math.log(grid[x][y],2)*20, 100, 90)
            rect(x*width/4,y*width/4+height-width,width/4,width/4)
            fill(0,0,100)
            textSize(20)
            textAlign(CENTER,CENTER)
            text(str(grid[x][y]),x*width/4+width/8,y*width/4+width/8+height-width)

def showScore():
    textSize(50) 
    text(str(score),width*7/8,(height-width)/2)   
    

def setup():
    colorMode(HSB, 360, 100, 100);
    size(400, 480)
    background(0,0,80)

    #noStroke()
    stroke(0,0,80)
    strokeWeight(20)
    textAlign(CENTER,CENTER)
    
    score=0
    
    for i in range(4):
        line = []
        for j in range(4):
            line.append(0)
        grid.append(line)
    
    #println(grid)
    
    for i in range(2):
        addnewnumber(grid)    
    showGrid()
    
def draw():
    # Keep draw() here to continue looping while waiting for keys
    pass

def moveTogether_Up():
    moved = False
    for x in range(0,4):
        for y in range(0,3): #move together
            if grid[x][y]==0:
                for z in range(y+1,4):
                    if grid[x][z]!=0:
                        grid[x][y]=grid[x][z]
                        grid[x][z]=0
                        moved=True
                        break
    return moved

def moveTogether_Down():
    moved = False
    for x in range(0,4):
        for y in range(3,0,-1): #move together
            if grid[x][y]==0:
                for z in range(y-1,-1,-1): #down to 0
                    if grid[x][z]!=0:
                        grid[x][y]=grid[x][z]
                        grid[x][z]=0
                        moved=True
                        break
    return moved

def moveTogether_Left():
    moved = False
    for y in range(0,4):
        for x in range(0,3): #move together
            if grid[x][y]==0:
                for z in range(x+1,4):
                    if grid[z][y]!=0:
                        grid[x][y]=grid[z][y]
                        grid[z][y]=0
                        moved=True
                        break
    return moved

def moveTogether_Right():
    moved = False
    for y in range(0,4):
        for x in range(3,0,-1): #move together
            if grid[x][y]==0:
                for z in range(x-1,-1,-1):
                    if grid[z][y]!=0:
                        grid[x][y]=grid[z][y]
                        grid[z][y]=0
                        moved=True
                        break
    return moved

def checkUp():
    global score
    moved=moveTogether_Up()
    for x in range(0,4):
        for y in range(0,3):
            if grid[x][y]!=0 and grid[x][y]==grid[x][y+1]: #mergin possible
                grid[x][y]=2*grid[x][y] #merge
                grid[x][y+1]=0
                score+=grid[x][y]
                moved = True
                moveTogether_Up()
    return moved
            
def checkDown():
    global score
    moved=moveTogether_Down()
    for x in range(0,4):
        for y in range(3,0,-1): #[3,2,1]
            if grid[x][y]!=0 and grid[x][y]==grid[x][y-1]: #mergin possible
                grid[x][y]=2*grid[x][y] #merge
                grid[x][y-1]=0
                score+=grid[x][y]
                moved = True
                moveTogether_Down()
    return moved

def checkLeft():
    global score
    moved=moveTogether_Left()
    for y in range(0,4):
        for x in range(0,3):
            if grid[x][y]!=0 and grid[x][y]==grid[x+1][y]: #mergin possible
                grid[x][y]=2*grid[x][y] #merge
                grid[x+1][y]=0
                score+=grid[x][y]
                moved = True
                moveTogether_Left()
    return moved

def checkRight():
    global score
    moved=moveTogether_Right()
    for y in range(0,4):
        for x in range(3,0,-1):
            if grid[x][y]!=0 and grid[x][y]==grid[x-1][y]: #mergin possible
                grid[x][y]=2*grid[x][y] #merge
                grid[x-1][y]=0
                score+=grid[x][y]
                moved = True
                moveTogether_Right()
    return moved

def keyPressed():
    background(0,0,80)
    showGrid()
    if(key == CODED):
        if (keyCode == LEFT):
            if checkLeft() == True:
                addnewnumber(grid)
                showGrid()
        if (keyCode == RIGHT):
            if checkRight() == True:
                addnewnumber(grid)
                showGrid()
        if (keyCode == UP):
            if checkUp() == True:
                addnewnumber(grid)
                showGrid()
        if (keyCode == DOWN):
            if checkDown() == True:
                addnewnumber(grid)
                showGrid()
    showScore()
