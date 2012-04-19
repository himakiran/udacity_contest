# This code attempts to visualise Pi by giving color to each decimal from 0 to 10 and painting the same in the order of digits in Pi
# Spigot algorithm code to generate digits of Pi has been copied from http://davidbau.com/downloads/pi.py the original pi.py is att below


TOTAL = 1000 # Parameter passed to the Pi digits generating function
WIDTH = 1280  # The width of the Canvas rectangle on which we draw Pi
HEIGHT = 800  # The height of the Canvas rectangle on which we draw Pi
PIXEL_COUNT = 8 # Each digit of Pi is represented by a coloured rectangle of size PIXEL_COUNT by PIXEL_COUNT

# THis function generates the digits of Pi. The number of digits generated depends on the parameter . While i could not find an exact co-relation between
# the value of Total and the no of digits of Pi generated the below table might prove useful
# TOTAL         No_Of_Pi_Digits Generated
# 10            2
# 100           24
# 1000          233
# 10000         2316

def decimal_digits(num):
  """Proved-correct generator for digits of pi"""
  q,r,t,k,n,l = 1,0,1,1,3,3
  #while True:
  #replaced above with a for statement
  for j in range(num):
    if 4*q+r-t < n*t:
      yield n
      q,r,t,k,n,l = (10*q,10*(r-n*t),t,k,(10*(3*q+r))//t-10*n,l)
    else:
      q,r,t,k,n,l = (q*k,(2*q+r)*l,t*l,k+1,(q*(7*k+2)+r*l)/(t*l),l+2)

#digits is a generator object which generates each digit of Pi. we use this object inside a for loop to generate the digits one by one
digits = decimal_digits(TOTAL)

# This code below draws a canvas on which we want to paint Pi
from Tkinter import *
top = Tk()
top.title("VISUALISING PI")

canvas = Canvas(top,width=WIDTH, height=HEIGHT, bg='white')
canvas.pack(expand=YES, fill=BOTH)


# I created a colors dictionary in which i tried to match numbers to colors using VIBGYOR and RGB values of colors
# ie 0,0,0 for black to 0,0,255 for blue,... to 255,255,255 for white
# in that order

colors ={0:'black',1:'Violet',2:'blue',3:'green',4:'yellow',5:'orange',6:'red',7:'magenta',8:'cyan',9:'white'}
i = 0
j = 0
k = i+PIXEL_COUNT
l = j + PIXEL_COUNT
count=0

# This code below generates the digits of Pi one by one using the generator object 'digits' and then using the colors dictionary finds
# the color of each of the digit and paints the rectangle in the canvas filled with that color

for each in digits:
    
    canvas.create_rectangle(i, j, k, l, width=0, fill=colors[each])
    count+=1
    
    i+=PIXEL_COUNT
    k+=PIXEL_COUNT
    # this code segment enables to paint the digits in the next line as the previous line equals the canvas rectangle width
    if i > WIDTH and i % WIDTH == 0:
        
        j+=PIXEL_COUNT
        l+=PIXEL_COUNT
        i=0
        k=PIXEL_COUNT
print "Total no of digits in Pi painted is :"
print count

        
mainloop()

