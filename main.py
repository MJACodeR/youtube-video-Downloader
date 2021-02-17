from pytube import*
from pytube import YouTube
from tkinter import*
from tkinter .filedialog import*
from tkinter .messagebox import*
from threading import*
# Total size container
file_size = 0
# this get called for updating pecenteges


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # get the pecentge of file that has been download
    #file_downloaded = (file_size - remaining)
    percent = (100*(file_size-remaining))/file_size
    dBtn.config(text="{:00.0f} % downloaded".format(percent))


def startDownload():
    #global file_size
    try:
        url = urlField.get()
        print(url)
        # changing_button_Text
        dBtn.config(text="Please Wait..")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
# creating youtube object(ob) with url
        ob = YouTube(url, on_progress_callback=progress)
        strm = ob.streams.first()
        file_size = strm.filesize
        # print(file_size)
        # print(strms)
        print(ob.title)
        print(ob.length)
        print(ob.views)
        print(ob.rating)
# print(ob.description)
# NOW_DOWNLOAD_FUNCTION
        strm.download(path_to_save_video)
        print("Thank YOU for Downloding video")
        dBtn.config(text="Done..")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download fineshed", "Thank You for Downloading")
        urlField.delete(0, END)

    except Exception as e:
        print(e)
        print("error")

# Creating new thread


def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()


    # Starting_GUI_buliding
main = Tk()
main.title("My Youtube Downloader")
# SET_THE_ICON
main.iconbitmap('icon.ico')
main.geometry("500x600")
# heading icon
file = PhotoImage(file="youtube.png")
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP, pady=20)
# URL_Text_FILED
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=20)

# DOWNLOAD_BUTTON
dBtn = Button(main, text="start Download", font=(
    "verdana", 18), relief="ridge", command=startDownloadThread)
dBtn.pack(side=TOP, pady=15)
main.mainloop()
