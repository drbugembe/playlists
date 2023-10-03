from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os
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


def compress_images(request):
    if request.method == 'POST':
        input_folder = request.POST.get('input_folder')
        output_folder = request.POST.get('output_folder')
        max_file_size = int(request.POST.get('max_file_size'))

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Iterate over the files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                # Open the image file
                image_path = os.path.join(input_folder, filename)
                image = Image.open(image_path)

                # Calculate the current file size
                current_file_size = os.path.getsize(image_path) / 1024  # Size in KB

                # Check if compression is required
                if current_file_size > max_file_size:
                    # Calculate the compression ratio
                    compression_ratio = max_file_size / current_file_size

                    # Resize the image with the compression ratio
                    width, height = image.size
                    new_width = int(width * compression_ratio)
                    new_height = int(height * compression_ratio)
                    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

                    # Save the compressed image with the desired file size
                    output_path = os.path.join(output_folder, filename)
                    resized_image.save(output_path, optimize=True, quality=95)

                    print(f"Compressed {filename} to {max_file_size}KB")
                else:
                    # Copy the image to the output folder if no compression is needed
                    output_path = os.path.join(output_folder, filename)
                    image.save(output_path)

                    print(f"Image {filename} does not require compression")

        print("Compression completed!")
        return HttpResponse("Compression completed!")

    return render(request, 'youtubelists/compress.html')

