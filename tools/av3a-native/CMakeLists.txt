cmake_minimum_required(VERSION 3.21 FATAL_ERROR)

project(FongMiDirectAv3aJNI C CXX)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

foreach(required VIVID_DIR MEDIA3_DIR)
    if(NOT DEFINED ${required})
        message(FATAL_ERROR "${required} is required")
    endif()
endforeach()

set(AV3A_DECODER "${VIVID_DIR}/av3adecoder")
file(GLOB AV3A_DECODER_SOURCES CONFIGURE_DEPENDS
    "${AV3A_DECODER}/avs3Decoder/src/*.c"
    "${AV3A_DECODER}/libavs3_common/*.c"
    "${AV3A_DECODER}/libavs3_debug/*.c")

add_library(av3a_core OBJECT ${AV3A_DECODER_SOURCES})
target_compile_options(av3a_core PRIVATE -O3 -fsigned-char -fno-strict-aliasing)
target_compile_definitions(av3a_core PRIVATE ANDROID)
if(ANDROID_ABI STREQUAL "arm64-v8a")
    target_compile_definitions(av3a_core PRIVATE SUPPORT_NEON)
endif()
target_include_directories(av3a_core PRIVATE
    "${AV3A_DECODER}/avs3Decoder/include"
    "${AV3A_DECODER}/libavs3_common"
    "${AV3A_DECODER}/libavs3_debug")

add_library(av3aJNI SHARED
    "${MEDIA3_DIR}/libraries/decoder_av3a/src/main/jni/av3a_jni.cc"
    $<TARGET_OBJECTS:av3a_core>)
target_include_directories(av3aJNI PRIVATE
    "${AV3A_DECODER}/avs3Decoder/include"
    "${AV3A_DECODER}/libavs3_common"
    "${AV3A_DECODER}/libavs3_debug")
target_link_libraries(av3aJNI PRIVATE log m dl)
target_link_options(av3aJNI PRIVATE
    "-Wl,-z,max-page-size=16384"
    "-Wl,--no-undefined")
