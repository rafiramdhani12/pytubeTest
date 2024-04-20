import tkinter
import customtkinter
from pytube import YouTube 

def startDownload():
    try:
        YtLink = link.get()
        ytObject = YouTube(YtLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_lowest_resolution()
        
        title.configure(text=ytObject.title,text_color="white")
        finishLabel.configure(text="")
        finishLabel.configure(text="downloaded")
        video.download()
    except:
         finishLabel.configure(text="downloaded error",text_color="red")
   
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded= total_size - bytes_remaining
    percentage_of_complition = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_complition))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    
    #update progress bar
    progressBar.set(float(percentage_of_complition)/100)
    

# system setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding ui element
title = customtkinter.CTkLabel(app, text="insert a youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350 , height=40,textvariable=url_var)
link.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#proggres percentage
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#download button
download = customtkinter.CTkButton(app,text="download",command=startDownload)
download.pack()

# run app
app.mainloop()
   

# url ='https://youtu.be/TDi-hGRYX6g?si=a3ek83LjRX5eNjff'

# yt = YouTube(url)

# stream = yt.streams.get_by_resolution("480p")

# stream.download()