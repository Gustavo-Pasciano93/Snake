# Jogo da Cobrinha 🐍

Bem-vindo ao repositório do jogo da Cobrinha! Este projeto foi desenvolvido em Python, utilizando o módulo `turtle` e o paradigma de Programação Orientada a Objetos (POO). O objetivo é recriar o clássico jogo da cobrinha, onde a cobra deve coletar comida para crescer enquanto evita colidir consigo mesma ou com as bordas da tela.

## Funcionalidades

- **Movimento da Cobrinha:** Controle a direção da cobra usando as teclas W (cima), S (baixo), A (esquerda) e D (direita).
- **Comida:** A comida aparece aleatoriamente na tela, e a cobra cresce ao coletá-la.
- **Pontuação:** A pontuação aumenta conforme a cobra coleta a comida. O jogo mantém o registro do maior placar.

## Estrutura do Projeto

O projeto está organizado em quatro arquivos principais:

### food.py

Define a classe `Food`, responsável pela criação e reposicionamento da comida.

```python
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)



### score.py

Define a classe Score, responsável por gerenciar e exibir a pontuação.

```python
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    def increase_score(self):
        self.score += 1
        self.update_score()



### snake.py

Define a classe Snake, responsável pela criação e movimento da cobra.

```python
from turtle import Turtle

START_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        cobra = Turtle()
        cobra.shape("square")
        cobra.shapesize(0.5, 0.5)
        cobra.color("white")
        cobra.penup()
        cobra.goto(position)
        self.segments.append(cobra)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



### main.py

Contém a lógica principal do jogo, integrando as outras classes.

```python
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A Cobra Vai Fumar")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset()
        
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()
            
    snake.move()
    
screen.exitonclick()
