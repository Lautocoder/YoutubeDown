# YoutubeDown

Un téléchargeur de vidéos YouTube simple et convivial.

## ⚡ Pour les utilisateurs (sans développement)

1. Télécharge `YoutubeDown.exe` depuis la section [Releases](../../releases)
2. Double-clique sur l'exe pour lancer le programme
3. Saisis l'URL YouTube et valide
4. La vidéo sera téléchargée dans un sous-dossier download

**Prérequis :** Aucun ! L'exe embarque tout ce qu'il faut.

## 👨‍💻 Pour les développeurs

### Installation

```bash
# Clone le repo
git clone https://github.com/Lautocoder/YoutubeDown.git
cd YoutubeDown

# Crée l'environnement virtuel
python -m venv myenv

# Active l'env
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate

# Installe les dépendances
pip install -r requirements.txt
```

### Générer l'exe

```bash
pip install pyinstaller
pyinstaller --onefile YoutubeDown.py
```

L'exe sera dans `dist/YoutubeDown.exe`.

## 📋 Prérequis système

- **Pour l'exe** : Rien (tout est inclus)
- **Pour développer** : Python 3.8+, ffmpeg (optionnel mais recommandé pour la fusion vidéo/audio)

## 📝 Notes

- Les vidéos sont téléchargées en MP4 avec meilleure qualité
- Confirmez avant chaque téléchargement
- Appuyez sur ENTER sans URL pour quitter
