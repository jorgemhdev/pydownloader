from pytube import YouTube


""" #code from StackOverflow(https://stackoverflow.com/questions/49185538/how-to-add-progress-bar#comment108955353_49241754) that i still have to try
#uses on_progress_callback
def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def progress_monitor(self, stream, chunk, file_handle, bytes_remaining):

    size = video.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size) """


print(" ")
print("--------------------------------------------------------------------------------")
print("|                               PyDownloader v 1.0                             |")
print("|              A simple Python script that downloads YouTube Videos            |")
print("|                      Made by Jorge Martinez (jorgemhdev)                     |")
print("--------------------------------------------------------------------------------")
print(" ")
print("Gathering video data...")

video = YouTube(sys.argv[1])
print(" ")
print("Title: ", video.title)
print("Views: ", video.views)
print("Length: ", video.length, " seconds")
print(" ")

streams = video.streams #collects only optimal streams to download

print("The following streams have been found:")
print(" ")
j = 1
for i in streams: #displays all optimal streams available to download
    print(j, " - ", i)
    j = j + 1

selection_input = int(input("What stream do should be downloaded? (1-...) "))

print("Downloading video, please wait... ")
selected = streams[selection_input - 1] #select the desired stream in the list and download it
selected.download()
print("Video downloaded successfully! Check the directory this script is in.")