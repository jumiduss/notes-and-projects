import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0,3.0, 0.01)

# ax1 = plt.subplot(212)
# ax1.margins(0.05)
# ax1.plot(t1, f(t1))

# ax2 = plt.subplot(221)
# ax2.margins(2, 2)
# ax2.plot(t1, f(t1))
# ax2.set_title("Zoomed Out")

# ax3 = plt.subplot(222)
# ax3.margins(x=0,y=-0.25)
# ax3.plot(t1, f(t1))
# ax3.set_title('Zommed In')

# plt.show()


y, x = np.mgrid[:5, 1:6]
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]
fig, (ax1, ax2) = plt.subplots(ncols=2)

# Here we set the stickiness of the axes object...
# ax1 we'll leave as the default, which uses sticky edges
# and we'll turn off stickiness for ax2
ax2.use_sticky_edges = False

for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno')  # sticky
    ax.add_patch(
        plt.Polygon(poly_coords, color='forestgreen', alpha=0.5)
    )  # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title('{} Sticky'.format(status))

plt.show()

# fig = go.Figure()
# fig.add_trace(go.Scatter(
#     x=[0.3, 0.6],y=[0,0], mode='markers', marker_size=20
# ))
# fig.update_xaxes(showgrid=False)
# fig.update_yaxes(showgrid=False,zeroline=True,zerolinecolor='black',zerolinewidth=3,showticklabels=False)
# fig.update_layout(height=200, plot_bgcolor='white')
# fig.show()