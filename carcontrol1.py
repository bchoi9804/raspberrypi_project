import cv2
import uart

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
    
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        
        if keyValue == ord('q'):
            break
        elif keyValue == 82:
            print("go")
            carState = "go"
            uart.uart('w')
        elif keyValue == 84:
            print("stop")
            carState = "stop"
            uart.uart('s')
        elif keyValue == 81:
            print("left")
            carState = "left"
            uart.uart('l')
        elif keyValue == 83:
            print("right")
            carState = "right"
            uart.uart('r')
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()