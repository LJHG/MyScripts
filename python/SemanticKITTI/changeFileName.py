import os
import argparse


'''
这个脚本用于修改一个文件夹下的所有文件的名字，专用于KITTI数据集
例如对于001500.bin ~ 001520.bin文件，通过对所有文件的数字mod1500，来将其修改为000000.bin ~ 000020.bin
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser("./changefilename.py")
    parser.add_argument(
        '--directory', '-d',
        type=str,
        required=True,
        help='the folder that contains files you need to modify',
    )
    parser.add_argument(
        '--number', '-n',
        type=int,
        required=True,
        help='the number you want to mod'
    )
    FLAGS, unparsed = parser.parse_known_args()

    cwd = os.getcwd()
    fileList=os.listdir(cwd +'/'+FLAGS.directory)
    for i in fileList:
        fileName,type = i.split('.')
        newFileName = '%06d'%(int(fileName)%FLAGS.number)
        type = '.' + type
        os.rename(os.path.join(cwd +'/'+FLAGS.directory,fileName+type),os.path.join(cwd +'/'+FLAGS.directory,newFileName+type))

