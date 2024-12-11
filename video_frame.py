import cv2

# Path to the video file
video_path = 'downloaded_video.mp4'

# Open video file
cap = cv2.VideoCapture(video_path)

frame_number = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_path = f'frames/frame_{frame_number}.jpg'
    cv2.imwrite(frame_path, frame)  # Save frame as an image
    frame_number += 1
cap.release()
print(f"Extracted {frame_number} frames.")
