from tkinter import *
# from pytube import YouTube
from pytubefix import YouTube

class Downloader:
    def __init__(self):
        bgColor = '#0c070c'
        fgColor = '#efe4f0'
        btnColor = '#66374b'
        
        # self.link = link
        self.root = Tk()
        self.root.title("Youtube Downloader")
        self.root.geometry('720x480')

        self.root.configure(bg=bgColor)
        self.root.minsize(480,360)
        self.root.maxsize(1280,720)

        header_text = Label(self.root, text="Youtube Downloader", bg=bgColor, fg=fgColor, font=('sans-serif', 30))
        header_text.pack(pady=10)

        input_text = Label(self.root, text="please enter youtube video's link", bg=bgColor, fg=fgColor,font=('sans-serif',10))
        input_text.pack(pady=(10,5))

        self.link_input = Entry(self.root, width=30)
        self.link_input.pack(pady=(1, 15), ipady=2)

        download_button = Button(text='download', bg=btnColor,fg=fgColor, width=15, height=1, command=self.downloader)
        download_button.pack(pady=(10,10))
        
    def downloader(self):
        link = self.link_input.get()
        yt = YouTube(link)
        print(yt.title)

        video = yt.streams.get_highest_resolution()
        video.download()



    def start(self):
        self.root.mainloop()
    


loader = Downloader() #passes the link
loader.start()
