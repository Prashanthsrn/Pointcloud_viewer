import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Union

class PointCloudViewer:
    def load_cloud(self, file_path: str) -> o3d.geometry.PointCloud:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} not found")
            
        if file_path.suffix == '.ply':
            return o3d.io.read_point_cloud(str(file_path))
        elif file_path.suffix == '.pcd':
            return o3d.io.read_point_cloud(str(file_path))
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

    def process_cloud(self, point_cloud: o3d.geometry.PointCloud, voxel_size: float = None) -> o3d.geometry.PointCloud:
        processed = point_cloud
        
        if voxel_size is not None:
            processed = processed.voxel_down_sample(voxel_size=voxel_size)
        
        processed.estimate_normals()
        return processed

    def visualize(self, clouds: Union[o3d.geometry.PointCloud, List[o3d.geometry.PointCloud]], colors: List[str] = None,point_size: float = 0.5,alpha: float = 1.0, show_axes: bool = True):
        if not isinstance(clouds, list):
            clouds = [clouds]
            
        if colors is None:
            colors = ['royalblue' for _ in clouds]
        
        plt.style.use('dark_background')
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        for cloud, color in zip(clouds, colors):
            points = np.asarray(cloud.points)
            
            center = points.mean(axis=0)
            max_dist = np.max(np.linalg.norm(points - center, axis=1))
            
            scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2],
                               c=color,
                               s=point_size,
                               alpha=alpha,
                               marker='.')
            
            ax.set_xlim(center[0] - max_dist, center[0] + max_dist)
            ax.set_ylim(center[1] - max_dist, center[1] + max_dist)
            ax.set_zlim(center[2] - max_dist, center[2] + max_dist)
        
        if show_axes:
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
        else:
            ax.set_axis_off()
        
        ax.set_box_aspect([1, 1, 1])
        
        ax.view_init(elev=30, azim=45)
        
        ax.grid(False)
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        
        plt.show()

    def get_cloud_info(self, cloud: o3d.geometry.PointCloud) -> dict:
        points = np.asarray(cloud.points)
        return {
            'num_points': len(points),
            'bounds': {
                'min': points.min(axis=0),
                'max': points.max(axis=0)
            },
            'center': points.mean(axis=0),
            'has_normals': cloud.has_normals(),
            'has_colors': cloud.has_colors()
        }