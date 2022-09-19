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
		position = position,
		color = color.white,
		scale = scale,
		model= 'sphere',
		texture ='reflection_map_3'
,
		origin_y = 0
	
		
		)	
	def update(self):
		if (self.x)%5 == 0:
			self.x *= math.cos(self.z/30)/2
		else:
			self.x += math.sin(self.z/30)/2
		if (self.y)%5 == 0:
			self.y *= math.cos(self.x/30)/2
		else:
			self.y += math.sin(self.x/30)/2
		if (self.z)%5  == 0:
			self.z *= math.cos(self.y/30)/2
		else:
			self.z += math.sin(self.y/30)/2
		
		self.color = rgb(255*abs(math.sin(self.x/10)),
						 255*abs(math.sin(self.y/10)), 
						 255*abs(math.sin(self.z/10)))
		
		self.scale = ( abs(self.x/20)**2, 
		               abs(self.y/20)**2, 
		               abs(self.z/20)**2)
			
			
		
		
for x in range(-16,17):
	for y in range(-16,17):
		for z in range(-16,17):
			if (x**2 + y**2 + z**2)**0.5//1 + 1 == 8:
				voxel = Voxel(position = (x , y, z))
			
			
			

				


pivot = Entity()			
		
PointLight(parent=pivot, x = 1000, y = 1000, z = 1000)





	
camera.ortographic = True			

EditorCamera()				
 
app.run()
