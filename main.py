from point_cloud_viewer import PointCloudViewer

def main():
    viewer = PointCloudViewer()
    
    try:
        cloud = viewer.load_cloud("point_cloud(1).ply")
        
        info = viewer.get_cloud_info(cloud)
        print(f"\nPoint Cloud Info:")
        print(f"Number of points: {info['num_points']}")
        print(f"Has normals: {info['has_normals']}")
        print(f"Has colors: {info['has_colors']}")
        
        processed_cloud = viewer.process_cloud(
            cloud,
            voxel_size=None  
        )
        
        print("\nVisualizing point cloud...")
        print("Controls:")
        print("- Click and drag to rotate")
        print("- Right click and drag to zoom")
        print("- Middle click and drag to pan")
        
        viewer.visualize(
            processed_cloud,
            colors=['cyan'],  
            point_size=0.0001,        
            alpha=1.0,             
            show_axes=True         
        )
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()