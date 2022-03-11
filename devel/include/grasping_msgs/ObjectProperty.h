// Generated by gencpp from file grasping_msgs/ObjectProperty.msg
// DO NOT EDIT!


#ifndef GRASPING_MSGS_MESSAGE_OBJECTPROPERTY_H
#define GRASPING_MSGS_MESSAGE_OBJECTPROPERTY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace grasping_msgs
{
template <class ContainerAllocator>
struct ObjectProperty_
{
  typedef ObjectProperty_<ContainerAllocator> Type;

  ObjectProperty_()
    : name()
    , value()  {
    }
  ObjectProperty_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , value(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _value_type;
  _value_type value;





  typedef boost::shared_ptr< ::grasping_msgs::ObjectProperty_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::grasping_msgs::ObjectProperty_<ContainerAllocator> const> ConstPtr;

}; // struct ObjectProperty_

typedef ::grasping_msgs::ObjectProperty_<std::allocator<void> > ObjectProperty;

typedef boost::shared_ptr< ::grasping_msgs::ObjectProperty > ObjectPropertyPtr;
typedef boost::shared_ptr< ::grasping_msgs::ObjectProperty const> ObjectPropertyConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::grasping_msgs::ObjectProperty_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::grasping_msgs::ObjectProperty_<ContainerAllocator1> & lhs, const ::grasping_msgs::ObjectProperty_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.value == rhs.value;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::grasping_msgs::ObjectProperty_<ContainerAllocator1> & lhs, const ::grasping_msgs::ObjectProperty_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace grasping_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::grasping_msgs::ObjectProperty_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::grasping_msgs::ObjectProperty_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::grasping_msgs::ObjectProperty_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc6ccc4a57f61779c8eaae61e9f422e0";
  }

  static const char* value(const ::grasping_msgs::ObjectProperty_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc6ccc4a57f61779ULL;
  static const uint64_t static_value2 = 0xc8eaae61e9f422e0ULL;
};

template<class ContainerAllocator>
struct DataType< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "grasping_msgs/ObjectProperty";
  }

  static const char* value(const ::grasping_msgs::ObjectProperty_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "###########################################################\n"
"# Other generic properties of an object\n"
"string name\n"
"string value\n"
;
  }

  static const char* value(const ::grasping_msgs::ObjectProperty_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ObjectProperty_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::grasping_msgs::ObjectProperty_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::grasping_msgs::ObjectProperty_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "value: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPING_MSGS_MESSAGE_OBJECTPROPERTY_H