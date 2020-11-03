import os
import pathlib
import xml.etree.ElementTree as ET

def openFile(p, mode='w'):
    dir_output_path = '/'.join(p.split('/')[:-1])
    pathlib.Path(dir_output_path).mkdir(parents=True, exist_ok=True)
    return open(p, mode)

def clean_dataset(annos_path, outputs):
    f = openFile(outputs)
    annos = os.listdir(annos_path)
    for anno in annos:
        f.write(f"{anno.split('.')[0]}\n")

if __name__ == "__main__":
    clean_dataset('/mnt/datasets/PascalFormCOCO2017/Annotations/', '/mnt/datasets/PascalFormCOCO2017/ImageSets/Main/trainval.txt')
