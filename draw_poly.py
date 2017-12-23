from matplotlib import pyplot
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch

COLOR = {
    True:  '#6699cc',
    False: '#ff3333'
    }

def v_color(ob):
    return COLOR[ob.is_valid]

def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)

def plot_poly(poly):
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    plot_coords(ax, poly.exterior)
    patch = PolygonPatch(poly, facecolor=v_color(poly), edgecolor=v_color(poly), alpha=0.5, zorder=2)
    ax.add_patch(patch)
    pyplot.show()

def plot_heatmap(heatmap):
    pyplot.imshow(heatmap)
    pyplot.show()
