import numpy as np
import argparse
import torch
import cv2
from Alibaba_MIIL_ML_Decoder.models import create_model

# constants 
DEVICE = torch.device("cpu")
COLOR = (0, 255, 0)

parser = argparse.ArgumentParser(description='PyTorch MS_COCO infer')
parser.add_argument('--num-classes', default=196, type=int)
parser.add_argument('--model-path', type=str, default='./back_end/assets/stanford_car_data/tresnet_l_stanford_card_96.41.pth')
parser.add_argument('--pic-path', type=str, default='./back_end/assets/test_images/IMG_3933.jpg')
parser.add_argument('--model-name', type=str, default='tresnet_l')
parser.add_argument('--image-size', type=int, default=448)
# parser.add_argument('--dataset-type', type=str, default='MS-COCO')
parser.add_argument('--th', type=float, default=0.75)
parser.add_argument('--top-k', type=float, default=20)
# ML-Decoder
parser.add_argument('--use-ml-decoder', default=1, type=int)
parser.add_argument('--num-of-groups', default=-1, type=int)  # full-decoding
parser.add_argument('--decoder-embedding', default=768, type=int)
parser.add_argument('--zsl', default=0, type=int)

# construct the argument parser and parse the arguments
# parsing args
args = parser.parse_args()

# Setup model
print('creating model {}...'.format(args.model_name))
model = create_model(args, load_head=True)
########### eliminate BN for faster inference ###########
model = model.cpu().eval()
#######################################################
print('done')

# load in pretrained weights and set the mode to eval
# load the image from disk
image = cv2.imread(args.pic_path)
orig = image.copy()

# pre-processing
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.transpose((2, 0, 1))
image = np.expand_dims(image, axis=0)
image = image / 255.0
image = torch.FloatTensor(image)

# send the input to the device and pass the it through the network to
# get the detections and predictions
image = image.to(DEVICE)
detections = model(image)[0]

# loop over the detections
for i in range(0, len(detections["boxes"])):
	# extract the confidence (i.e., probability) associated with the
	# prediction
	confidence = detections["scores"][i]
	# filter out weak detections by ensuring the confidence is
	# greater than the minimum confidence
	if confidence > args["confidence"]:
		# extract the index of the class label from the detections,
		# then compute the (x, y)-coordinates of the bounding box
		# for the object
		idx = int(detections["labels"][i])
		box = detections["boxes"][i].detach().cpu().numpy()
		(startX, startY, endX, endY) = box.astype("int")
		# display the prediction to our terminal
		# draw the bounding box and label on the image
		cv2.rectangle(orig, (startX, startY), (endX, endY), COLOR, 2)
		
# show the output image
cv2.imshow("Output", orig)
cv2.waitKey(0)