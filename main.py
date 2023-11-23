from logic import fetch_resolutions, download

link = input("Paste link here: ")

print(f'Resolutions {fetch_resolutions(link)}')

tag = input('Enter tag id: ')
print("Downloading...")
download(link, tag)
print("Downloaded successfully!")