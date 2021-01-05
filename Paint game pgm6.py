from turtle import *
from freegames import vector

def line(start,end):
    up()
    goto(start.x,start.y)
    down()
    goto(end.x,end.y)

def square(start,end):
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start,end):
    "draw circle from start to end"
    pass
def rectangle(start,end):
    pass

def triangle(start,end):
    pass

def tap(x,y):
    start = state["start"]

    if start is None:
        state["start"]=vector(x,y)
    else:
        shape = state["shape"]
        end=vector(x,y)
        shape(start,end)
        state["start"]=None

def store(key,value):
    state[key]=value


state = {"start": None, "shape": line}
setup(420,420,370,0)
onscreenclick(tap)
listen()
onkey(undo, "u")
onkey(lambda: color("black"),"k")
onkey(lambda: color("white"),"w")
onkey(lambda: color("green"),"g")
onkey(lambda: color("blue"),"b")
onkey(lambda: color("red"),"r")
onkey(lambda : store("shape", line), "l")
onkey(lambda : store("shape", square), "s")
onkey(lambda : store("shape", circle), "c")
onkey(lambda : store("shape", rectangle), "r")
onkey(lambda : store("shape", triangle), "t")
done()

