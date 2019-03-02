cmake_minimum_required(VERSION 2.8)

project(hello_cmake)

enable_language(CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

execute_process(COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/A/preparing.py)

set(SOURCES_LIST ${CMAKE_CURRENT_SOURCE_DIR}/C/main.cpp ${CMAKE_CURRENT_SOURCE_DIR}/C/main.h)

#include(${CMAKE_CURRENT_SOURCE_DIR}/A/index.h)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/B)

set_target_properties(hello_lib PROPERTIES LINKER_LANGUAGE CXX)

add_executable(hello_cmake ${SOURCES_LIST})

target_link_libraries(hello_cmake hello_lib)
