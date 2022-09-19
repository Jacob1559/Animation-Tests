from ursina import *
 
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import lit_with_shadows_shader

import math

import numpy as np

app = Ursina()


class Voxel(Button):
	def __init__(self, position = (0,0,0), scale = (1,1,1)):
		super().__init__(

		parent = scene,
		position = position,
		color = color.white,
		model = 'cube',
		scale = scale,
		texture = 'white_cube',
		origin_y = 1,
		origin_x = 1,
		origin_z = 1
		
		)	

for z in range(-9,8):
	for x in range(-9,8):
		for y in range(-9,8):
			if y < 0:
				voxel = Voxel(position = (x,y, z))
			else:
				voxel = Voxel(scale = (abs(x), abs(y), abs(z)), position = (x**3,y**3, z**3))
				
			
				
				
			
pivot = Entity()			
		
PointLight(parent=pivot, x = 0, y = 0, z = 0)	
		
player = FirstPersonController()		
 
app.run()
