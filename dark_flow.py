

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
		model = 'sphere',
		texture = 'white_cube',
		scale = scale,
		origin_y = 0
	
		
		)
		
	def update(self):
		
		self.color =rgb(255*math.cos(time.time()*(2**(0.5))+ self.x/100),
						
						255*math.cos(time.time()*(3**(0.5))+ self.y/100),
						 
						255*math.cos(time.time()*(5**(0.5) + self.z/100)))
	
	
v = [[[None for x in range(-1,2)]for y in range(-1,2)]for z in range(-1,2)]

for x in range(-1,2):
	for y in range(-1,2):
		for z in range(-1,2):
			voxel = Voxel(position = ((x*5) ,(y*10), (z*10)) , scale = (1,1,1))
			v[x][y][z] = voxel




def update():
	t1 = time.time()
	x1 = v[x][y][z].position
	for i in range(-1,2):
		for j in range(-1,2):
			for k in range(-1,2):
				v[i][j][k].position += (1/600*v[i][j][k].y,1/600*v[i][j][k].z,1/600*v[i][j][k].x)
				x1 = v[i][j][k].position
				for l in range(-1,2):
					for m in range(-1,2):
						for n in range(-1,2):
							if v[i][j][k] != v[l][m][n]:
								if ((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 > 1:
									if v[i][j][k].x< v[l][m][n].x:
										v[i][j][k].x += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
									else:
										v[i][j][k].x -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
									if v[i][j][k].y < v[l][m][n].y:
										v[i][j][k].y += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
									else:
										v[i][j][k].y -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
									if v[i][j][k].z <v[l][m][n].z :
										v[i][j][k].z += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
									else:
										v[i][j][k].z -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*1))**3
								else:
									if v[i][j][k].x< v[l][m][n].x:
										v[i][j][k].x -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
									else:
										v[i][j][k].x += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
									if  v[i][j][k].y < v[l][m][n].y:
										v[i][j][k].y -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
									else:
										v[i][j][k].y += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
									if v[i][j][k].z < v[l][m][n].z:
										v[i][j][k].z -= (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
									else:
										v[i][j][k].z += (1/((((v[i][j][k].x - v[l][m][n].x)**2 + (v[i][j][k].y - v[l][m][n].y)**2 + (v[i][j][k].z - v[l][m][n].z)**2)**0.5 +10)*0.5))**3
					x2 = v[i][j][k].position
					v[i][j][k].position += (x2 - x1)
					
		
		
	

				
pivot = Entity()			
		
PointLight(parent=pivot, x = 100, y = 100, z = 100)	
		
camera.ortographic = True			

EditorCamera()				
 
app.run()
