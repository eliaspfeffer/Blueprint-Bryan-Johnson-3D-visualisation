import plotly.graph_objs as go
import numpy as np
import trimesh

# Load a simple 3D human body mesh
# You can use a simplified model or download an STL file for a human body
# For the sake of this example, let's create a simple mesh manually
body_mesh = trimesh.creation.icosphere(subdivisions=4, radius=1)

# Extract vertices and faces from the mesh
vertices = body_mesh.vertices
faces = body_mesh.faces

# Define organ positions and ages
organs = {
    "heart": {"position": [0.0, 0.5, 0.3], "age": 28},
    "brain": {"position": [0.0, 0.8, 0.0], "age": 45},
    "prostate": {"position": [0.0, -0.3, 0.0], "age": 30},
    "kidney_left": {"position": [-0.2, 0.4, 0.1], "age": 21},
    "kidney_right": {"position": [0.2, 0.4, 0.1], "age": 21},
    "liver": {"position": [0.1, 0.4, -0.1], "age": 33}
}

# age of organs as a list


# Function to map age to color
def age_to_color(age):
    if age <= 20:
        return "lightgreen"
    elif age <= 30:
        return "green"
    elif age <= 40:
        return "yellow"
    elif age <= 50:
        return "orange"
    else:
        return "red"

# Create the mesh figure for the human body
body_fig = go.Mesh3d(
    x=vertices[:, 0],
    y=vertices[:, 1],
    z=vertices[:, 2],
    i=faces[:, 0],
    j=faces[:, 1],
    k=faces[:, 2],
    color='lightblue',
    opacity=0.5,
    name='Body'
)

# Create scatter plots for organs
organ_markers = []
for organ, data in organs.items():
    organ_markers.append(
        go.Scatter3d(
            x=[data["position"][0]],
            y=[data["position"][1]],
            z=[data["position"][2]],
            mode='markers',
            marker=dict(
                size=5,
                color=age_to_color(data["age"]),
                opacity=0.8
            ),
            name=f'{organ} (age: {data["age"]})'
        )
    )

# Combine body mesh and organ markers into one figure
fig = go.Figure(data=[body_fig] + organ_markers)

# Update layout
fig.update_layout(
    title="Bryan Johnson's Organ Age Visualization",
    scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis'),
    )
)

fig.show()
