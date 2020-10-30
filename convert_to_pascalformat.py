from models.coco import COCO
import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Convert COCO Dataset Annotation into VOC Annotation")
parser.add_argument('--anno', type=str, default='/mnt/datasets/COCO/official/annotations/instances_train2017.json', help="Path To COCO Annotation.json")
parser.add_argument('--out', type=str, default='./Annotations/', help="Path To COCO Annotation.json")

def main():
	args = parser.parse_args()
	Anootation_path= args.anno
	output_dir = args.out

	coco=COCO(Anootation_path)
	cats = coco.loadCats(coco.getCatIds())
	nms=[cat['name'] for cat in cats]

	imgIds = coco.getImgIds()

	if not os.path.exists(output_dir):
	    os.makedirs(output_dir)

	for n in range(len(imgIds)):
		img = coco.loadImgs(imgIds[n])[0]
		annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
		anns = coco.loadAnns(annIds)


		xml = '<annotation>\n\t<folder>\n\t\tCOCO2014pascalformat\n\t</folder>\n\t<filename>\n'
		xml += '\t\t' + img['file_name'] + '\n\t</filename>\n\t<source>\n\t\t<database>\n\t\t\tCOCO2014pascalformat\n\t\t</database>\n\t</source>\n\t<size>\n\t\t'
		xml += '<width>\n\t\t\t' + str(img['width']) + '\n\t\t</width>\n\t\t' + '<height>\n\t\t\t' + str(img['height']) + '\n\t\t</height>\n\t\t'
		xml += '<depth>\n\t\t\t3\n\t\t</depth>\n\t</size>\n\t<segmented>\n\t\t0\n\t</segmented>\n'

		for i in range(len(anns)):
			bbox = anns[i]['bbox']
			xml += '\t<object>\n\t\t<name>\n\t\t\t' + str(anns[i]['category_id']) + '\n\t\t</name>\n'
			xml += '\t\t<bndbox>\n\t\t\t<xmin>\n\t\t\t\t' + str(int(round(bbox[0]))) + '\n\t\t\t</xmin>\n'
			xml += '\t\t\t<ymin>\n\t\t\t\t' + str(int(round(bbox[1]))) + '\n\t\t\t</ymin>\n'
			xml += '\t\t\t<xmax>\n\t\t\t\t' + str(int(round(bbox[0] + bbox[2]))) + '\n\t\t\t</xmax>\n'
			xml += '\t\t\t<ymax>\n\t\t\t\t' + str(int(round(bbox[1] + bbox[3]))) + '\n\t\t\t</ymax>\n\t\t</bndbox>\n'
			xml += '\t\t<truncated>\n\t\t\t0\n\t\t</truncated>\n\t\t<difficult>\n\t\t\t0\n\t\t</difficult>\n\t</object>\n'
		xml += '</annotation>'
		f_xml = open(output_dir + img['file_name'].split('.jpg')[0] + '.xml', 'w')
		f_xml.write(xml)
		f_xml.close()
		print(str(n+1) + ' out of ' + str(len(imgIds)))

if __name__ == '__main__':
  main()
