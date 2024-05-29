from turtle import Turtle, Screen
import time


class Snake:
    """going to initalise the snake and make it move"""

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.turtle_zoo = []
        self.make_first_snake()

        # self.fruit = Turtle(shape = "circle")
        # self.fruit.color("yellow")
        # self.fruit.goto((20,20))



    def make_first_snake(self):
        for position in self.starting_positions:
            gay = Turtle(shape= "square")
            gay.pu()
            gay.color("white")
            gay.goto(position)
            self.turtle_zoo.append(gay)

    def turn_left(self):
        self.turtle_zoo[0].left(90)

    def turn_right(self):
        self.turtle_zoo[0].right(90)

    def grow(self):     #append a turtle to the list, and then move them all down


        new_gay = Turtle(shape="square")
        new_gay.pu()
        new_gay.color("white")
        new_gay.goto(self.starting_positions[-1])
        self.turtle_zoo.append(new_gay)
        self.starting_positions.append(self.starting_positions[-1])


    def snake_move(self):
        time.sleep(0.08)
        self.turtle_zoo[0].forward(20)
        #self.eat_and_grow()
        # print(starting_positions)
        for i in range(len(self.starting_positions), 1, -1):  # loops through the following sections of the snake
            self.starting_positions[i - 1] = self.starting_positions[i - 2]  # makes them change postion to the one that was
        # starting_positions[1] = starting_positions[0]          #in front of them
        self.starting_positions[0] = self.turtle_zoo[0].pos()
        for j in range(len(self.starting_positions)):
            self.turtle_zoo[j].goto(self.starting_positions[j])

        #screen.listen()
        #screen.onkeypress(fun=self.turn_left(self), key="a")
        #screen.onkeypress(fun=self.turn_right(self), key="d")

    def reset_snake(self):
        for turtle in self.turtle_zoo:
            turtle.goto(-400,-400)
        self.turtle_zoo.clear()
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.make_first_snake()

