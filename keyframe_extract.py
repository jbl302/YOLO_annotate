# import cv2

# # Initialize the default camera
# camera = cv2.VideoCapture(0)

# # Check if the camera opened successfully
# if not camera.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# while True:
#     # Capture a single frame
#     ret, frame = camera.read()
#     ret = False
#     # Check if the frame was successfully captured
#     if not ret:
#         print("Failed to capture frame. Exiting...")
#         break

#     # Display the frame
#     # print(frame)
#     cv2.imshow("Camera Feed", frame)

#     # Break the loop if the user presses the 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# # Release the camera
# camera.release()

# # Destroy all OpenCV windows
# cv2.destroyAllWindows()


import videokf as vf

vf.extract_keyframes("downloaded_video.mp4")