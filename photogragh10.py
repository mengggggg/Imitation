#!/usr/bin/env python3
# 引入 PiCamera 包
from picamera import PiCamera
from time import sleep

camera = PiCamera()               # 创建 Camera 对象
camera.saturation = 80            # 设置图像的饱和度
camera.brightness = 50            # 设置图像的亮度(50 表示白平衡的状态)
camera.shutter_speed = 6000000   # 相机快门速度
camera.iso = 800                  # 设置图像的 ISO
camera.sharpness = 0              # 设置图像的锐度值
camera.hflip = True               # 是否进行水平翻转
camera.vflip = False              # 是否进行垂直翻转
camera.rotation = 0               # 设置图像旋转角度
camera.resolution = (1920, 1080) # 设置图像分辨率 

# 拍摄图片
for i in range(10):
	sleep(0.1)
	camera.capture('image%s.jpg' % i)
