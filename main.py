import cv2
from dense_optical_flow import *
from sparse_optical_flow import *

cap = cv2.VideoCapture("example_1.mov")
DenseOpticalFlow(cap)
