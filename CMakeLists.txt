cmake_minimum_required(VERSION 3.5)

project(hello CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

execute_process(COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/A/preparing.py)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/B)

set_target_properties(b PROPERTIES LINKER_LANGUAGE CXX)

add_executable(hello ${CMAKE_CURRENT_SOURCE_DIR}/C/main.cpp)
