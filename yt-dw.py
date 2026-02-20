from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import filedialog



print("1 - download")
print("2 - exit")
choose = int(input("Enter : "))
while choose != 2:
    if choose == 1:
            url = input("Enter link : ")
            yt = YouTube(url,on_progress_callback=on_progress)
            print(f"Name : {yt.title}")
            str = input(("Right ? {y/n}"))
            if (str == 'y'):
                folder = filedialog.askdirectory(title="Enter folder for save ")
                if folder:
                    ys = yt.streams.get_highest_resolution()
                    ys.download(folder)
                    print(f"\nSave on {folder}")
                    print("1 - download")
                    print("2 - exit")
                    choose = int(input("Enter : "))
            elif (str == 'n'):
                    print("Okay , enter new link")

if choose == 2:
     print("Exit, Bye!")

