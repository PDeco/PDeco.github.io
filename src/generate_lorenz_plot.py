"""
File purpose:
    Generating static html to visualize the lorenz plot on web server.
"""

import numpy as np
import dynamicsystem
import plotly.graph_objs as go
import plotly.offline as pyo

# The existing Lorenz system simulation code
x0 = np.array([[1, 1, 1]]).T
system = dynamicsystem.Lorenz(x0)
eval_time = 100
eval_timestamps = np.linspace(0, eval_time, 100000)
states, timestamps = system.propagate(eval_time, eval_timestamps=eval_timestamps)

# Extract x, y, z coordinates
x_data = states[0]
y_data = states[1]
z_data = states[2]

# Create a Plotly trace
trace = go.Scatter3d(
    x=x_data,
    y=y_data,
    z=z_data,
    mode="lines",
    line=dict(width=2, color="rgb(255, 0, 0)"),
)

# Create a Plotly layout
layout = go.Layout(
    title="Lorenz System Attractor",
    scene=dict(xaxis=dict(title="X"), yaxis=dict(title="Y"), zaxis=dict(title="Z")),
)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Generate the full HTML for the plot and save it to a file
# The `full_html=True` and `include_plotlyjs=True` arguments
# are key here. This generates a standalone HTML file with all
# the necessary JavaScript included.
pyo.plot(
    fig, filename="_includes/lorenz_plot.html", auto_open=False, include_plotlyjs=True
)

print("Plotly HTML file generated and saved to _includes/lorenz_plot.html")
