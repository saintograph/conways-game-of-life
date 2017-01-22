import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
	return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)
	
def addGlider(i, j, grid):
	glider = np.array([[0  ,   0, 255],
					   [255,   0, 255],
					   [0  , 255, 255]])
	grid[]
