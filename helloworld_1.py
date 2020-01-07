# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd

lcd.init(freq=15000000)
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
#设置相机亮度
sensor.set_brightness(-3)
#设置相机自动增益
#sensor.set_auto_gain(False,0)
#关闭相机的自动曝光，设置一个固定的曝光时间
sensor.set_auto_exposure(False,15000)
clock = time.clock()                # Create a clock object to track the FPS.

green_threshold   = (76, 96, -110, -30, 8, 66)
size_threshold = 2000

def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob


while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()        # Take a picture and return the image.              # Display on LCD
    #img.binary([(150,250)])
    #膨胀两个像素，性能下降的很快
    #img.erode(1)
   # img.close(1)
    #img.top_hat(1)
    #img.black_hat(1)
    #print(img.width())
    #print("gain",sensor.get_gain_db())
    #print("曝光时间",sensor.get_exposure_us())
    #Rects=img.find_rects()
    #for Rect in Rects:
    #img.draw_rectangle(Rect.rect(),color = (0,0,255))



























    print("帧率",clock.fps())
