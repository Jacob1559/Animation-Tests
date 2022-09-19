from ursina.mesh import Mesh

from ursina import *

import random

 

from ursina.shaders import lit_with_shadows_shader

import math

import numpy as np

app = Ursina()

def update():
	camera_control()
	
	



class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1),color = color.white):
		super().__init__(
		parent = scene,
		position = position,
		color = color,
		collision = False,
		scale = scale,
		model= 'cube',
		texture = 'white_cube',
		origin_y = 0,
		origin_z = -40
	
		
		)	
		
	def update(self):
		if self.x >0 :
			self.x +=   (math.cos(self.y/(abs(self.z**(0.5)) + 1))**(2))*time.dt*5
		else:
			self.x -=   (math.cos(self.y/(abs(self.z**(0.5)) + 1))**(2))*time.dt*6
		
		if self.z >0 :
			self.z +=   (math.cos(self.x/(abs(self.y**(0.5)) + 1))**(2))*time.dt*7
		else:
			self.z -=   (math.cos(self.x/(abs(self.y**(0.5)) + 1))**(2))*time.dt*8
		
		
		if self.y > 0:
			self.y +=   (math.cos(self.x/(abs(self.z**(0.5)) + 1))**(1))*time.dt*9  
		else:
			self.y -=   (math.cos(self.x/(abs(self.z**(0.5)) + 1))**(1))*time.dt*10 
		
			
		
		
		
		
		
		
for z in range(-16,17):
	for x in range(-16,17):
		for y in range(-16,17):
			if abs((y**2 - x**2 - z**2)**0.5)//1 + 1 == 8:
				voxel = Voxel(position = (x , y, z), color = rgb(abs(x)*100,abs(y)*100, abs(z)*100 ))
				

				
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
		
PointLight(parent=pivot, x = 1000, y = 1000, z = 1000)



	
camera.ortographic = True			

EditorCamera()				
 
app.run()
