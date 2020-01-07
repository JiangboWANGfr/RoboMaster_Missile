#this is the real code that has being feizhuang to lei
# Blob Detection Example
#
# This example shows off how to use the find_blobs function to find color
# blobs in the image. This example in particular looks for dark green objects.

import sensor, image, time


sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # use RGB565.#灰度图
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

class Get_Center:
    def __init__(self):
        self.max_blob = [] #save two rectangles which is using to calculate the center_center
        self.center_x = 160
        self.center_y = 120

    def find_max(blobs):
        max_size=0
        for blob in blobs:
            if blob[2]*blob[2] > max_size: #blob[2]和blob[3]表示宽高
                max_blob=blob
                max_size = blob[2]*blob[2]
        return max_blob

    def find_center_point(max_blob):
        center_x_1 = max_blob[0]+max_blob[2]/2 #the center_x of the first rectangle
        center_y_1 = max_blob[1]+max_blob[3]/2 #the center_y of the first rectangle

        return int(center_x_1),int((center_y_1))


    #this function must be test before using
    def send_message_to_DK():
        if(center_x == 0|center_y ==0)
            self.center_x , self.center_y
        else
            return center_x , center_y


    def main_function():
        pass


while(True):
    get_center = Get_Center()
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.
    print("fps",clock.fps())
    #img.to_grayscale()
    img=img.close(1) #看具体情况有没有必要
    blobs = img.find_circles(threshold = 2000)

    #if blobs:
        #if len(blobs)==2:
            #for i in range(2):
               #max_blob.append(find_max(blobs))

    center_x , center_y = get_center.find_center_point(max_blobs)

    get_center.send_massage_to_DK()

    #max_blob_1,max_blob_2 = find_max(blobs)
    x_error = max_blob[0]-img.width()/2   #横坐标
    h_error = 3.14*max_blob[2]*max_blob[2]-size_threshold  #大小误差
    print("x error: ", x_error)

    #for b in blobs:
        ## Draw a rect around the blob.
        #img.draw_rectangle(b[0:4]) # rect
        #img.draw_cross(int(b[0]+b[2]/2),int(b[1]+b[3]/2)) # cx, cy
    if (len(max_blob)==1):
        img.draw_circle(max_blob[0],max_blob[1],max_blob[3],color =(255,0,0),fill = True) # rect
        #img.draw_rectangle(max_blob[0:4]) # rect
        img.draw_cross(int(max_blob[0]),int(max_blob[1])) # cx, cy
        print("h_output",h_error)





# print("fps2",clock.fps())
