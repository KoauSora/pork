//经过我的慎重考虑决定还是使用多线程来完成这次的代码，请大家自学这方面的内容，如果遇到兼容性的问题日后讨论
#include <iostream>
#include <vector>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <thread>
#include <torch/torch.h>
#include <torch/script.h>
using namespace std;
using namespace cv;
void function1(){
    Mat b;
    b = imread("C:\\Users\\21525\\Desktop\\project_pork_vision\\62ccc74927a81e952449a926a4e72491_2288382312505991075.png",IMREAD_COLOR);
    imshow("pic",b);
//    waitKey(0);
    cout << "this is function1!";
}
void function2(){
    torch::Tensor output = torch::randn({3,2});
    std::cout << output;
    cout << "this is function2!";
}
int main() {
    thread mythread(function1);
    mythread.join();
    thread mythread2(function2);
    mythread2.join();
    std::cout << "hello!";
    return 0;
}