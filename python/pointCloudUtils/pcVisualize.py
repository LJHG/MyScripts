import open3d as o3d
import numpy as np
from open3d import *
import argparse

'''
点云可视化脚本
用法: python pcVisualize.py -f <filename>
'''

# 对ply格式的pc做可视化
def vispc_ply(filename):
    pc = o3d.io.read_point_cloud(filename)
    o3d.visualization.draw_geometries([pc])

# 对npy格式的pc做可视化
def vispc_npy(filename):
    xyz = np.load(filename).astype(np.float32)
    if(len(xyz[0]) == 6):
        # 去掉rgb
        xyz = xyz[:,:3]
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(xyz)
    o3d.visualization.draw_geometries([pc])


if __name__ == '__main__':
    parser = argparse.ArgumentParser("./pcVisualize.py")
    parser.add_argument(
        '--filename', '-f',
        type=str,
        required=True,
        help='point cloud file',
    )
    parser.add_argument(
        '--type', '-t',
        type=int,
        required=False,
        help='specify the file type, ply, npy, pcd...'
    )
    FLAGS, unparsed = parser.parse_known_args()

    
    filename = FLAGS.filename
    if(filename.split(".")[-1] == "ply"):
       vispc_ply(filename)
    elif(filename.split(".")[-1] == "npy"):
        vispc_npy(filename)
    else:
        print("unsupported file type")       

    # vispc_ply("./data/testdata/8iVFB/longdress_vox10_1300.ply")
    # vispc_ply("./data/scannet_ply/train/scene0000_00.ply")