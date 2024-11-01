# Point Cloud Viewer

A simple Python tool for visualizing 3D point clouds using Open3D and Matplotlib.

## Features
- Load and view PLY point cloud files

## Usage
```python
from point_cloud_viewer import PointCloudViewer

viewer = PointCloudViewer()
cloud = viewer.load_cloud("your_cloud.ply")
viewer.visualize(cloud)
```

