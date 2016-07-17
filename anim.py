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
      if (5/math.pow(math.sqrt(math.pow(mbA[0]-j,2)+math.pow(mbA[1]-i,2)),meatgoo))+ (9/math.pow(math.sqrt(math.pow(mbB[0]-j,2)+math.pow(mbB[1]-i,2)),meatgoo))+ (3/math.pow(math.sqrt(math.pow(mbC[0]-j,2)+math.pow(mbC[1]-i,2)),meatgoo))>meatt:
        grid[j][i]="10"

  return grid

# First set up the figure, the axis, and the plot element we want to animate
fig=plt.figure()
line, =plt.subplot(1, 1, 1)
plt.title('default: no edges')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
  grid=meatballs(grid, i)
  Z=numpy.array(grid).astype(numpy.int)
  c = plt.pcolor(Z)
  line.set_data(x, y)
  return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('graphtro.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
