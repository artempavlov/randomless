import numpy as np
import cv2
import 

class RandomGenerator(object):
    def __init__(self):
        pass
    
    def random(self):
        pass
    
    def randint(self):
        pass


class CameraRandom(RandomGenerator):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        
        #while(True):
            # Capture frame-by-frame
        #    ret, frame = cap.read()
        
            # Our operations on the frame come here
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # Display the resulting frame
        #    cv2.imshow('frame',gray)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        
        # When everything done, release the capture
        #cap.release()
        #cv2.destroyAllWindows()
    
    def random(self):
        ret, frame = self.cap.read()
        if ret:
            return frame[0][0][0] / 255


if __name__ == '__main__':
    cr = CameraRandom()
    for i in range(10):
        print(cr.random())