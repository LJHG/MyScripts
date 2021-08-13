import numpy as np
import open3d as o3d
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser("./bin2ply.py")
    parser.add_argument(
        '--root', '-r',
        type=str,
        required=True,
        help='the folder that contains the dataset',
    )
    parser.add_argument(
        '--length', '-l',
        type=int,
        required=True,
        help='the folder of bin file len you wanna convert',
    )

    FLAGS, unparsed = parser.parse_known_args()
    root = FLAGS.root + '/'
    for drive_id in range(FLAGS.length):
        path = root + '%06d.bin' % drive_id
        xyzr = np.fromfile(path, dtype=np.float32).reshape(-1, 4)
        # print(len(xyzr))
        xyz0 = xyzr[:, :3]
        src_keypts = o3d.geometry.PointCloud()
        src_keypts.points = o3d.utility.Vector3dVector(xyz0)
        print(src_keypts)
        o3d.io.write_point_cloud(root + '%06d.ply' % drive_id,src_keypts)
