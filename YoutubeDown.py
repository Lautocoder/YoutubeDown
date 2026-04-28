import yt_dlp
import os

BASE_YOUTUBE_URL = 'https://www.youtube.com'

def download_video(url: str):
    # Options yt-dlp: on privilégie la meilleure vidéo/audio MP4 et on fusionne le résultat en un seul fichier.
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # On récupère les métadonnées avant de lancer le téléchargement pour afficher le titre à l'utilisateur.
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'Vidéo inconnue')
        print(f"Vous voulez télécharger la vidéo : {title}")

        # Double validation: l'utilisateur confirme explicitement avant de consommer la bande passante.
        confirm = input("Confirmer le téléchargement ? (O/n) : ").strip().lower()
        if confirm == 'o' or confirm == '':
            print("Téléchargement...")
            ydl.download([url])
            print("✓ Téléchargement terminé !")
        else:
            print("Téléchargement annulé.")

def progress_hook(d: dict):
    # Ce hook est appelé par yt-dlp pendant le téléchargement pour afficher une progression simple en console.
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        if total > 0:
            percent = downloaded * 100 / total
            speed = d.get('speed', 0) or 0
            speed_kb = speed / 1024
            print(f"\rOn progress ... {int(percent)}% | {speed_kb:.1f} KB/s", end='', flush=True)
    elif d['status'] == 'finished':
        print()  # Nouvelle ligne après la barre de progression

while True:
    url = ""
    while True:
        # On boucle jusqu'à obtenir une URL vide (quitte) ou une URL YouTube valide.
        url = input("\nSaisir l'url de la vidéo youtube à télécharger (ENTER pour quitter) : ").strip()

        if len(url) == 0:
            break
        elif not url.lower().startswith(BASE_YOUTUBE_URL):
            print("Veuillez saisir le lien d'une vidéo YouTube !")
        else:
            break

    if url.lower().startswith(BASE_YOUTUBE_URL):
        try:
            download_video(url)
        except yt_dlp.utils.DownloadError as e:
            print(f"Erreur lors du téléchargement : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
    else:
        print("Au revoir !")
        break