import matplotlib.pyplot as plt
from numpy.random import rand
import math, numpy

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

meatballs(grid, 10)
Z = numpy.array(grid).astype(numpy.int)
# Z = rand(50,50)

plt.subplot(1, 1, 1)
c = plt.pcolor(Z)
plt.title('default: no edges')

plt.show()