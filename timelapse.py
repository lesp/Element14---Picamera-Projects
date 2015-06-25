import time
import picamera

try:
    with picamera.PiCamera() as camera:
        i = 0
        while True:
            camera.start_preview()
            time.sleep(2)
            camera.capture(str(i)+(".jpg"))
            i += 1
            time.sleep(3)
except KeyboardInterrupt:
    print("Exiting")
    
