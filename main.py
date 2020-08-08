from pytube import YouTube
import argparse
import sys


def on_progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining

    ch = '█'

    done = int(bytes_received / filesize * 20)
    remaining = int(bytes_remaining / filesize * 20)

    bar = ch * done + ' ' * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = f' -> |{bar}| {percent}%\r'

    sys.stdout.write(text)
    sys.stdout.flush()


def download(url):
    yt = YouTube(url, on_progress_callback=on_progress)

    streams_list = yt.streams.filter(file_extension='mp4', progressive=True)
    print("Available videos:")

    for _, stream in enumerate(streams_list, start=1):
        filename = stream.default_filename
        size = stream.filesize_approx/1000000
        resolution = stream.resolution
        print(
            f"{_}. Name: {filename} | Resolution: {resolution}| Size in MB: {size}"
        )

    stream_id = int(
        input("Enter the number of the file you would like to download: ")
    )
    stream = streams_list[stream_id - 1]
    stream.download()

    print("Download complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    args = parser.parse_args()

    download(args.url)
