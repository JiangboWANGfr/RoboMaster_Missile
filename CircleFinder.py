#this is the real code that has being feizhuang to lei
# Blob Detection Example
#
# This example shows off how to use the find_blobs function to find color
# blobs in the image. This example in particular looks for dark green objects.

import sensor, image, time


sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.YUV422) # use RGB565.#灰度图
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(time = 2000) # Let new settings take affect.
#设置相机亮度
sensor.set_brightness(-3)
#设置相机自动增益
sensor.set_auto_gain(False)
#关闭相机的自动曝光，设置一个固定的曝光时间
sensor.set_auto_exposure(False,15000)
sensor.set_auto_whitebal(False)
clock = time.clock()                # Create a clock object to track the FPS.

size_threshold = 2000 #this is set to centoral the distance

# For color tracking to work really well you should ideally be in a very, very,
# very, controlled enviroment where the lighting is constant...

class Get_Center():
    def __init__(self):
        self.max_blob = [] #save two rectangles which is using to calculate the center_center
        self.center_x = 160
        self.center_y = 120

    def find_max(blobs):
        max_size=0
        for blob in blobs:
            if blob[2]*blob[3] > max_size: #blob[2]和blob[3]表示宽高
                max_blob=blob
                max_size = blob[2]*blob[3]
        return max_blob

    def find_center_point(max_blob):
        center_x_1 = max_blob[0]+max_blob[2]/2 #the center_x of the first rectangle
        center_y_1 = max_blob[1]+max_blob[3]/2 #the center_y of the first rectangle

        return (int(center_x_1),int(center_y_1))


    #this function must be test before using
    def send_message_to_DK():
        return center_x , center_y

    def main_function():
        pass

def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size: #blob[2]和blob[3]表示宽高
            max_blob=blob
            max_size = blob[2]*blob[3]
    temp = max_blob
    blobs.remove(max_blob)
    return temp

def find_center_point(max_blob):
    center_x_1 = max_blob[0]+max_blob[2]/2 #the center_x of the first rectangle
    center_y_1 = max_blob[1]+max_blob[3]/2 #the center_y of the first rectangle

    return (int(center_x_1),int(center_y_1))



while(True):
    get_center = Get_Center()
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot().lens_corr(1.8)
    print("fps",clock.fps())
    blobs = []
    #img.to_grayscale()
    img=img.close(1) #看具体情况有没有必要
    for c in img.find_circles(threshold = 3500, x_margin = 10, y_margin = 10, r_margin = 10,
            r_min = 2, r_max = 100, r_step = 2):
        area = (c.x()-c.r(), c.y()-c.r(), 2*c.r(), 2*c.r())
                #area为识别到的圆的区域，即圆的外接矩形框
        statistics = img.get_statistics(roi=area)#像素颜色统计
        print(statistics)
        if 0<statistics.l_mode()<100 and 0<statistics.a_mode()<127 and 0<statistics.b_mode()<127:#if the circle is red#设置颜色阈值
            blobs.append(c)
            img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))#识别到的红色圆形用红色的圆框出来
        else:
            img.draw_rectangle(area, color = (255, 255, 255))
        max_blob = find_max(blobs)
        (center_x , center_y) = find_center_point(max_blob)

        #get_center.send_massage_to_DK()
        print("center_x",center_x)
        print("center_y",center_y)

        x_error = max_blob[0]+max_blob[2]/2-img.width()/2   #横坐标
        h_error = max_blob[2]*max_blob[3]-size_threshold  #大小误差
        print("x error: ", x_error)

        #for b in blobs:
            ## Draw a rect around the blob.
            #img.draw_rectangle(b[0:4]) # rect
            #img.draw_cross(int(b[0]+b[2]/2),int(b[1]+b[3]/2)) # cx, cy
        #if (len(max_blob)==1):
        img.draw_rectangle(max_blob[0:4],color= (0,255,0),thickness = 2,fill = False) # rect
        #img.draw_rectangle(max_blob[                                                                        0:4]) # rect
        img.draw_cross(int(max_blob[0]+max_blob[2]/2),int(max_blob[1]+max_blob[3]/2)) # cx, cy
        print("h_output",h_error)


        print("fps2",clock.fps())

