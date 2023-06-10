import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(600, 650)
screen.title('TamilNadu District Guessing game')
img ='TN_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv('TamilNadu.csv')
districts = data['district'].to_list()
print(districts)

answered_districts = 0
while answered_districts < 38:
    answer = screen.textinput(title='Guess the District ', prompt='District Name ?').title()

    if answer in districts:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        position = data[data['district']==answer]
        pen.goto(float(position.x), float(position.y))
        pen.pendown()
        pen.write(f'{answer}', font =("Courier", 11, "bold"))
        answered_districts+=1
        screen.title(f'{answered_districts}/38')

    if answer=='Exit':
        exit(0)
    
turtle.mainloop()