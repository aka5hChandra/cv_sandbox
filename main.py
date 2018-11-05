import cv2

img =  cv2.imread('./savedImages/temp.jpg')
def vedioStream():
    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
        if cv2.waitKey(1) & 0xFF == ord(' ') :
            cv2.imwrite('./savedImages/temp.jpg',frame)
    cap.release()
    cv2.destroyAllWindows()

def getPoints(event, x,y, flag, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        print ((x,y))
    
      

    
  

def main():
    #vedioStream()
    #img = cv2.imread('./savedImages/temp.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',getPoints)
    while (True):
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    cv2.destroyAllWindows()
 
main()
