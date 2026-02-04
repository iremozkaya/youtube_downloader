import yt_dlp

url = input("enter URL: ")

ydl_opts = {
    'format': 'best',
    'outtmpl': r'C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\%(title)s.(ext)s'
}

try: 
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except:
    print("error")