import requests
import shutil
import os
import cv2
import time
from typing import Generator

FPS = 15
IMG_SIZE = 512

current_dir = os.path.dirname(os.path.realpath(__file__))
with open(f"{current_dir}/available_camera_feeds.txt", "r") as f:
    AVAILABLE_CAMERA_FEEDS = f.read().split("\n")


def get_live_feed(base_url: str, save_video: bool = True) -> Generator[str, None, None]:
    try:
        initial_url = f"{base_url}/playlist.m3u8"

        r = requests.get(initial_url)
        chunk_url = next(l for l in r.text.split("\n") if l.endswith(".m3u8"))

        r = requests.get(f"{base_url}/{chunk_url}")
        ts_urls = [l for l in r.text.split("\n") if l.endswith(".ts")]

        if save_video:
            out_url = f"{current_dir}/temp/{base_url.rsplit('/', -1)[-1].split('.', 1)[0]}.mp4"
            writer = cv2.VideoWriter(
                out_url, cv2.VideoWriter_fourcc(*"mp4v"), FPS, (IMG_SIZE, IMG_SIZE)
            )

        for ts_url in ts_urls:
            with requests.get(f"{base_url}/{ts_url}", stream=True) as r:
                with open(f"{current_dir}/temp/{ts_url}", "wb") as f:
                    shutil.copyfileobj(r.raw, f)

            path = f"{current_dir}/temp/{ts_url}"
            cap = cv2.VideoCapture(path)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))

                if save_video:
                    writer.write(frame)

                encoded_image = cv2.imencode(".jpeg", frame)[1]
                image_bytes = encoded_image.tobytes()

                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + image_bytes + b"\r\n"
                )
                time.sleep(0.05)

            cap.release()

            os.remove(path)

        if save_video:
            writer.release()

    except:
        pass


def main() -> None:
    print(get_live_feed(AVAILABLE_CAMERA_FEEDS[100]))


if __name__ == "__main__":
    main()
