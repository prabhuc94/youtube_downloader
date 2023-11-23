import os
from pathlib import Path
from pytube import YouTube
from file_sizer import convert_size


def fetch_resolutions(link):
    yt = YouTube(link)
    resolutions = []
    for s in yt.streams.filter(type='video'):
        if s.is_progressive:
            resolutions.append({
                "res": s.resolution,
                "tag": s.itag,
                "size": convert_size(s.filesize),
                "mime": s.mime_type.replace('video/', ''),
                "fps": s.fps
            })

    return resolutions


def download(link, tag, res, on_progress, on_complete):
    yt = YouTube(link, on_progress_callback=on_progress, on_complete_callback=on_complete)
    downloads_path = str(Path.home() / "Downloads")
    if tag != 0:
        yt.streams.get_by_itag(tag).download(output_path=downloads_path)
    elif bool(res and not res.isspace()):
        yt.streams.get_by_resolution(res).download(output_path=downloads_path)
    else:
        yt.streams.get_highest_resolution().download(output_path=downloads_path)
    return "done"
