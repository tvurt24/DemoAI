import turtle
import colorsys
import math
from collections import deque

turtle.setup(1000,1000)
turtle.hideturtle()
turtle.title("Tháp Hà Nội")
turtle.speed(0)
turtle.tracer(0,0)

n = 5 #Số đĩa mặc định
peg_height = 300
disk_height_max = 10
disk_width_max = 150
disk_width_min = 20
disk_delta = 15
disk_delta_max = 30
disk_height = 20
animation_step = 10

#Peg - A, B, C là đại diện cho 3 trụ
A = [] 
B = []
C = []

#Turtle
T = [] 

def draw_line(x,y,heading,length,pensize,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.fd(length)
    
def draw_scene():
    turtle.bgcolor('black')
    draw_line(-600,-200,0,1200,10,'white')
    for i in range(-250,251,250):
        draw_line(i,-196,90,peg_height,5,'white')

def initialize():    
    global disk_width_max,disk_width_min,disk_ratio,disk_delta
    for i in range(n):
        A.append(i)
        t = turtle.Turtle()
        t.hideturtle()
        t.pencolor('white')
        t.fillcolor('pink')
        T.append(t)
    disk_delta = min(135/(n-1),disk_delta_max)
    
def draw_single_disk(r, x, k, extra=0):
    global disk_delta
    
    w = disk_width_max - disk_delta*(r-1)
    T[r].up()
    T[r].goto(x-w/2,-195+disk_height*k + extra)
    T[r].down()
    T[r].seth(0)
    T[r].begin_fill()
    for i in range(2):
        T[r].fd(w)
        T[r].left(90)
        T[r].fd(disk_height)
        T[r].left(90)
    T[r].end_fill()
    
def draw_disks():
    for i in range(len(A)):
        draw_single_disk(A[i],-250,i)
    for i in range(len(B)):
        draw_single_disk(B[i],0,i)
    for i in range(len(C)):
        draw_single_disk(C[i],250,i)
  
def move_disk(source,target):
    if source == "A":
        x = -250
        P = A
    elif source == "B":
        x = 0
        P = B
    else:
        x = 250
        P = C

    if target =="A":
        x2 = -250
        Q = A
    elif target == "B":
        x2 = 0
        Q = B
    else:
        x2 = 250
        Q = C

    for extra in range(1,250-(-95+disk_height*(len(P)-1)),animation_step):
        T[P[len(P)-1]].clear()
        draw_single_disk(P[len(P)-1],x,len(P)-1,extra)
        turtle.update()

    T[P[len(P)-1]].clear()
    draw_single_disk(P[len(P)-1],x,len(P)-1,extra)
    turtle.update()
    tp = x
    if x2 > x:
        step = animation_step
    else:
        step = -animation_step
    for tp in range(x,x2,step):
        T[P[len(P)-1]].clear()       
        draw_single_disk(P[len(P)-1],tp,len(P)-1,extra)
        turtle.update()
    T[P[len(P)-1]].clear()
    draw_single_disk(P[len(P)-1],x2,len(P)-1,extra)
    turtle.update()
    Q.append(P[len(P)-1])
    del P[-1]
    for extra in range(250-(-95+disk_height*(len(Q)-1)),0,-animation_step):
        T[Q[len(Q)-1]].clear()
        draw_single_disk(Q[len(Q)-1],x2,len(Q)-1,extra)
        turtle.update()
    T[Q[len(Q)-1]].clear()
    draw_single_disk(Q[len(Q)-1],x2,len(Q)-1)
    turtle.update()   
    return

#Using recursion
def hanoi_recursion(X,Y,Z,n): #n là số cọc, X là cọc nguồn, Y là cọc trung gian, Z là cọc mục tiêu
    if n == 1:
        move_disk(X,Z)
        return
    hanoi_recursion(X,Z,Y,n-1)
    move_disk(X,Z)
    hanoi_recursion(Y,X,Z,n-1)

#Using stack
def hanoi_stack(n, X, Y, Z): #n là số cọc, X là cọc nguồn, Y là cọc trung gian, Z là cọc mục tiêu
    stack = []

    while True:
        while n>1:
            stack.append((n, X, Y, Z))
            n = n - 1
            X, Y, Z = X, Z, Y
        move_disk(X, Z)
        if stack:
            n, X, Y, Z = stack.pop()
            move_disk(X, Z)
            n = n - 1
            X, Y, Z = Y, X, Z
        else:
            break

draw_scene()
turtle.update()
n = int(turtle.numinput('Số lượng đĩa','Vui lòng nhập số lượng đĩa:',5,2,10))
#5 là số đĩa mặc định, số đĩa nhập vào phải >=2 và <=10

initialize()
draw_disks()
#hanoi_recursion("A","B","C",n)
hanoi_stack(n, "A", "B", "C")

turtle.update()

turtle.exitonclick()


