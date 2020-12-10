#!/usr/bin/env python

import sys
import os

class Model:
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name')
        self.filepath = kwargs.pop('filepath')

    def __str__(self):
        return '[Model]: <{}>'.format(self.name + '\n          '+ self.filepath)

    def sys_lfs_call(self):
        return "cd onnx_models && git lfs pull --include=" + str(self.filepath) + " --exclude="""

    def download(self):
        print('[Info]: Download model: ' + self.name)
        return os.system(self.sys_lfs_call())

def create_basedir(basedir):
    curdir = os.getcwd()
    if curdir and not os.path.exists(curdir + "/" + basedir):
        print('[Info]: Cloning onnx_models repository from https://github.com/onnx/models.git')
        os.system("git clone --recursive https://github.com/onnx/models.git " + basedir)
    else:
        print('[Warning]: Current directory already contains a "onnx_models" folder, clone is skipped')

models = [
    Model(
        name='ssd-mobilenet-v1-10',
        filepath='vision/object_detection_segmentation/ssd-mobilenetv1/model/ssd_mobilenet_v1_10.onnx',
    ),
    Model(
        name='squeezenet1.0-9',
        filepath='vision/classification/squeezenet/model/squeezenet1.0-9.onnx',
    ),
    Model(
        name='emotion-ferplus-8',
        filepath='vision/body_analysis/emotion_ferplus/model/emotion-ferplus-8.onnx',
    ),
    Model(
        name='FasterRCNN-10',
        filepath='vision/object_detection_segmentation/faster-rcnn/model/FasterRCNN-10.onnx',
    ),
    Model(
        name='yolov3-10',
        filepath='vision/object_detection_segmentation/yolov3/model/yolov3-10.onnx',
    ),
    Model(
        name='tinyyolov2-8',
        filepath='vision/object_detection_segmentation/tiny-yolov2/model/tinyyolov2-8.onnx',
    ),
]
if __name__ == '__main__':
    selected_model_name = None
    print_all_models = False
    if len(sys.argv) > 1:
        selected_model_name = sys.argv[1]
        if (selected_model_name != "print"):
            print('Model: ' + selected_model_name)
        else:
            print_all_models = True

    create_basedir('onnx_models')

    for m in models:
        if (not print_all_models):
            if selected_model_name is not None and not m.name.startswith(selected_model_name):
                continue
            m.download()
        else:
            print(m)
print('[Info]: Done')