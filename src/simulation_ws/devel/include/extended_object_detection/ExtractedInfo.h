// Generated by gencpp from file extended_object_detection/ExtractedInfo.msg
// DO NOT EDIT!


#ifndef EXTENDED_OBJECT_DETECTION_MESSAGE_EXTRACTEDINFO_H
#define EXTENDED_OBJECT_DETECTION_MESSAGE_EXTRACTEDINFO_H


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
struct ExtractedInfo_
{
  typedef ExtractedInfo_<ContainerAllocator> Type;

  ExtractedInfo_()
    : sub_id(0)
    , text()  {
    }
  ExtractedInfo_(const ContainerAllocator& _alloc)
    : sub_id(0)
    , text(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _sub_id_type;
  _sub_id_type sub_id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _text_type;
  _text_type text;





  typedef boost::shared_ptr< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> const> ConstPtr;

}; // struct ExtractedInfo_

typedef ::extended_object_detection::ExtractedInfo_<std::allocator<void> > ExtractedInfo;

typedef boost::shared_ptr< ::extended_object_detection::ExtractedInfo > ExtractedInfoPtr;
typedef boost::shared_ptr< ::extended_object_detection::ExtractedInfo const> ExtractedInfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::extended_object_detection::ExtractedInfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::extended_object_detection::ExtractedInfo_<ContainerAllocator1> & lhs, const ::extended_object_detection::ExtractedInfo_<ContainerAllocator2> & rhs)
{
  return lhs.sub_id == rhs.sub_id &&
    lhs.text == rhs.text;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::extended_object_detection::ExtractedInfo_<ContainerAllocator1> & lhs, const ::extended_object_detection::ExtractedInfo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace extended_object_detection

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "185b73de2075ebcbf80e7c87c570695a";
  }

  static const char* value(const ::extended_object_detection::ExtractedInfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x185b73de2075ebcbULL;
  static const uint64_t static_value2 = 0xf80e7c87c570695aULL;
};

template<class ContainerAllocator>
struct DataType< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "extended_object_detection/ExtractedInfo";
  }

  static const char* value(const ::extended_object_detection::ExtractedInfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 sub_id\n"
"string text\n"
;
  }

  static const char* value(const ::extended_object_detection::ExtractedInfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sub_id);
      stream.next(m.text);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ExtractedInfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::extended_object_detection::ExtractedInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::extended_object_detection::ExtractedInfo_<ContainerAllocator>& v)
  {
    s << indent << "sub_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.sub_id);
    s << indent << "text: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.text);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EXTENDED_OBJECT_DETECTION_MESSAGE_EXTRACTEDINFO_H
