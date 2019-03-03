add_library(b "")

target_sources(
    b
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/lib.h
)

target_include_directories(
    b
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}
)
