from ursina import *
 
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import lit_with_shadows_shader
from ursina import *
 
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import lit_with_shadows_shader

import math

app = Ursina()



		
class Voxel(Entity):
	def __init__(self, position = (1,0,0), scale = (1,1,1)):
		super().__init__(
		parent = scene,
		position = position,
		color = color.white,
		model = 'cube',
		texture = 'white_cube',
		
	
		
		)	
	def update(self):
		
		self.rotation += (1,1,1)
		
		
		self.scale = 	( -1.1+ math.cos(time.time()*self.x), 
		
						 -1.1 + math.sin(time.time()*self.y), 
		
						 -1.1 + math.cos(time.time()*self.z))
						
		self.color +=color.color(math.sin(time.time()*self.x), 
								
								math.sin(time.time()*self.y),
								
								math.sin(time.time()*self.z))
		
		
for x in range(-16,17):
	for y in range(-16,17):
		for z in range(-16,17):
			if (x**2 + y**2 + z**2)**0.5//1 + 1 == 8:
				voxel = Voxel(position = (x , y, z))
			
			
			

	
				


						
			
		
pivot = Entity()			
		
	
PointLight(parent=pivot, x = 100, y = 100, z = 100)	
		
			
camera.ortographic = True			

EditorCamera()				
 

app.run()
