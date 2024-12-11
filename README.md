# Project Workflow

## Key Steps

### 1. Clone the Repository
Start by cloning the repository to your local machine.

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Required Libraries
Install all the necessary libraries specified in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Download a Video
run the `data_download.py` it will download a sample video 
- Use **Pixabay**, a free platform, and explore its [API documentation](https://pixabay.com/api/docs/) for video-related resources.
- Alternatively, use a different platform of your choice to download the video.

### 5. Extract Keyframes
Run the `keyframe_extract.py` script to extract keyframes from the downloaded video.  

```bash
python keyframe_extract.py
```

If needed, you can replace this script with a different keyframe extraction tool of your choice.

### 6. Run YOLO Detection
Run the `yolo_running.py` script to:
- Create annotated images.
- Generate corresponding `.txt` files containing object coordinates (`x, y, w, h`).  

```bash
python yolo_running.py
```

### 7. Verify Annotations
Use the **LabelImg** tool to verify the annotations. This step ensures that the generated bounding boxes are accurate.

## Additional Notes
- You can explore alternate tools or scripts for keyframe extraction and video downloading if the provided options do not suit your workflow.
- Ensure your environment is configured correctly to avoid runtime issues.
