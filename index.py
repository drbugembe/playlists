from pytube import Playlist

# URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PLknQy8uSGMyuRnIV-sRDnsi7V7puW7oeh"

# Destination folder to save the downloaded videos
download_folder = "D:/WHM12"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Loop through all the videos in the playlist and download them
for video in playlist.videos:
    try:
        # Print the video title to show progress
        print("Downloading:", video.title)

        # Set the destination path for the downloaded video
        video_stream = video.streams.filter(progressive=True, file_extension="mp4").first()
        video_stream.download(output_path=download_folder)

        # Print a message when the download is complete
        print("Download complete!")

    except Exception as e:
        # Print an error message if the download fails
        print("Error downloading video:", str(e))

print("All videos downloaded successfully!")
