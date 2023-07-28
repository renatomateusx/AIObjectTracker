import cv2

#Tracking Video using KCF Algo. Which for speeded videos is not so good.

#creating the tracker
# tracker = cv2.TrackerKCF_create()
#Tracking Video using KCF Algo. Which for speeded videos is not so good.

tracker = cv2.TrackerCSRT_create()
#Tracking Video using CSRTF Algo. Which for speeded videos has more precision.

#preparing the video
video = cv2.VideoCapture('race.mp4')

#reading the video
ok, frame = video.read()

bbox = cv2.selectROI(frame)
#print(bbox)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break
    ok, bbox = tracker.update(frame)
    print(ok)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, "Error", (600, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: #ESCAPE
        break
