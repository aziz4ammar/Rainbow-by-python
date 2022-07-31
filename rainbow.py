from turtle import *
colors=["red","orange","yellow","green", "blue","purple","pink"]
setup (600,500)
speed ("fastest")
bgcolor ("deepskyblue")
up ()
x=300
y=-100
r=300
for i in range (7) :
    goto (x,y)
    left (90)
    fillcolor (colors[i])
    begin_fill ()
    circle (r,180)
    end_fill ()
    left (90)
    x=x-20
    r=r-20
pensize (7)
x=-300
b=100
n=120
y=-100
goto (x,y)
for i in range (3):
    fillcolor ("gray")
    begin_fill ()
    for i in range(3):
        fd (b)
        left (n)
    fd (b)
    end_fill ()
    b=b+100
goto (-300,-100)
fillcolor ("green")
begin_fill ()
for i in range (2) :
    fd (600)
    right (90)
    fd (150)
    right (90)
end_fill ()
hideturtle ()
