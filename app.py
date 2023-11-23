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
        resolution_combobox.pack(padx=10, pady=5)
        resolution_combobox['values'] = resos
        resolution_combobox.config(state='normal')
        print(f"Valid url {link}")
    else:
        print(f"Not valid url {link}")

def resolution_select(event):
    print(f"Selected {event}")
    progress_label.pack(padx=10, pady=5)
    progressbar.pack(padx=10, pady=5)
    download_button.pack(padx=10, pady=5)
def download_url():
    link = link_text.get()
    res = resolution_combobox.get()
    print(f"downloading initiate {link} {res}")
    download(link, 0, res, on_progress=on_progress, on_complete=on_complete)

def on_complete(stream, file_path) :
    progressbar.forget()
    progress_label.forget()
    download_button.forget()
    link_text.delete(0, 350)
    resolution_combobox.pack_forget()
    download_complete_label.configure(text=file_path)
    download_complete_label.pack()
    download_complete_label.update()
    print(file_path)

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    percentage = float(pct_completed / 100)
    progress_label.configure(text=str(int(pct_completed)) + "%")
    progress_label.update()
    progressbar.set(value=percentage)
    print(f"Status: {percentage} %")



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

check_button = ctk.CTkButton(content_frame, text="Check", command=check_url)
check_button.pack(pady=10, padx=5)

resolutions = ["720p"]
resolution_var = tk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, state='disabled')
# resolution_combobox.pack(pady=10, padx=5)

download_button = ctk.CTkButton(content_frame, text="Download", command=download_url)

resolution_combobox.bind('<<ComboboxSelected>>', resolution_select)


progress_label = ctk.CTkLabel(content_frame, text="0 %")
# progress_label.pack()
progressbar = ctk.CTkProgressBar(content_frame, orientation="horizontal",mode="determinate", width=350, )
# progressbar.pack(padx=10 ,pady=10)
progressbar.set(0)

download_complete_label = ctk.CTkLabel(content_frame, text="")


root.mainloop()
