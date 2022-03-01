# Install script for directory: /home/user/simulation_ws/src/perception_object_detection/extended_object_detection

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/user/simulation_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection/msg" TYPE FILE FILES
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/ImagePoint.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/Rect.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/Track.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/ExtractedInfo.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/Contour.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/SimpleObject.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/SimpleObjectArray.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/ComplexObject.msg"
    "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/msg/ComplexObjectArray.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection/srv" TYPE FILE FILES "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/srv/SetSimpleObjects.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection/cmake" TYPE FILE FILES "/home/user/simulation_ws/build/perception_object_detection/extended_object_detection/catkin_generated/installspace/extended_object_detection-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/include/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/roseus/ros/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/common-lisp/ros/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/gennodejs/ros/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/user/simulation_ws/devel/lib/python3/dist-packages/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/lib/python3/dist-packages/extended_object_detection")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/user/simulation_ws/build/perception_object_detection/extended_object_detection/catkin_generated/installspace/extended_object_detection.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection/cmake" TYPE FILE FILES "/home/user/simulation_ws/build/perception_object_detection/extended_object_detection/catkin_generated/installspace/extended_object_detection-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection/cmake" TYPE FILE FILES
    "/home/user/simulation_ws/build/perception_object_detection/extended_object_detection/catkin_generated/installspace/extended_object_detectionConfig.cmake"
    "/home/user/simulation_ws/build/perception_object_detection/extended_object_detection/catkin_generated/installspace/extended_object_detectionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/extended_object_detection" TYPE FILE FILES "/home/user/simulation_ws/src/perception_object_detection/extended_object_detection/package.xml")
endif()

