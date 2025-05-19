import turtle
import time

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("浪漫爱心")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# 定义颜色列表
colors = ["red", "pink", "orange", "purple", "yellow"]

# 定义爱心函数
def draw_heart(size, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.pensize(2)
    pen.penup()
    pen.goto(0, -size)
    pen.pendown()
    pen.begin_fill()
    pen.left(140)
    pen.forward(18 * size)
    pen.circle(-9 * size, 200)
    pen.setheading(60)
    pen.circle(-9 * size, 200)
    pen.forward(18 * size)
    pen.end_fill()

# 定义动态文字函数
text_pen = turtle.Turtle()
text_pen.speed(0)
text_pen.color("white")
text_pen.penup()
text_pen.hideturtle()

def show_text(text, size):
    text_pen.clear()
    text_pen.goto(0, -size // 2)
    text_pen.write(text, align="center", font=("Arial", size, "bold"))

# 主循环
texts = ["Love", "Forever", "Together"]
running = True  # 添加一个标志位控制循环
for i in range(100):
    if not running:
        break
    color = colors[i % len(colors)]
    size = 10 - i // 10
    draw_heart(size, color)
    if i % 10 == 0:
        text = texts[i // 30 % len(texts)]
        show_text(text, size * 5)
    time.sleep(0.1)

# 在循环结束后调用 turtle.done()，不再执行其他操作
turtle.done()