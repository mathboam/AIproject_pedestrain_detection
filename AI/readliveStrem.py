import cv2 as cv
import datetime
import face_recognition as fr

capture = cv.VideoCapture(0)
date_time = str(datetime.datetime.now())
text = 'timestamp: ' + date_time

width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)

capture.set(3, int(width/2))
capture.set(4, int(height/2))
#
# print(capture.get(3))
# print(capture.get(4))

# 1280.0
# 720.0

# fourcc = cv.VideoWriter.fourcc(*'XVID')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

# initialize variables
faceLocations = []
# output = cv.VideoWriter('./Assets/recordings.avi', fourcc, 30, (int(width), int(height)), True)
while capture.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # recognize frames
    # rgb_frame = frame1[:, :, ::-1]

    # get locations of faces in the current frame of video
    # faceLocations = fr.face_locations(rgb_frame)

    # for top, right, bottom, left in faceLocations:
    #     cv.rectangle(frame1, (left, top), (right, bottom), (0, 0, 255), 2)


    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 500:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, text, (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    # output.write(frame)
    # font = cv.FONT_HERSHEY_COMPLEX_SMALL
    # text = 'Width: ' + str(width) + ' Height: ' + str(height)
    #
    #
    # frame = cv.putText(frame, date_time, (233, 333), font, 1, (0, 255, 255), 2, cv.LINE_AA)
    if ret:
        cv.imshow('feed', frame1)
        frame1 = frame2
        ret, frame2 = capture.read()



    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release();
# output.release()
cv.destroyAllWindows();