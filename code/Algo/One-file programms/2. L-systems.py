import turtle as t
import random as r


d = {"1": "21",
     "0": "1[-0]+0"}
start = "0"
times = 11
angle = 20
dl = 12
stc = []
thik = 12

t.speed(0)
t.hideturtle()
t.tracer(0)
t.penup()
t.setpos(0, -300)
t.pendown()
t.lt(90)
t.pensize(thik)

def generate(st, times, d):
    res = ''
    for ch in st:
        if ch in d:
            res += d[ch]
        else:
            res += ch
    if times == 0:
        return st
    elif times == 1:
        return res
    else:
        return generate(res, times-1, d)

def turtle_do(moveset):
    global thik
    for ch in moveset:
        if ch == "1":
            t.fd(dl)
        elif ch == "2":
            if r.randint(0,10) > 4:
                t.fd(dl)
        elif ch == "0":
            t.color(r.choice(['#138808', '#009900', '#3caa3c', '#57a639', '#5da130', "#8ccb5e"]))
            t.pensize(1.5)
            t.fd(dl + r.randint(-5,5))
            t.pensize(1)
            t.color("black")
        elif ch == "-":
            t.rt(angle + r.randint(-12, 12))
        elif ch == "+":
            t.lt(angle + r.randint(-12, 12))
        elif ch == "[":
            thik = thik * 0.75
            t.pensize(thik)
            stc.append(thik)
            stc.append(t.xcor())
            stc.append(t.ycor())
            stc.append(t.heading())
        elif ch == "]":
            t.penup()
            t.setheading(stc.pop())
            t.sety(stc.pop())
            t.setx(stc.pop())
            thik = stc.pop()
            t.pensize(thik)
            t.pendown()

moveset = generate(start, times, d)
turtle_do(moveset)
t.mainloop()
print(r.randint(0, 10) < 5)