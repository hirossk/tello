from time import sleep
import tellopy
import cv2
import av
import numpy

def handler(event, sender, data, **args):
    drone = sender
    #if event is drone.EVENT_FLIGHT_DATA:
    #    print(data)

def test():
    drone = tellopy.Tello()
    print("========\nTelloへの接続を開始します。（60秒間tryし続けます）\n========")
    drone.connect()
    drone.wait_for_connection(60.0)

    print("========離陸します。========")
    drone.takeoff()
    print("========3秒時間を置きます。========")
    sleep(3)
    print("========時計回りに90度回転します。========")
    drone.clockwise(90)
    sleep(10)
    print("========着陸します。========")
    drone.land()
    print("========3秒時間を置きます。========")
    sleep(3)
    print("========drone.subscribe()します。========")
    drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
    print("========30droneインスタンスをquit()します。========")
    drone.quit()

if __name__ == '__main__':
    test()
