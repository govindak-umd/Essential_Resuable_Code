video_file = cv2.VideoCapture('laferrari.mp4')
if (video_file.isOpened() == False):
    print('Please check the file name again!')
#video writing
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
cam_out = cv2.VideoWriter('ContouredRed.mp4',0x7634706d, 5.0, (1280,720))
while(video_file.isOpened()):
    ret,frame = video_file.read()
    print('hey')
