import argparse
from pytube import YouTube
import validators
import sys
import os
from pathlib import Path
from progressbar import progress_function, on_progress, on_complete


def cli_argument():
    parser = argparse.ArgumentParser(description="Download youtube video / auto  based on argument")
    parser.add_argument("-a", "--audio", dest="audio", type=str, help="Enter youtube url to download audio only")
    parser.add_argument("-v", "--video", dest="video", type=str, help="Enter youtube url to download video only")
    argument = parser.parse_args()
    if argument.audio:
        download_audio(argument.audio)
    elif argument.video:
        download_video(argument.video)

def download_audio(yt_url):
    is_valid = validators.url(yt_url)
    if not is_valid:
        print(f"Given url is not valid one [{yt_url}]")
        sys.exit()
    yt = YouTube(yt_url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    downloads_path = str(Path.home() / "Downloads")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=downloads_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def download_video(yt_url):
    is_valid = validators.url(yt_url)
    if not is_valid:
        print(f"Given url is not valid one [{yt_url}]")
        sys.exit()
    yt = YouTube(yt_url, on_progress_callback=progress_function, on_complete_callback=on_complete)
    downloads_path = str(Path.home() / "Downloads")
    video = yt.streams.filter(type='video', progressive=True,).get_highest_resolution()
    print(f"Downloading resolution {video.resolution}")
    out_file = video.download(output_path=downloads_path)

args = cli_argument()