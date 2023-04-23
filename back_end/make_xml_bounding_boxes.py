import xml.etree.ElementTree as gfg
import os 
import scipy.io as sio

# and then just call the function
my_file = r"/Users/owenhankinson/Desktop/Computer Vision/OpenCV-parking-tracking/back_end/assets/stanford_car_data/devkit/cars_train_annos.mat"

def generateXMLFile(fullpath: str, folderName: str,  fileNameText: str, xmin: int, xmax: int, ymin: int, ymax: int):
  root = gfg.Element("annotation")
    
  folder = gfg.Element('folder') 
  folder.text = f"{folderName}"
  root.append(folder)

  fileName = gfg.Element('filename')
  fileName.text = f"{fileNameText}"
  root.append(fileName)

  path = gfg.Element('path')
  path.text = f"{fullpath}"
  root.append(path)

  size = gfg.Element('size')
  root.append(size)

  width = gfg.SubElement(size, "width")
  width.text = "800"

  height = gfg.SubElement(size, "height")
  height.text = "600"

  depth = gfg.SubElement(size, "depth")
  depth.text = "3"

  object = gfg.Element('object')
  root.append(object)

  name = gfg.SubElement(object, "name")
  name.text = "car"

  pose = gfg.SubElement(object, "pose")
  pose.text = "Unspecified"

  truncated = gfg.SubElement(object, "truncated")
  truncated.text = "0"

  difficult = gfg.SubElement(object, "difficult")  
  difficult.text = "Unspecified"

  bndbox = gfg.SubElement(object, "bndbox")

  _xmin = gfg.SubElement(bndbox, "xmin")
  _xmin.text = f"{xmin}"

  _xmax = gfg.SubElement(bndbox, "xmax")
  _xmax.text = f"{xmax}"

  _ymin = gfg.SubElement(bndbox, "ymin")
  _ymin.text = f"{ymin}"

  _ymax = gfg.SubElement(bndbox, "ymax")
  _ymax.text = f"{ymax}"
  
  no_ext = fileNameText.split(".")[0]
  save_path_file = f"/Users/owenhankinson/Desktop/Computer Vision/OpenCV-parking-tracking/back_end/assets/stanford_car_data/{folderName}/{no_ext}.xml"

  tree = gfg.ElementTree(root)
    
  with open(save_path_file, "wb") as f:
    tree.write(f) 
    f.close()


if __name__ == "__main__": 
  top_data = sio.loadmat(my_file)
  for i in range(len(top_data["annotations"][0])):
    data = top_data["annotations"][0][i]
    fileName = data[5][0] #5 for train 4 for test
    generateXMLFile(f"/Users/owenhankinson/Desktop/Computer Vision/OpenCV-parking-tracking/back_end/assets/stanford_car_data/cars_train/{fileName}", "cars_train", fileName, data[0][0][0], data[1][0][0], data[2][0][0], data[3][0][0])


# <annotation verified="yes">
# 	<folder>train</folder>
# 	<filename>IMG_0509.jpg</filename>
# 	<path>/Users/thuytran/Downloads/Photos-002/train/IMG_0509.jpg</path>
# 	<source>
# 		<database>Unknown</database>
# 	</source>
# 	<size>
# 		<width>800</width>
# 		<height>600</height>
# 		<depth>3</depth>
# 	</size>
# 	<segmented>0</segmented>
# 	<object>
# 		<name>android</name>
# 		<pose>Unspecified</pose>
# 		<truncated>0</truncated>
# 		<difficult>0</difficult>
# 		<bndbox>
# 			<xmin>10</xmin>
# 			<ymin>131</ymin>
# 			<xmax>288</xmax>
# 			<ymax>401</ymax>
# 		</bndbox>
# 	</object>
# 	<object>
# 		<name>pig_android</name>
# 		<pose>Unspecified</pose>
# 		<truncated>0</truncated>
# 		<difficult>0</difficult>
# 		<bndbox>
# 			<xmin>526</xmin>
# 			<ymin>82</ymin>
# 			<xmax>722</xmax>
# 			<ymax>324</ymax>
# 		</bndbox>
# 	</object>
# </annotation>