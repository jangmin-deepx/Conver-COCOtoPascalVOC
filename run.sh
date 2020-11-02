#conda activate pytorch1.5.1
rm ./ImageSets/Main/trainval.txt
python convert_to_pascalformat.py
python getList.py