#this is the test
# Blob Detection Example
#
# This example shows off how to use the find_blobs function to find color
# blobs in the image. This example in particular looks for dark green objects.

import sensor, image, time

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QVGA) # use QQVGA for speed.
sensor.skip_frames(time = 2000) # Let new settings take affect.
#设置相机亮度
sensor.set_brightness(-3)
#设置相机自动增益
#sensor.set_auto_gain(True,0)
#关闭相机的自动曝光，设置一个固定的曝光时间
sensor.set_auto_exposure(False,15000)
clock = time.clock()                # Create a clock object to track the FPS.

size_threshold = 2000 #this is set to centoral the distance

# For color tracking to work really well you should ideally be in a very, very,
# very, controlled enviroment where the lighting is constant...

def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size: #blob[2]和blob[3]表示宽高
            max_blob=blob
            max_size = blob[2]*blob[3]
    temp = max_blob
    blobs.remove(max_blob)
    return temp

while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.
    print("fps",clock.fps())
    #img.to_grayscale()
    b=img.close(1)
    blobs = img.find_rects(threshold = 10000)

    max_blob = []
    if blobs:
        if len(blobs)==1:
            max_blob.append(find_max(blobs))
        else:
            for i in range(2):
               max_blob.append(find_max(blobs))

        #max_blob_1,max_blob_2 = find_max(blobs)
        x_error = max_blob[0][0]+max_blob[0][2]/2-img.width()/2   #横坐标
        h_error = max_blob[0][2]*max_blob[0][3]-size_threshold  #大小误差
        print("x error: ", x_error)

        #for b in blobs:
            ## Draw a rect around the blob.
            #img.draw_rectangle(b[0:4]) # rect
            #img.draw_cross(int(b[0]+b[2]/2),int(b[1]+b[3]/2)) # cx, cy
    if (len(max_blob)==2):
        img.draw_rectangle(max_blob[0][0:4]) # rect
        img.draw_rectangle(max_blob[1][0:4]) # rect
        img.draw_cross(int(max_blob[0][0]+max_blob[0][2]/2),int(max_blob[0][1]+max_blob[0][3]/2)) # cx, cy
        print("h_output",h_error)





# print("fps2",clock.fps())
