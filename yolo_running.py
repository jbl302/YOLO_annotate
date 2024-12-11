import os

import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Input and output folders
frames_folder = "keyframes"
results_folder = "results"

# Ensure the output folder exists
os.makedirs(results_folder, exist_ok=True)

# Process each frame
for frame_file in sorted(os.listdir(frames_folder)):
    frame_path = os.path.join(frames_folder, frame_file)
    result = model(frame_path)  # Perform detection on the frame

    # Step 1: Save the annotated image
    annotated_image = result[0].plot()  # Annotated image as a numpy array
    annotated_image_path = os.path.join(results_folder, f"{frame_file}")
    cv2.imwrite(annotated_image_path, annotated_image)  # Save the annotated image
    print(f"Annotated image saved: {annotated_image_path}")

    # Step 2: Save bounding box data to a text file
    result_text_path = os.path.join(results_folder, f"{os.path.splitext(frame_file)[0]}.txt")
    with open(result_text_path, 'w') as f:
        for box in result[0].boxes:
            # Extract bounding box information
            x, y, w, h = box.xywhn.tolist()[0]  # Normalized x, y, width, height
            # confidence = box.conf.tolist()[0]  # Confidence score
            class_id = int(box.cls.tolist()[0])  # Class ID
            
            # Write the results in the desired format
            f.write(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f} \n")
    print(f"Bounding box data saved: {result_text_path}")

    # Ensure alternating save (image, then text) is explicitly clear in the process
    print(f"Processed frame: {frame_file}")

print("Processing complete. Annotated images and text files are saved alternately in the 'results' folder.")
