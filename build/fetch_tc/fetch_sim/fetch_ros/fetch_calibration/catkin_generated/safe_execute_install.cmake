execute_process(COMMAND "/home/kavihost/catkin_ws/build/fetch_tc/fetch_sim/fetch_ros/fetch_calibration/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/kavihost/catkin_ws/build/fetch_tc/fetch_sim/fetch_ros/fetch_calibration/catkin_generated/python_distutils_install.sh) returned error code ")
endif()