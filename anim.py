import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import LinearSegmentedColormap
import math, random

grid=[[0 for i in range(50)] for j in range(50)]
text="""
Ever seen metaballs done in matplotlib?
                          Look at the awesome axis, it's off the charts!!
                          Greetings go to:   
    stage7 | Yawin | halcy & SVatG | Klon | Marcan | Imobilis | Euskal Encounter crew & scene people
                          I'll have a proper demo next time, promise! ;P
""".replace("\n", "")

needed_frames=(len(text)*3)+150

cube=[(-10,10,-10),(10,10,-10),(10,-10,-10),(-10,-10,-10),
      (-10,10,10), (10,10,10), (10,-10,10), (-10,-10,10) ]

def rotate_3dpoint(p, angle, ax):
  r = [0, 0, 0]
  ca = math.cos(angle)
  sa = math.sin(angle)
  r[0]+=(ca+(1-ca)*ax[0]*ax[0])*p[0]
  r[0]+=((1-ca)*ax[0]*ax[1]-ax[2]*sa)*p[1]
  r[0]+=((1-ca)*ax[0]*ax[2]+ax[1]*sa)*p[2]
  r[1]+=((1-ca)*ax[0]*ax[1]+ax[2]*sa)*p[0]
  r[1]+=(ca+(1-ca)*ax[1]*ax[1])*p[1]
  r[1]+=((1-ca)*ax[1]*ax[2]-ax[0]*sa)*p[2]
  r[2]+=((1-ca)*ax[0]*ax[2]-ax[1]*sa)*p[0]
  r[2]+=((1-ca)*ax[1]*ax[2]+ax[0]*sa)*p[1]
  r[2]+=(ca+(1-ca)*ax[2]*ax[2])*p[2]
  return r

def rotate_object(obj, angle, axis):
  """Rotate an object around given axis."""
  for n,i in enumerate(obj):
      obj[n] = rotate_3dpoint(i, angle, axis)

def rotcube(step):

  step=int(math.floor(step/5))
  global cube

  rotate_object(cube, (0.5+0.5*math.sin(step/35))/30  , (0,1,0))
  rotate_object(cube, (0.75+0.75*math.cos(step/50))/30, (0,0,1))
  rotate_object(cube, (1+math.sin(step/30))/30        , (1,0,0))
  grid=[[0 for i in range(50)] for j in range(50)]
  tempvert=[tuple(j+25 for j in i) for i in cube]
  for i in tempvert: grid[int(i[0])][int(i[1])]=i[2]
  return grid

meatt=1.4
meatgoo=0.95
def meatballs(step):

  grid=[[0 for i in range(50)] for j in range(50)]
  step+=1
  meatang=3.14*step/150;
  mbA=[25+math.cos(meatang*5)*20,25+math.sin(meatang*2)*20]
  mbB=[25+math.sin(meatang*2.6)*20,25+math.cos(meatang*2.0)*20]
  mbC=[25+math.sin((meatang*2)+100)*20,25+math.cos(meatang+50)*20]
  for i in range(50):
    for j in range(50):
      if (5/math.pow(math.sqrt(math.pow(mbA[0]-j,2)+math.pow(mbA[1]-i,2)),meatgoo))+ (9/math.pow(math.sqrt(math.pow(mbB[0]-j,2)+math.pow(mbB[1]-i,2)),meatgoo))+ (3/math.pow(math.sqrt(math.pow(mbC[0]-j,2)+math.pow(mbC[1]-i,2)),meatgoo))>meatt:
        grid[j][i]="10"
      else: 
        grid[j][i]="0"
  return grid

def scroll(text, step):

  base=["" for i in range(50-step)]
  stp=0 if step-50<0 else step
  txt=[i for i in text[stp:step]]
  return base+txt

#0f380f Darkest Green   Hex: #0f380f RGB: 15, 56, 15
#306230 Dark Green      Hex: #306230 RGB: 48, 98, 48
#8bac0f Light Green     Hex: #8bac0f RGB: 139, 172, 15
#9bbc0f Lightest Green  Hex: #9bbc0f RGB: 155, 188, 15

cdict={'red':   ((0.0, 0.0, 0.15),
                 (0.25, 0.15, 0.48),
                 (0.50, 0.48, 0.139),
                 (0.75, 0.139, 0.155),
                 (1.00, 0.155, 0.155)),

       'green': ((0.0, 0.0, 0.56),
                 (0.25, 0.56, 0.98),
                 (0.50, 0.98, 0.172),
                 (0.75, 0.172, 0.188),
                 (1.00, 0.188, 0.188)),

       'blue':  ((0.0, 0.0, 0.15),
                 (0.25, 0.15, 0.48),
                 (0.50, 0.48, 0.15),
                 (0.75, 0.15, 0.15),
                 (1.00, 0.15, 0.15)),
      }

plt.register_cmap(name='gbmap', data=cdict)

fig=plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0,50))
line, = ax.plot([], [], lw=2)
plt.title('Graphtro :D')
plt.ylabel('Awesome ->')
plt.xticks(range(50), [""])
plt.yticks(range(2,48), ["_" for i in range(50)])

def init():
  line.set_data([], [])
  return line,

def animate(i):
  global grid
  # grid=meatballs(i)
  grid=rotcube(i)
  Z=np.array(grid).astype(np.int)
  c=plt.pcolor(Z, cmap='gbmap')

  plt.xticks(range(50), scroll(text, int(math.floor(i/3)) ))
  awesomeh=random.randint(5, int(math.floor(35+15*math.sin(i/4))))
  plt.yticks(range(1,50), ["_" for i in range(awesomeh)])
  return c

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=60, interval=20, blit=True)
anim.save('./output/graphtro.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#ffmpeg -i input.mp4 -i input.mp3 -c copy -map 0:0 -map 1:0 output.mp4