import sensor,image,time
sensor.reset()
sensor.reset()  # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565)  # use RGB565.#灰度图
sensor.set_framesize(sensor.QVGA)  # use QVGA for speed.
sensor.skip_frames(time=2000)  # Let new settings take affect.
# 设置相机自动增益
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
##设置相机亮度
# sensor.set_brightness(-3)
##关闭相机的自动曝光，设置一个固定的曝光时间
# sensor.set_auto_exposure(False,15000)
clock = time.clock()  # Create a clock object to track the FPS.
colorThreshould = (96, 100, -21, 7, -8, 6)
DEBUG = 1

class MissileCenter:
    def __init__(self):
        #self.circles = []  # save circles in the picture
        self.center_x = 160
        self.center_y = 120


    def find_MaxCircle(self,circles):
        max_size = 0
        for circle in circles:
            if circle[2] * circle[3] > max_size:#blob[2]和blob[3]表示宽高
                Max_blob = circle
                max_size = circle[2] * circle[3]
                print("ddd")
        return Max_blob

    def get_Missile_Center(self, max_circle):
        self.center_x = max_circle.cx()
        self.center_y = max_circle.cy()

    # this function must be test before using
    def send_Message_to_DK(self):
        if DEBUG :
            print("self.center_x",self.center_x)
            print("self.center_y",self.center_y)
        #return self.center_x,self.center_y

    def image_Detection(self,img):
        # img.to_grayscale()
        # img.gaussian(1,threshold=True,invert =True )
        img.binary([colorThreshould])
        img = img.close(1)  # 看具体情况有没有必要
        circles = []
        if DEBUG:
            for c in img.find_blobs([colorThreshould]):
                area = (c.x(), c.y(), c.w(), c.h())
                print(c.w() * c.h())
                if 350 < c.w() * c.h() < 600:
                    circles.append(c)
                    img.draw_rectangle(c[0:4], color=(255, 0, 0), thickness=2, fill=False)

                # area为识别到的矩形的区域
            # statistics = img.get_statistics(roi=area)#像素颜色统计
            # print(statistics)
            # if 87 < statistics.l_mode() < 100 and -6 < statistics.a_mode() < 21 and -7 < statistics.b_mode() < 11:  # if the circle is red#设置颜色阈值
            #     blobs.append(c)
            #     print("append c")
            #     img.draw_rectangle(c.x(), c.y(), c.w(), c.h(), color=(255, 255, 255))  # 识别到的绿色圆形用红色的圆框出来
            #     print("lenlenlenlnelnellenenlenelelen", len(blobs))
        return circles

def main():
    while(True):
        missileCenter = MissileCenter()
        clock.tick()  # Track elapsed milliseconds between snapshots().
        img = sensor.snapshot()  # Take a picture and return the image.
        print("fps", clock.fps())

        circles =  missileCenter.image_Detection(img)
        print(circles)
        if circles:
            max_circle = missileCenter.find_MaxCircle(circles)
            print("ok")
            if max_circle:
                missileCenter.get_Missile_Center(max_circle)
        missileCenter.send_Message_to_DK()

if __name__ == "__main__":
    main()

















