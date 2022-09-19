from panda3d.core import CollisionNode, CollisionBox, CollisionSphere, CollisionPolygon

from panda3d.core import NodePath

from ursina.vec3 import Vec3

from ursina.mesh import Mesh

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
		collision = False,
		scale = scale,
		model = 'cube',
		texture = 'white_cube',
		origin_y = 0
	
		
		)	
	def update(self):
		self.rotation += (self.x/100, self.y/100, self.z/100)
		self.color =rgb( 255*math.cos(time.time()*(2**(0.5))+ self.x/100),
						
						255*math.cos(time.time()*(3**(0.5))+ self.y/100),
						 
						255*math.cos(time.time()*(5**(0.5) + self.z)))
		
		
		
		
		

for x in range(-8,9):
	for y in range(-8,9):
		for z in range(-8,9):
			voxel = Voxel(scale = (x**2, y**2, z**2), position = (x**3, y**3, z**3))
				
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

Sky(color = color.black)	
		
camera.ortographic = True			

EditorCamera()				
 

app.run()
