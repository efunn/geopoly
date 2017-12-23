# how to unlock luigi: clear the first part of mushroom kingdom with a 2 in the seconds place 

from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.geometry import MultiPoint
import numpy as np
from draw_poly import plot_poly, plot_heatmap

coords_filename = 'coordinates/texas.txt'

# coords is a list of (x, y) tuples
# poly = Polygon(((0, 0), (0, 1), (1, 1), (1, 0)))

coords = np.loadtxt(coords_filename)

lat_search = [min(coords[:,0]),max(coords[:,0])]
long_search = [min(coords[:,1]),max(coords[:,1])]
grid_size = 0.5 # in degrees
lat_search_range = np.arange(lat_search[0],lat_search[1],grid_size)
long_search_range = np.arange(long_search[0],long_search[1],grid_size)

# # if you need to meshgrid
# lat_grid, long_grid = np.meshgrid(lat_search_range,long_search_range)

# # only works with ordered points (probably some way to do unordered)
# poly = MultiPoint(coords).convex_hull
poly = Polygon(coords)

# # this shows you the xy coordinates of the polygon
# print poly.exterior.coords.xy

# # if you want to just plot the polygon
# plot_poly(poly)

in_grid_array = np.zeros((np.size(lat_search_range),np.size(long_search_range)))
for lat_index, lat_coord in enumerate(lat_search_range):
    for long_index, long_coord in enumerate(long_search_range):
        in_grid_array[lat_index,long_index] = poly.contains(Point((lat_coord,long_coord)))

# plotting the in grid coordinates
plot_heatmap(in_grid_array)
