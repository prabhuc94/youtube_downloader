import customtkinter as ctk
from logic import fetch_resolutions, download
from tkinter import ttk
import tkinter as tk
import os
import validators

def check_url():
    link = link_text.get()
    is_valid = validators.url(link)
    if is_valid:
        res = fetch_resolutions(link)
        print(f"Res {res}")
        resos = []
        for s in res:
            resos.append(s['res'])
        resolution_combobox['values'] = resos
        resolution_combobox.config(state='normal')
        print(f"Valid url {link}")
    else:
        print(f"Not valid url {link}")

def resolution_select(event):
    print(f"Selected {event}")
    download_button.pack()
def download_url():
    link = link_text.get()
    res = resolution_combobox.get()
    print(f"downloading initiate {link} {res}")
    progressbar.pack()
    complete = download(link, 0, res, on_progress=on_progress)
    if bool(complete and not complete.isspace()):
        print(f"downloading completed")


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    progressbar.set(value=round(pct_completed))
    progress_label.configure(text=f"{round(pct_completed)} %")
    print(f"Status: {round(pct_completed)} %")


root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title('Youtube Downloader!')

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

link_text = ctk.CTkEntry(content_frame, width=350, height=40, placeholder_text="Enter the youtube url here...")
link_text.pack(pady=10, padx=5)

text_var = tk.StringVar()
check_button = ctk.CTkButton(content_frame, text="Check", textvariable=text_var, command=check_url)
check_button.pack(pady=10, padx=5)

text_var.set("Checking")

resolutions = ["720p"]
resolution_var = tk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, state='disabled')
resolution_combobox.pack(pady=10, padx=5)

download_button = ctk.CTkButton(content_frame, text="Download", command=download_url)

resolution_combobox.bind('<<ComboboxSelected>>', resolution_select)


progress_label = ctk.CTkLabel(content_frame, text="0 %")
progress_label.pack()
progressbar = ctk.CTkProgressBar(content_frame, orientation="horizontal",mode="determinate", width=350, )
progressbar.pack(padx=10 ,pady=10)

root.mainloop()
