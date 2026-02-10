import yt_dlp

while True:
    format=input("---------------\nfor mp3: enter 1\nfor mp4: enter 2\nyour choice: ")
    if format=="1":
        url=input("enter URL: ")

        ydl_opts={
        'format': 'bestaudio/best',
        'outtmpl': r'C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\yt_downloader\%(title)s.(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("mp3 successfully downloaded")
                break
        except:
            print("ERROR")

    elif format=="2":
        url=input("enter URL: ")

        ydl_opts={
            'format': 'best',
            'outtmpl': r'C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\yt_downloader\%(title)s.(ext)s'
        }

        try: 
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("video successfully downloaded")
                break
        except:
            print("ERROR")
        
    else:
        print("invalid choice, try again")