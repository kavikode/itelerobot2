#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/user/simulation_ws/src/perception_object_detection/dodo_detector_ros"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/user/simulation_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/user/simulation_ws/install/lib/python3/dist-packages:/home/user/simulation_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/user/simulation_ws/build" \
    "/usr/bin/python3" \
    "/home/user/simulation_ws/src/perception_object_detection/dodo_detector_ros/setup.py" \
     \
    build --build-base "/home/user/simulation_ws/build/perception_object_detection/dodo_detector_ros" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/user/simulation_ws/install" --install-scripts="/home/user/simulation_ws/install/bin"
