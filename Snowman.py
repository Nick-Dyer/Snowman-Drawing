from turtle import *

speed(0)
setup(800, 700)


#Blue Background
penup()
goto(0, -320)
pendown()
color("lightskyblue")
begin_fill()
circle(320)
end_fill()


#Bottom of body
penup()
goto(0, -280)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

#Middle of body
penup()
goto(0, -110)
pendown()
color("white")
begin_fill()
circle(90)
end_fill()

#Top of body
penup()
goto(0, 20)
pendown()
color("white")
begin_fill()
circle(70)
end_fill()



#Function for small black circles

def black_circle():
    color("black")
    begin_fill()
    circle(10)
    end_fill()



#Eyes
x = -20
for i in range(2):
    penup()
    goto(x,110)
    pendown()
    black_circle()

    x += 40


#Buttons
y = 0
for i in range (4):
    penup()
    goto(0,y)
    pendown()
    black_circle()
    y -= 55


#Mouth
penup()
goto(0,70)
pendown()
color("red")
begin_fill()
circle(17)
end_fill()

penup()
goto(0,75)
pendown()
color("white")
begin_fill()
circle(17)
end_fill()


#Right Arm
penup()
goto(75,0)
pendown()
color("brown")
begin_fill()
left(40)
for i in range(2):
    fd(75)
    lt(90)
    fd(7)
    lt(90)
end_fill()


#Right Finger 1
penup()
goto(115, 38)
pendown()
begin_fill()
left(40)
for i in range(2):
    fd(25)
    lt(90)
    fd(5)
    lt(90)
end_fill()

#Right Fnger 2
begin_fill()
rt(100)
for i in range(2):
    fd(25)
    lt(90)
    fd(5)
    lt(90)

end_fill()


#Left Arm
penup()
goto(-130,50)
pendown()
color("brown")
begin_fill()
right(10)
for i in range(2):
    fd(75)
    lt(90)
    fd(7)
    lt(90)
end_fill()


#Left Finger 1
penup()
goto(-112, 58)
pendown()
begin_fill()
right(40)
for i in range(2):
    fd(25)
    lt(90)
    fd(5)
    lt(90)
end_fill()

#Left Fnger 2
penup()
goto(-108, 41)
pendown()
begin_fill()
rt(100)
for i in range(2):
    fd(25)
    lt(90)
    fd(5)
    lt(90)

end_fill()


# Hat
penup()
goto(50, 150)
pendown()
color("black")
begin_fill()
right(10)
forward(100)
right(90)
forward(10)
right(90)
forward(20)
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
left(90)
forward(20)
right(90)
end_fill()

#Text
penup()
goto(-100, 230)
pendown()

color("red")
write("WHATS GOOD NIGGA !", font = ("Arial", 20, "bold"))

hideturtle()
