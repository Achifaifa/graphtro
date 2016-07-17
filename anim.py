import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math

grid=[[0 for i in range(50)] for j in range(50)]

meatt=1.4
meatgoo=0.95
def meatballs(grid,step):

  meatang=3.14*step/150;
  mbA=[25+math.cos(meatang*5)*20,25+math.sin(meatang*2)*20]
  mbB=[25+math.sin(meatang*2.6)*20,25+math.cos(meatang*2.0)*20]
  mbC=[25+math.sin((meatang*2)+100)*20,25+math.cos(meatang+50)*20]
  for i in range(50):
    for j in range(50):
      try:
        if (5/math.pow(math.sqrt(math.pow(mbA[0]-j,2)+math.pow(mbA[1]-i,2)),meatgoo))+ (9/math.pow(math.sqrt(math.pow(mbB[0]-j,2)+math.pow(mbB[1]-i,2)),meatgoo))+ (3/math.pow(math.sqrt(math.pow(mbC[0]-j,2)+math.pow(mbC[1]-i,2)),meatgoo))>meatt:
          grid[j][i]="10"
        else: 
          grid[j][i]="0"
      except: pass
  return grid

fig=plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0,50))
line, = ax.plot([], [], lw=2)
plt.title('default: no edges')

def init():
    line.set_data([], [])
    return line,

def animate(i):
  global grid
  grid=meatballs(grid, i)
  Z=np.array(grid).astype(np.int)
  c = plt.pcolor(Z)
  return c

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=60, interval=20, blit=True)
anim.save('graphtro.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
