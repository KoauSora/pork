cmake_minimum_required(VERSION 3.26)

project(pork_vision)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_PREFIX_PATH D:\\Pytorch\\CPU\\libtorch)

set(Torch_DIR "D:\\Pytorch\\CPU\\libtorch\\share\\cmake\\Torch")
set(OpenCV_DIR "D:\\OpenCV\\build")

include_directories(D:\\OpenCV\\build\\include)
include_directories(D:\\OpenCV\\build\\x64\\vc16\\bin)
include_directories(D:\\OpenCV\\build)
include_directories(
        UI_part
        vision_parts
        AI_part
)

find_package(Torch REQUIRED)
find_package(OpenCV REQUIRED)

add_executable(pork_vision main.cpp
        vision_parts/recognize_part.cpp
        vision_parts/recognize_part.h
        UI_part/UI_widgets.cpp
        UI_part/UI_widgets.h
        UI_part/UI_VirtualBase.cpp
        UI_part/UI_VirtualBase.h
        vision_parts/recognize_part_VirtualBase.cpp
        vision_parts/recognize_part_VirtualBase.h
        AI_part/AI_part_VirtualBase.cpp
        AI_part/AI_part_VirtualBase.h
        vision_parts/study_part.cpp
        vision_parts/study_part.h
        vision_parts/study_part_VirtualBase.cpp
        vision_parts/study_part_VirtualBase.h
        UI_part/Mat_list.cpp
        UI_part/Mat_list.h
        AI_part/AL_part.cpp
        AI_part/AL_part.h
        vision_parts/pytorch_deepstudy.cpp
        vision_parts/pytorch_deepstudy.h
)

target_link_libraries(pork_vision ${TORCH_LIBRARIES})
target_link_libraries(pork_vision D:\\OpenCV\\build\\x64\\vc16\\lib\\opencv_world480d.lib)
target_link_libraries(pork_vision D:\\OpenCV\\build\\x64\\vc16\\lib\\opencv_world480.lib)

set_property(TARGET pork_vision PROPERTY CXX_STANDARD 17)
