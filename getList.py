import os
import pathlib
import xml.etree.ElementTree as ET

coco_labels = list(map(lambda x: x.strip(), open('./labels_coco.txt').readlines()))
coco_labels.insert(0, 'BACKGROUND')
mapping = {
            "airplane":            'aeroplane',
            "dining table":        'diningtable',
            "motorcycle":          'motorbike',
            "potted plant":        'pottedplant',
            "couch":               'sofa',
            "tv":                  'tvmonitor',
        }

def getFileList(p,output):
    fileList = os.listdir(p)
    dir_output_path = '/'.join(output.split('/')[:-1])
    pathlib.Path(dir_output_path).mkdir(parents=True, exist_ok=True)

    text_output = openFile(output)
    for f in fileList:
        f = f.split('.')[0]
        text_output.write(f'{f}\n')

def openFile(p, mode='w'):
    dir_output_path = '/'.join(p.split('/')[:-1])
    pathlib.Path(dir_output_path).mkdir(parents=True, exist_ok=True)
    return open(p, mode)

def clean_dataset(annos_path, outputs):
    f = openFile(outputs)
    annos = os.listdir(annos_path)
    for anno in annos:
        objs = ET.parse(os.path.join(annos_path, anno)).findall('object')
        for obj in objs:
            name = obj.find('name').text.lower().strip()
            if coco_labels[int(name)] in mapping:
                f.write(f"{anno.split('.')[0]}\n")

if __name__ == "__main__":
    clean_dataset('./Annotations', './ImageSets/Main/trainval.txt')
