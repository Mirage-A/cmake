project(hello_world)

set(SOURCE_EXE C/main.cpp)

set(SOURCE_LIB B/lib.h)

add_library(foo STATIC ${SOURCE_LIB})

add_executable(main ${SOURCE_EXE})

target_link_libraries(main foo)