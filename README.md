Using a Raspberry Pi and tensorflow lite. We used a model to detect and graph a heatmap of when traffic was highest going in and out of TMU dorm area. 

#### Results
Raw results are found in results.txt where you can see the hours of operations and how many frames were captured of cars passing through. Program running at ~6 FPS so if a car passes by up or down the hill it would be about 3-5 seconds of detection. By dividing the frames captured by these low and high bounds we can get a range of how many vehicles passed by. (each car = 18 - 30 frames). There are some issues with the way we capture parked cars. If a car was parked in front of the camera for an extended amount of time, that may skew the distribution. 
