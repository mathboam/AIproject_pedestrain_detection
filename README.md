PROJECT WORK

# AIproject_pedestrain_detection

Introduction:
Pedestrain as  defined in the dictionary is a person walking rather than travelling in a vehicle. Basically pedestrains are humans with some features like hand bags, cover cloths, clothing and others. In this project we used a humna detection algorithm in detecting the pedestrains on the streets and road sides.

Data and Methodology:
We build a pedestrian detection system by by combining Histogram of Oriented Gradients (HoG) feature and support vector machine (SVM). HoG feature provides a reasonable and feature invariant object representation, while SVM framework gives us a robust classifier that can control both the training set error and the classifier's complexity. Which was what we used in our project. A trained human detection and pedestrain detection classifier was used for this project.This project works on the web.

While it is possible to detect pedestrians from images, videos, and webcam streaming, we only focus on detection from videos.

Dependencies:
python (version 3.8 was used in this project)
opencv 
numpy
flask

Command format:
Our system was tested and runnned locally with flask. So once u have this repo and have all the dependencies installed successfully, u navigate into this repo on ur device and run the following in your terminal:

$ export FLASK_APP=pedestraindetection.py
$ flask run

this will run the app locally. Visit the port in ur browser and upload a video for it to detect the pedestrains and 
 

INPUT:  video
OUTPUT: streaming video with the pedestrain detection

Conclusion:
This project is detecting pedestrains and humans by the road side and can be used for any human and pedestrain detection work.


References:
https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html
