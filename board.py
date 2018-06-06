import turtle
turtle.penup();
turtle.goto(-600,340);
turtle.pendown();
#turtle.hideturtle();
turtle.shape('turtle');
for i in range(2):
     turtle.forward(1200);
     turtle.right(90);
     turtle.forward(680);
     turtle.right(90);
turtle.penup();
turtle.goto(-460,230);
turtle.pendown();
for i in range(2):
     turtle.forward(920);
     turtle.right(90);
     turtle.forward(460);
     turtle.right(90);
turtle.left(90);
for i in range (5):
    turtle.forward(110);
    turtle.right(90);
    turtle.forward(102.22);
    turtle.right(90);
    turtle.forward(110);
    turtle.left(90);
    if(i!=4):
        turtle.forward(102.22);
        turtle.left(90);
for i in range(5):
    turtle.forward(140);
    turtle.right(90);
    turtle.forward(51.11);
    turtle.right(90);
    turtle.forward(140);
    turtle.left(90);
    if(i!=4):
        turtle.forward(51.11);
        turtle.left(90);
for i in range (5):
    turtle.forward(110);
    turtle.right(90);
    turtle.forward(102.22);
    turtle.right(90);
    turtle.forward(110);
    turtle.left(90);
    if(i!=4):
        turtle.forward(102.22);
        turtle.left(90);
for i in range(5):
    turtle.forward(140);
    turtle.right(90);
    turtle.forward(51.11);
    turtle.right(90);
    turtle.forward(140);
    turtle.left(90);
    if(i!=4):
        turtle.forward(51.11);
        turtle.left(90);
turtle.exitonclick();  

