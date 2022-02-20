import cv2

videoCapture = cv2.VideoCapture()
videoCapture.open('/home/smile/视频/77第三次培训.mp4')#更改本地视频

#fps = videoCapture.get(cv2.CAP_PROP_FPS)
fps = 10
#frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
frames = 1000
# fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=", fps, "frames=", frames)

for i in range(int(frames)):
    ret, frame = videoCapture.read()
    cv2.imwrite("sunminglei%d.jpg" % i, frame)
