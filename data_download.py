import requests

url = "https://pixabay.com/api/videos/?key=47534568-57a2359c4467bf92c1f79460d&q=people+walking"


response = requests.get(url)
structured = response.json()
video_url = structured['hits'][0]['videos']['large']['url']
print(video_url)
# print(response.json())
video_response = requests.get(video_url)

if video_response.status_code == 200:
    # Define the output file path where the video will be saved
    output_path = "downloaded_video.mp4"

    # Open the file in write-binary mode and save the content
    with open(output_path, 'wb') as f:
        f.write(video_response.content)

    print(f"Video downloaded successfully: {output_path}")
else:
    print("Failed to download the video.")