"""
7.1) Write a function ball_collide that takes two balls as parameters and computes if they
are colliding. Your function should return a Boolean representing whether or not the balls
are colliding. Hint: Represent a ball on a plane as a tuple of (x, y, r), r being the radius
If (distance between two balls centers) <= (sum of their radii) then (they are colliding)
"""
import math
def ball_collide(ball_1,ball_2):
    d=math.sqrt((ball_1[0]-ball_2[0])**2 +(ball_1[1]-ball_2[1])**2)
    if(d<=(ball_1[2]+ball_2[2])):
        return True
    else:
        return False
x1=int(input("x1="))
y1=int(input("y1="))
r1=int(input("r1="))
x2=int(input("x2="))
y2=int(input("y2="))
r2=int(input("r2="))
ball_1=(x1,y1,r1)
ball_2=(x2,y2,r2)
collision=ball_collide(ball_1,ball_2)
if(collision):
    print("Balls are collide.")
else:
    print("Balls are not collide.")
"""
x1=-2
y1=-2
r1=3
x2=1
y2=1
r2=3
Balls are collide.
"""
