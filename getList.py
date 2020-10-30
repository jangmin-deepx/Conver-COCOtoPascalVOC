import os
import pathlib

def getFileList(p,output):
    fileList = os.listdir(p)
    dir_output_path = '/'.join(output.split('/')[:-1])
    pathlib.Path(dir_output_path).mkdir(parents=True, exist_ok=True)

    text_output = open(output, 'w')
    for f in fileList:
        f = f.split('.')[0]
        text_output.write(f'{f}\n')

if __name__ == "__main__":
    getFileList('./Annotations', './IMAGE/main/trainval.txt')
