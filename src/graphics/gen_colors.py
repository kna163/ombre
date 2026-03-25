import random
import numpy as np
import matplotlib.pyplot as plt
import sys
import pathlib

if len(sys.argv) != 2:
    raise SyntaxError("Please provide path for where to save the colors.")
base_path = pathlib.Path(sys.argv[1])
if not (base_path / "gen_colors.py").is_file():
    raise SyntaxError("Check to make sure path leads to gen_colors.py.")

random.seed(32)
N = 20 # makes N^2 colors

def rand_color():
    a = random.random()-.5
    b = random.random()-.5
    c = -a-b
    x = max(np.abs([a,b,c]))-min(np.abs([a,b,c]))
    if x < .2:
        a,b,c = 2*a/x,2*b/x,2*c/x
    r = random.random()
    a,b,c = np.exp([a,b,c])
    d = max(a,b,c,1)
    a,b,c = a/d,b/d,c/d
    if r < 1/3:
        a,c = c,a
    elif r < 2/3:
        b,c = c,b
    return [a,b,c]

color_square = np.array([[rand_color() for _ in range(N)] for _ in range(N)], dtype=np.float32)
plt.imsave(base_path / "colors.png",color_square)

colors = np.reshape(color_square,(N*N,3))
np.save(base_path / 'colors.npy', colors)