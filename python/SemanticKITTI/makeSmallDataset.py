import os
import argparse
import shutil


'''
这个脚本用于将KITTI数据集08序列的4071帧拆分为21帧的多个序列，并构建小数据集，间隔为10帧  0~20 10~30.....4050~4070
-d dataset
-s smalldataset
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser("./changefilename.py")
    parser.add_argument(
        '--dataset', '-d',
        type=str,
        required=True,
        help='the folder that contains the full dataset',
    )
    parser.add_argument(
        '--smalldataset', '-s',
        type=str,
        required=True,
        help='the folder that output the small dataset'
    )
    FLAGS, unparsed = parser.parse_known_args()

    cwd = os.getcwd()
    dirTo08 = cwd +'/'+FLAGS.dataset + '/sequences/08'
    velodynePath = dirTo08 + '/velodyne'
    labelsPath = dirTo08 + '/labels'
    
    
    for i in range(406):
        # 创建文件夹
        # os.mkdir(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20))
        # os.mkdir(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences')
        # os.mkdir(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/08')
        # os.mkdir(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/01')
        # os.mkdir(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/02')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/08/velodyne')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/01/velodyne')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/02/velodyne')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/08/labels')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/01/labels')
        os.makedirs(cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/02/labels')
        toBeMinus = i*10
        for j in range(21):
            index = i*10 + j
            # 待复制文件地址
            oldBin = velodynePath + '/' + '%06d'%index + '.bin'
            oldLabel = labelsPath + '/' + '%06d'%index + '.label'
            # 复制到新的08 squence的地址(顺便改名)
            newBin = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/08/velodyne/' + '%06d'%(index-toBeMinus) + '.bin'
            newLabel = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/08/labels/' + '%06d'%(index-toBeMinus) + '.label'
            shutil.copy(oldBin,newBin)
            shutil.copy(oldLabel,newLabel)

            # 敷衍一下01和02
            if(j == 0):
                newBin = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/01/velodyne/' + '%06d'%(index-toBeMinus) + '.bin'
                newLabel = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/01/labels/' + '%06d'%(index-toBeMinus) + '.label'
                shutil.copy(oldBin,newBin)
                shutil.copy(oldLabel,newLabel)
                newBin = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/02/velodyne/' + '%06d'%(index-toBeMinus) + '.bin'
                newLabel = cwd + '/' + FLAGS.smalldataset + '/smalldataset{}-{}'.format(i*10,i*10+20) + '/sequences/02/labels/' + '%06d'%(index-toBeMinus) + '.label'
                shutil.copy(oldBin,newBin)
                shutil.copy(oldLabel,newLabel)
