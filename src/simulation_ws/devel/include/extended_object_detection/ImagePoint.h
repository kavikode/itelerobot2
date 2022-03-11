// Generated by gencpp from file extended_object_detection/ImagePoint.msg
// DO NOT EDIT!


#ifndef EXTENDED_OBJECT_DETECTION_MESSAGE_IMAGEPOINT_H
#define EXTENDED_OBJECT_DETECTION_MESSAGE_IMAGEPOINT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace extended_object_detection
{
template <class ContainerAllocator>
struct ImagePoint_
{
  typedef ImagePoint_<ContainerAllocator> Type;

  ImagePoint_()
    : x(0)
    , y(0)  {
    }
  ImagePoint_(const ContainerAllocator& _alloc)
    : x(0)
    , y(0)  {
  (void)_alloc;
    }



   typedef int32_t _x_type;
  _x_type x;

   typedef int32_t _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::extended_object_detection::ImagePoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::extended_object_detection::ImagePoint_<ContainerAllocator> const> ConstPtr;

}; // struct ImagePoint_

typedef ::extended_object_detection::ImagePoint_<std::allocator<void> > ImagePoint;

typedef boost::shared_ptr< ::extended_object_detection::ImagePoint > ImagePointPtr;
typedef boost::shared_ptr< ::extended_object_detection::ImagePoint const> ImagePointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::extended_object_detection::ImagePoint_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::extended_object_detection::ImagePoint_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::extended_object_detection::ImagePoint_<ContainerAllocator1> & lhs, const ::extended_object_detection::ImagePoint_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::extended_object_detection::ImagePoint_<ContainerAllocator1> & lhs, const ::extended_object_detection::ImagePoint_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace extended_object_detection

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::extended_object_detection::ImagePoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::extended_object_detection::ImagePoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::extended_object_detection::ImagePoint_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bd7b43fd41d4c47bf5c703cc7d016709";
  }

  static const char* value(const ::extended_object_detection::ImagePoint_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbd7b43fd41d4c47bULL;
  static const uint64_t static_value2 = 0xf5c703cc7d016709ULL;
};

template<class ContainerAllocator>
struct DataType< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "extended_object_detection/ImagePoint";
  }

  static const char* value(const ::extended_object_detection::ImagePoint_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 x\n"
"int32 y\n"
;
  }

  static const char* value(const ::extended_object_detection::ImagePoint_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ImagePoint_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::extended_object_detection::ImagePoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::extended_object_detection::ImagePoint_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<int32_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<int32_t>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EXTENDED_OBJECT_DETECTION_MESSAGE_IMAGEPOINT_H