import pytube as p

# link = input('Enter the youtube video link URL:\n')

yt = p.YouTube("https://www.youtube.com/watch?v=V2EfL1j4KYE")
yt.streams.first().download()
print('downloaded', link)
