cmake_minimum_required(VERSION 2.8)

project(hello_lib)

enable_language(CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

add_library(hello_lib lib.h)
