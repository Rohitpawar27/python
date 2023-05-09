import cv2
d=cv2.VideoCapture("abcd.mp4")
frame=d.get(cv2.CAP_PROP_FRAME_COUNT)
t=d.get(cv2.CAP_PROP_FPS)
print(frame)
print(t)