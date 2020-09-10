import cv2


class RandomGenerator(object):
    def __init__(self):
        pass
    
    def random(self):
        pass
    
    def randint(self):
        pass


class CameraRandom(RandomGenerator):
    def __init__(self):
        self.cap = cv2.VideoCapture(1)
    
    def random(self):
        ret, frame = self.cap.read()
        if ret:
            return frame.sum() % 10
    
    def exit(self):
        self.cap.release()


if __name__ == '__main__':
    cr = CameraRandom()
    for i in range(10):
        print(cr.random())