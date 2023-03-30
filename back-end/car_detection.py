# Import libraries
from PIL import Image
import cv2
import numpy as np

# SOURCE: https://www.analyticsvidhya.com/blog/2021/12/vehicle-detection-and-counting-system-using-opencv/
#         https://pimylifeup.com/raspberry-pi-security-camera/

# Ideas for space recognition: 
# 1. Send in video feed that is monitored for car movement (most precise)
# 2. Take a snapshot of the cars every 30 seconds (2880 pictures in a day), purge all images every 4ish hours (30 second accuracy)

'''
  Work Flow:
    1. Raspberry Pi takes a picture of the parking spaces (every 30 seconds)
    2. Python then uses the cascade to detect the cars in the spaces
    3. Send a request to the front end site (hosted by the school hopefully)
    4. Front end displays a diagram of cars in/out of the spaces. 
'''
# ---------------------------------------------------------------------------------------------------------------------------------

class Car():
  def __init__(self, location, color):
    self.location = location
    self.color = color
  
  def printLocation(self):
     return self.location
  
  def printColor(self):
     return self.color


def detectAndCountCars():
  car_map: list[Car] = [] 

  image = Image.Image # image goes here we will set up a script on the raspberryPI that will take an image, then run this script with the most recent image taken.
  image = image.resize((450,250))
  image_arr = np.array(image)

  # grayscale
  grey = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)
  Image.fromarray(grey)

  # blur
  blur = cv2.GaussianBlur(grey,(5,5),0)
  Image.fromarray(blur)

  # dialation
  dilated = cv2.dilate(blur,np.ones((3,3)))
  Image.fromarray(dilated)

  # detect cars using a pretrained cascade
  car_cascade_src = '/content/drive/MyDrive/Computer Vision/data/cars.xml'
  car_cascade = cv2.CascadeClassifier(car_cascade_src)
  cars = car_cascade.detectMultiScale(dilated, 1.1, 1)

  # Draw rectangle around cars
  cnt = 0
  for (x,y,w,h) in cars:
      cv2.rectangle(image_arr,(x,y),(x+w,y+h),(255,0,0),2)
      cnt += 1
  print(cnt, " cars found")
  Image.fromarray(image_arr)


  # try with video
  video_src = '/content/drive/MyDrive/Computer Vision/data/Cars.mp4'

  cap = cv2.VideoCapture(video_src)
  car_cascade = cv2.CascadeClassifier(car_cascade_src)
  video = cv2.VideoWriter('result.mp4',0x7634706d, 15, (450,250))

  # return map of cars and what location they are in. 

