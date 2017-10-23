import matplotlib.pyplot as plt
import math
import numpy as np

velo = int(input("Enter Initial Velocity (m/s): "))
angle = int(input("Enter Angle Of Projection (degrees): "))
rad = (math.pi/180)*angle

time_f = 2*velo*(math.sin(rad))/9.81
h = (velo**2)*((math.sin(rad))**2)/(2*9.81)
r = (velo**2)*(math.sin(2*rad))/9.81

velox = velo*(math.cos(rad))
veloy = velo*(math.sin(rad))

numx = []
numy = []
for i in (np.arange(0,int(time_f),0.1)):
    xdist = velo * i
    xvelo = velox
    ydist = (veloy*i)-(9.81*i**2)/2
    yvelo = veloy - (9.81*i)
    numx.append(xdist)
    numy.append(ydist)

plt.plot(numx,numy,color='blue')

velo1 = int(input("Enter Initial Velocity (m/s): "))
angle1 = int(input("Enter Angle Of Projection (degrees): "))
rad1 = (math.pi/180)*angle1

time_f1 = 2*velo1*(math.sin(rad1))/9.81
h1 = (velo1**2)*((math.sin(rad1))**2)/(2*9.81)
r1 = (velo1**2)*(math.sin(2*rad1))/9.81

velox1 = velo1*(math.cos(rad1))
veloy1 = velo1*(math.sin(rad1))

numx1 = []
numy1 = []
for t in (np.arange(0,int(time_f1),0.1)):
    xdist1 = velo1 * t
    xvelo1 = velox1
    ydist1 = (veloy1*t)-(9.81*t**2)/2
    yvelo1 = veloy1 - (9.81*t)
    numx1.append(xdist1)
    numy1.append(ydist1)

plt.plot(numx1,numy1,color='red')

velo2 = int(input("Enter Initial Velocity (m/s): "))
angle2 = int(input("Enter Angle Of Projection (degrees): "))
rad2 = (math.pi/180)*angle2

time_f2 = 2*velo2*(math.sin(rad2))/9.81
h2 = (velo2**2)*((math.sin(rad2))**2)/(2*9.81)
r2= (velo2**2)*(math.sin(2*rad2))/9.81

velox2 = velo2*(math.cos(rad2))
veloy2 = velo2*(math.sin(rad2))

numx2= []
numy2= []
for z in (np.arange(0,int(time_f2),0.1)):
    xdist2 = velo2 * z
    xvelo2 = velox2
    ydist2 = (veloy2*z)-(9.81*z**2)/2
    yvelo2 = veloy2 - (9.81*z)
    numx2.append(xdist2)
    numy2.append(ydist2)

plt.plot(numx2,numy2,color='yellow')
plt.show()

