from p5 import *


def setup():
  createCanvas(400, 400)


def draw():
  background("black")
  drawTickAxes()

  squareSide = mouseX - 150
  circleX = 150 + squareSide/2
  radius =  squareSide/2
  squareArea = squareSide*squareSide
  triangleArea=squareSide*squareSide/2
  
  noFill()
  stroke('magenta')
  strokeWeight(4)
  circle(circleX,circleX,squareSide)
  triangle(150,150,circleX,squareSide+150,circleX+ squareSide/2,150)
  square(150,150,squareSide)

# CALCULATE THE AREAS
  circleArea = round(PI*radius*radius)

  
  textSize(20)
  strokeWeight(0)
  fill('magenta')
  text(f"Radius: {radius}", 100, 100)
  text(f"Square Area: {squareArea}", 100, 80)
  text(f"Circle Area: {circleArea}", 100, 60)
  text(f"Triangle Area: {triangleArea}", 100, 40)

