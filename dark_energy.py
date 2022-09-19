from panda3d.core import CollisionNode, CollisionBox, CollisionSphere, CollisionPolygon

from panda3d.core import NodePath

from ursina.vec3 import Vec3

from ursina.mesh import Mesh

from ursina import *
 
import random

from ursina.shaders import lit_with_shadows_shader

import math


p2 = float(input("enter the resisance power: "))
p = float(input("enter the gravitatioanl power: "))
G = float(input("enter the gravitatioanl constaint: "))
g = 1/float(input("enter the g force: "))
r = 1/(float(input("enter the resisance force: "))*2)
a = int(input("enter the lenth of the array: "))
b = int(input("enter the hight of the array: "))
c = int(input("enter the width of the array: "))
s = float(input("enter the size of each particle: "))
d = float(input("enter the distance between each particle: "))
I = float(input("enter inital velcity: "))
app = Ursina()

class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		position = position,
		color = color.white,
		model = 'sphere',
		texture = 'white_cube',
		scale = scale,
		origin_y = 0
		)
	def update(self):
		self.color =rgb( 255*math.cos(time.time()*(2**(0.5))+ self.x/100),
						
						255*math.cos(time.time()*(3**(0.5))+ self.y/100),
						 
						255*math.cos(time.time()*(5**(0.5) + self.z/100)))
			
		
	
v = [[[None for x in range(a)]for y in range(b)]for z in range(c)]

for x in range(a):
	for y in range(b):
		for z in range(c):
			voxel = Voxel(position = ((x*d) ,(y*d), (z*d)) , scale = (s,s,s))
			v[x][y][z] = voxel





def update():
	for i in range(a):
		for j in range(b):
			for k in range(c):
				random.seed(i+ j + k)
				v[i][j][k].x += (random.random()-0.5)*2*(I/6)
				v[i][j][k].y += (random.random()-0.5)*2*(I/6)
				v[i][j][k].z += (random.random()-0.5)*2*(I/6)
				x1 = v[i][j][k].position
				
				for l in range(a):
					for m in range(b):
						for n in range(c):
							if v[i][j][k] != v[l][m][n]:
								if ((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 > s:
									if v[i][j][k].x< v[l][m][n].x:
										v[i][j][k].x += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
									else:
										v[i][j][k].x -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
									if v[i][j][k].y < v[l][m][n].y:
										v[i][j][k].y += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
									else:
										v[i][j][k].y -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
									if v[i][j][k].z <v[l][m][n].z :
										v[i][j][k].z += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
									else:
										v[i][j][k].z -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*g))**p
								else:
									if v[i][j][k].x< v[l][m][n].x:
										v[i][j][k].x -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
									else:
										v[i][j][k].x += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
									if  v[i][j][k].y < v[l][m][n].y:
										v[i][j][k].y -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
									else:
										v[i][j][k].y += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
									if v[i][j][k].z < v[l][m][n].z:
										v[i][j][k].z -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
									else:
										v[i][j][k].z += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +G)*r))**p2
			
				x2 = v[i][j][k].position
				v[i][j][k].position += (x2 - x1)
				
					
pivot = Entity()			
		
PointLight(parent=pivot, x = 1000, y = 1000, z = 1000)	
		
camera.ortographic = True			

EditorCamera()				
 
app.run()

