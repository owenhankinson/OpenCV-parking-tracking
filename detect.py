import numpy as np
import tensorflow as tf
from PIL import Image
import math
import cv2
from timeit import default_timer as timer
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Taken from https://github.com/anis-13/Cars-detection-on-Tflite
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model_float.tflite")

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

inp_mean = 127.5
inp_std = 127.5


# read a video file
cap = cv2.VideoCapture(0)  # 1 uses the webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
car_frames_counted = 0 # number appended to file. Reset after the hour
t = timer()
def hourHasPast(cur_time): # current_time in seconds 
    if cur_time % 3600 == 0: # 3600 = 1 hr
        return True
    return False

while cap.isOpened():
    # read frames

    if hourHasPast(math.floor(timer())):
        car_frames_counted = 0 # reset frames after the hour
    ret, img2 = cap.read()

    t_in = cv2.getTickCount()
    if ret:
        img = cv2.resize(img2, (300, 300))

        # convert for float graph
        # convert image from 0:255 to -1 : 1
        input_data = (abs((np.array(img) - inp_mean) /
                      inp_std) - 1)  .astype(np.float32)

        input_data = np.expand_dims(input_data, axis=0)

        # Test model on random input data.
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        predictions = np.squeeze(
            interpreter.get_tensor(output_details[0]['index']))
        output_classes = np.squeeze(
            interpreter.get_tensor(output_details[1]['index']))
        confidence_scores = np.squeeze(
            interpreter.get_tensor(output_details[2]['index']))

        for i, newbox in enumerate(predictions):
            if confidence_scores[i] > 0.2:
                car_frames_counted += 1
                val = np.asarray(newbox)
                y_min = int(val[0] * 480)

                y_max = int(val[2] * 480)

                x_min = int(val[1] * 640)

                x_max = int(val[3] * 640)
                cv2.rectangle(np.asarray(img2), (x_min, y_min),
                              (x_max, y_max), (0, 255, 0), 2, 1)

        fps = round(cv2.getTickFrequency() / (cv2.getTickCount() - t_in), 2)
        cv2.putText(img2, 'FPS : {}  '.format(fps), (280, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), lineType=cv2.LINE_AA)
        
        cur_time = timer()
        cv2.putText(img2, f'Time : {cur_time}  ', (280, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), lineType=cv2.LINE_AA)
        cv2.putText(img2, f'Captured : {car_frames_counted}  ', (280, 120),
            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), lineType=cv2.LINE_AA)
        cv2.imshow(' ', np.asarray(img2))
        # out.write(img2)
        cv2.waitKey(1)
    else:
        break
