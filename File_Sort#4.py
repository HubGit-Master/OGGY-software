#Python Project, V1.4. OGGY SOFTWARE, 2026/2/21
#Tested on Linux Mint 22.3, Linux 6.17.0-14 Python 3.10.12.
#Should work on almost every computer with Python 3.10.12.
#If you have any issues, please report them to my github:@HubGit-Master

import os
import shutil
home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")

document_filer = (".txt", ".docx", ".pdf", ".docm", ".odt", ".pptx", ".odp")
image_filer = (".jpg", ".png", ".gif", ".bmp", ".svg", ".ott")
video_filer = (".mp4", ".avi", ".mkv")
audio_filer = (".mp3", ".wav", ".flac")
code_filer = (".py", ".js", ".html", ".css", ".exe", ".msi")

documents = os.path.join(home, "Documents")
pictures = os.path.join(home, "Pictures")
videos = os.path.join(home, "Videos")
music = os.path.join(home, "Music")
desktop = os.path.join(home, "Desktop")

for folder in (documents, pictures, videos, music, desktop):
    os.makedirs(folder, exist_ok=True)

for file in os.listdir(downloads):
    full_path = os.path.join(downloads, file)

    if not os.path.isfile(full_path):
        continue

    if file.lower().endswith(document_filer):
        print(f"Moving {file} from Downloads to Documents...")
        shutil.move(full_path, os.path.join(documents, file))

    elif file.lower().endswith(image_filer):
        print(f"Moving {file} from Downloads to Pictures...")
        shutil.move(full_path, os.path.join(pictures, file))

    elif file.lower().endswith(video_filer):
        print(f"Moving {file} from Downloads to Videos...")
        shutil.move(full_path, os.path.join(videos, file))

    elif file.lower().endswith(audio_filer):
        print(f"Moving {file} from Downloads to Music...")
        shutil.move(full_path, os.path.join(music, file))

    elif file.lower().endswith(code_filer):
        print(f"Moving {file} from Downloads to Desktop...")
        shutil.move(full_path, os.path.join(desktop, file))


print("No (More) files to move.")
