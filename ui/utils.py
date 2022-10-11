import os
from pathlib import Path
import requests
import glob

dest_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")


def clear_installed_videos(_=None):
    # Ensure directory exists
    Path(dest_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = glob.glob(f"{dest_path}/*")
    for f in files:
        print(f"{f} removed")
        os.remove(f)


def download_video(_, url: str):
    clear_installed_videos()
    response = requests.get(url)
    open(os.path.join(Path(dest_path), "deck_startup.webm"), "wb").write(response.content)
