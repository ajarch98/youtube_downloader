from pytube import YouTube
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    args = parser.parse_args()

    yt = YouTube(args.url)

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
