import cv2 as cv
import torch
import threading

from UI_Part.UI_Base import UI_Base

lock = threading.Lock()

def function1():
    with lock:
        # 这里用来处理图像并且输出处理的结果,以下是测试程序
        b = cv.imread("C:\\Users\\21525\\Pictures\\c602433df6d28e791b5ca2f57ceb44ca_7455375312935578669.jpg")
        cv.imshow("pic", b)
        cv.waitKey(0)
        print("This is function1!")


def function2():
    # 这里用来并行的AI算法操作，以实现分析出牌，以下是测试程序
    output = torch.rand(3, 2)
    print(output)
    print("This is function2!")


def function3():
    with lock:
        # 预留给UI的接口
        UI_object = UI_Base()
        UI_object.get_mat()
        cv.imshow("image", UI_object.image)
        cv.waitKey(0)
        print("This is function3!")


thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)
thread3 = threading.Thread(target=function3)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
