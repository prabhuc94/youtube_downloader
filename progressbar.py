import sys

def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    filesize = chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    percentage = float(pct_completed / 100)
    print_progressbar(total_size, bytes_downloaded)

def print_progressbar(total, current, barsize=60):
    progress = int(current*barsize/total)
    completed = str(int(current*100/total)) + '%'
    print('[', chr(9608)*progress, ' ', completed, '.'*(barsize-progress), '] ', str(current)+'/'+str(total), sep='', end='\r', flush=True)

def on_complete(stream, file_path) :
    print(f"Downloaded successfully {file_path}")