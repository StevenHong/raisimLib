import numpy as np

x_points = 30
y_points = 30

range = [0, 0.4]

vals = np.random.random(x_points*y_points)*(range[1]-range[0])+range[0]

vals = vals.reshape((x_points, y_points))
vals[x_points//2-1:x_points//2+2,y_points//2-1:y_points//2+2] = 0
vals = vals.flatten()

print(vals)
