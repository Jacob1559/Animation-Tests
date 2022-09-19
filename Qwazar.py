from panda3d.core import CollisionNode, CollisionBox, CollisionSphere, CollisionPolygon

from panda3d.core import NodePath

from ursina.vec3 import Vec3

from ursina.mesh import Mesh

from ursina import *
 

from ursina.shaders import lit_with_shadows_shader

import math

app = Ursina()

	

	

class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		scale = scale,
		position = position,
		color = color.white,
		model = 'cube',
		texture = 'white_cube',
		
	
		
		)	
	
		
		
		
		

v = [[[None for x in range(-4,5)]for y in range(-4,5)]for z in range(-4,5)]

			
		
for z in range(-4,5):
	for x in range(-4,5):
		for y in range(-4,5):
			voxel = Voxel(position = (x,y, z), scale = (1, 1,1))
			v[x][y][z] = voxel



			
			
class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		scale = scale,
		position = position,
		color = color.white,
		model = 'cube',
		texture = 'white_cube',
		
	
		
		)	
	def update(self):
		i = -4
		j = -4	
		k = -4		
		while k < 5:
			while j < 5:
				while i < 5:
					self.position += (math.sin(v[i][j][k].x*self.y)/60, math.sin(v[i][j][k].y*self.z)/60 ,math.sin(v[i][j][k].z*self.x)/60)
					i = i + 1
				j = j + 1
			k = k + 1
for z in range(-9,9):
	for x in range(-9,9):
		for y in range(-9,9):
			if ((x**2 + y**2 + z**2)**0.5)//1 == 8:
				voxel = Voxel(position = (x,y, z), scale = (1, 1,1))
	
				
	
pivot = Entity()			
		
	
PointLight(parent=pivot, x = 100, y = 100, z = 100)	
		
			
camera.ortographic = True			

EditorCamera()				
 

app.run()
