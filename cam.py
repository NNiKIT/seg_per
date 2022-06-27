import cv2

# Start a video cam session
video_session = cv2.VideoCapture(0)

# Given a video capture object, read frames from the same and convert it to RGB
def grab_frame(cap):
  _, frame = cap.read()
  return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)