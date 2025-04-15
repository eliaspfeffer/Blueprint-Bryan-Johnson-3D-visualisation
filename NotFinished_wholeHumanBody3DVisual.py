import plotly.graph_objs as go
import trimesh
import os

# Define the path to the STL file
file_path = 'human_body.stl'

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist. Please check the file path.")

# Load the human body STL file
mesh = trimesh.load_mesh(file_path)

# Extract vertices and faces from the mesh
vertices = mesh.vertices
faces = mesh.faces

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


# Combine body mesh into one figure
fig = go.Figure(data=[body_fig])

# Update layout
fig.update_layout(
    title="3D Human Body Model",
    scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis'),
    )
)

fig.show()
