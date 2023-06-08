import requests
import os


url = "https://parsinger.ru/video_downloads/videoplayback.mp4"

response = requests.get(url=url, stream=True)

with open('videoplayback.mp4', "wb") as video:
    for _ in response:
        video.write(response.content)


def get_file_size(file_name, absolute=None) -> int:
    if not absolute:
        direct = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(direct, file_name)
    return os.path.getsize(file_name)


print(get_file_size("videoplayback.mp4"))
