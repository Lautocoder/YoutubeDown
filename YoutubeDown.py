from pytube import YouTube

BASE_YOUTUBE_URL = 'https://www.youtube.com'

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded*100 / stream.filesize
    print(f"On progress ... {int(percent)}%")

while True:
    url=""
    while True:
        url=input("Saisir l'url de la vidéo youtube a télécharger (ENTER pour quitter): ")
        if not url.lower().startswith(BASE_YOUTUBE_URL)  and len(url)>0:
            print("Veuillez saisir le lien d'une video youtube !!!")
        else:
            break


    if  url.lower().startswith(BASE_YOUTUBE_URL):
        youTube_video = YouTube(url)
        youTube_video.register_on_progress_callback(on_download_progress)
        print(f"Vous voulez télécharger la vidéo : {youTube_video.title}")
        try :
            stream=youTube_video.streams.get_highest_resolution()
            # stream=youTube_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            print("Téléchargement...")
            stream.download()
            print("Ok")
        except:
            print(f"Malheureusement on arrive pas à télécharger la vidéo : {youTube_video.title}")
            

    else:
        break
            