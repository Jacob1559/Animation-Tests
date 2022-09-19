from ursina import *
 
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import lit_with_shadows_shader

import math



app = Ursina()

def update():
	camera_control()
			
class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		position = position,
		color = color.white,
		model = 'cube',
		texture = 'white_cube',
		origin_y = 0
	
		
		)	
	
	def update(self):
		if (self.x)%20 == 0:
			self.x -= math.sin(self.z/60)
		else:
			self.x += math.cos(self.z/60)
		if (self.y)%20 == 0:
			self.y -= math.sin(self.x/60)
		else:
			self.y += math.cos(self.x/60)
		if (self.z)%20  == 0:
			self.z -= math.sin(self.y/60)
		else:
			self.z += math.sin(self.y/60)
			
		self.scale = (abs(self.x)*(math.sin(self.x/100)+ 1.1), abs(self.y)*(math.sin(self.y/100) + 1.1), abs(self.z)*(math.sin(self.z/100)+ 1.1))
		

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
			
pivot = Entity()			
		
PointLight(parent=pivot, x = 1000, y = 1000, z = 1000)	
		
camera.ortographic = True			

EditorCamera()				

app.run()
