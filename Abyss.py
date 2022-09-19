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
		model = 'sphere',
		texture = 'circle',
		origin_y = 0
	
		
		)	
	
	def update(self):
		if (self.x)%2 == 0:
			self.x -= math.sin(self.z/60)
		else:
			self.x += math.cos(self.z/60)
		if (self.y)%2 == 0:
			self.y -= math.sin(self.x/60)
		else:
			self.y += math.cos(self.x/60)
		if (self.z)%2  == 0:
			self.z -= math.sin(self.y/60)
		else:
			self.z += math.sin(self.y/60)
			
		self.color =rgb( 255*math.cos(time.time()*(2**(0.5))+ self.x/100),
						
						255*math.cos(time.time()*(3**(0.5))+ self.y/100),
						 
						255*math.cos(time.time()*(5**(0.5) + self.z/100)))
		

for z in range(-9,9):
	for x in range(-9,9):
		for y in range(-9,9):
			if ((x**2 + y**2 + z**2)**0.5)//1 == 8:
				voxel = Voxel(position = (x,y, z))
			
			
def camera_control():
	camera.z += held_keys['e']*10*time.dt
	camera.z -= held_keys['c']*10*time.dt
	camera.z += held_keys['r']*10
	camera.z -= held_keys['v']*10
	camera.y += held_keys['w']*10*time.dt
	camera.y -= held_keys['s']*10*time.dt
	camera.x += held_keys['a']*10*time.dt
	camera.x -= held_keys['d']*10*time.dt

Sky(color = color.black)			
pivot = Entity()			
		
PointLight(parent=pivot, x = 1000, y = 1000, z = 1000)	
		
camera.ortographic = True			

EditorCamera()				

app.run()
