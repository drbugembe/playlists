from django.shortcuts import render
from pytube import Playlist

def index(request):
    message = None
    if request.method == 'POST':
        playlist_url = request.POST['playlist_url']
        download_folder = request.POST['download_folder']

        try:
            playlist = Playlist(playlist_url)
            for video in playlist.videos:
                video_stream = video.streams.filter(progressive=True, file_extension="mp4").first()
                video_stream.download(output_path=download_folder)
            message = "Download complete!"
        except Exception as e:
            message = f"Error downloading videos: {str(e)}"

    return render(request, 'youtubelists/index.html', {'message': message})
