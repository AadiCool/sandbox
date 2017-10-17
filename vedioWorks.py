import cv2

def nothing(x):
    pass


cap = cv2.VideoCapture('test.mp4')
cv2.namedWindow('frame')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar('frame no', 'frame', 0, length,nothing)
c2=g=c=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if g==0:
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.setTrackbarPos('frame no','frame',c2)
    c2=c2+1
    k=cv2.waitKey(25) & 0xFF
    if  k== 27:
        break
    elif k == ord('s'):
        cv2.imwrite('image frame capture'+str(c)+'.jpg',frame)
        c=c+1
    elif k == ord('g'):
        g=1-g
    elif k == ord('p'):
        while(True):
            k2=cv2.waitKey(25)
            if k2 == ord('p'):
                break
    else: continue





cap.release()
cv2.destroyAllWindows()