Jogo da cobrinha criado para treinar Orientação de Objetos. 
Foi utilizado neste projeto o python versão 3.12, dentro da ferramenta focamos na biblioteca Turtle para executar o projeto.

Para rodar o jogo criamos no vscodeuma aba main.py, uma score.py( para atualizar o score do jogo), uma food.py(criar a comida na tela para  a cobra seguir), e uma snake.py( onde criamos a cobra e seus movimentos).


Abaixo segue uma amostra do arquivo main:
#arquivo main
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A cobra vai fumar")
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
    
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    if snake.head.xcor() >280 or snake.head.ycor() < - 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        
        score.reset()
        snake.reset()
        
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <5:
            
            score.reset()
            snake.reset()
            
        

    
    snake.move()
    
    score.update_score()
    
    
    
screen.exitonclick()
    
    
    
screen.exitonclick()
