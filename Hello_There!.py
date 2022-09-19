from ursina import *
 
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import lit_with_shadows_shader

import math

import numpy as np

app = Ursina()

def update():
	camera_control()
			

		
class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		position = position,
		color = color.white,
		scale = scale,
		collision = True,
		model = 'cube',
		texture = 'white_cube',
		origin_y = 0
	
		
		)	
	def update(self):
		self.rotation += (self.x,self.y,self.z)
		self.x += self.x*math.sin(time.time())
		self.y += self.y*math.sin(time.time())
		self.z += self.z*math.sin(time.time())
		
		
for z in range(-17,16):
	for x in range(-17,16):
		for y in range(-17,16):
			if abs((y**2 -x**2 - z**2)**0.5)//1 + 1 == 8:
				voxel = Voxel(position = (x , y, z))
				
def camera_control():
	camera.z += held_keys['e']*10*time.dt
	camera.z -= held_keys['c']*10*time.dt
	camera.z += held_keys['r']*10
	camera.z -= held_keys['v']*10
	camera.y += held_keys['w']*10*time.dt
	camera.y -= held_keys['s']*10*time.dt
	camera.x += held_keys['a']*10*time.dt
	camera.x -= held_keys['d']*10*time.dt
			
			
pivot = Entity()			
		
PointLight(parent=pivot, x = 100, y = 100, z = 100)	
		
camera.ortographic = True			

EditorCamera()				
 

app.run()
