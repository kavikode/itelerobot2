# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from extended_object_detection/ComplexObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import extended_object_detection.msg
import geometry_msgs.msg

class ComplexObject(genpy.Message):
  _md5sum = "3993aebfee64aed740beacfc2837e451"
  _type = "extended_object_detection/ComplexObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 type_id                                       # id of object type, according to ObjectBase
string type_name                                    # name of object type, according to ObjectBase

float64 score                                       # confidence coefficient of current result
extended_object_detection/Rect rect                 # object frames on image and 3d coordinates
geometry_msgs/Transform transform                   # transform to object center in meters, if z=1 distance is unknow, only direction
extended_object_detection/SimpleObject[] objects    # set of simple objects form current complex

================================================================================
MSG: extended_object_detection/Rect
extended_object_detection/ImagePoint left_bottom
extended_object_detection/ImagePoint right_up
geometry_msgs/Vector3[] cornerTranslates    # translate to rect corners, from bottom left in clock-wice direction, if z value is 1, it means that it is unit vector in homogeneous coordnates 


================================================================================
MSG: extended_object_detection/ImagePoint
int32 x
int32 y

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: extended_object_detection/SimpleObject
# object info
int32 type_id                               # id of type, corresponded to object base
string type_name                            # name of type, corresponded to object base
float64 score                               # confidence coefficient of current result
extended_object_detection/ExtractedInfo[] extracted_info

# object position and geometry
geometry_msgs/Transform transform           # transform to object center
extended_object_detection/Rect rect         # object frames on image and 3d coordinates
extended_object_detection/Contour contour   # contour image and 3d info

# tracking
extended_object_detection/Track track       # information about tracking if it is enabled





================================================================================
MSG: extended_object_detection/ExtractedInfo
int32 sub_id
string text

================================================================================
MSG: extended_object_detection/Contour
extended_object_detection/ImagePoint[] image_points   # points on image
geometry_msgs/Vector3[] contourTranslates             # translations to contour points

================================================================================
MSG: extended_object_detection/Track
uint8 DETECTED = 1  # Current result is obtained by detector
uint8 TRACKED = 2  # Current result is obtained by opencv tracker
uint8 LOST = 3      # Failed to obtain result, this is last saved

int32 id            # track unique id (in group of one object)
uint8 status        # status described above
#extended_object_detection/ImagePoint[] image_point_history
#geometry_msgs/Transform[] transform_history
"""
  __slots__ = ['type_id','type_name','score','rect','transform','objects']
  _slot_types = ['int32','string','float64','extended_object_detection/Rect','geometry_msgs/Transform','extended_object_detection/SimpleObject[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type_id,type_name,score,rect,transform,objects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ComplexObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.type_id is None:
        self.type_id = 0
      if self.type_name is None:
        self.type_name = ''
      if self.score is None:
        self.score = 0.
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.objects is None:
        self.objects = []
    else:
      self.type_id = 0
      self.type_name = ''
      self.score = 0.
      self.rect = extended_object_detection.msg.Rect()
      self.transform = geometry_msgs.msg.Transform()
      self.objects = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.type_id
      buff.write(_get_struct_i().pack(_x))
      _x = self.type_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d4i().pack(_x.score, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y))
      length = len(self.rect.cornerTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.rect.cornerTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_7d().pack(_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w))
      length = len(self.objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects:
        _x = val1.type_id
        buff.write(_get_struct_i().pack(_x))
        _x = val1.type_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.score
        buff.write(_get_struct_d().pack(_x))
        length = len(val1.extracted_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.extracted_info:
          _x = val2.sub_id
          buff.write(_get_struct_i().pack(_x))
          _x = val2.text
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v1 = val1.transform
        _v2 = _v1.translation
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v3 = _v1.rotation
        _x = _v3
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v4 = val1.rect
        _v5 = _v4.left_bottom
        _x = _v5
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
        _v6 = _v4.right_up
        _x = _v6
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
        length = len(_v4.cornerTranslates)
        buff.write(_struct_I.pack(length))
        for val3 in _v4.cornerTranslates:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v7 = val1.contour
        length = len(_v7.image_points)
        buff.write(_struct_I.pack(length))
        for val3 in _v7.image_points:
          _x = val3
          buff.write(_get_struct_2i().pack(_x.x, _x.y))
        length = len(_v7.contourTranslates)
        buff.write(_struct_I.pack(length))
        for val3 in _v7.contourTranslates:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.track
        _x = _v8
        buff.write(_get_struct_iB().pack(_x.id, _x.status))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.objects is None:
        self.objects = None
      end = 0
      start = end
      end += 4
      (self.type_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type_name = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.score, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y,) = _get_struct_d4i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rect.cornerTranslates = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.rect.cornerTranslates.append(val1)
      _x = self
      start = end
      end += 56
      (_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.objects = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.SimpleObject()
        start = end
        end += 4
        (val1.type_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type_name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.type_name = str[start:end]
        start = end
        end += 8
        (val1.score,) = _get_struct_d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.extracted_info = []
        for i in range(0, length):
          val2 = extended_object_detection.msg.ExtractedInfo()
          start = end
          end += 4
          (val2.sub_id,) = _get_struct_i().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.text = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.text = str[start:end]
          val1.extracted_info.append(val2)
        _v9 = val1.transform
        _v10 = _v9.translation
        _x = _v10
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v11 = _v9.rotation
        _x = _v11
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v12 = val1.rect
        _v13 = _v12.left_bottom
        _x = _v13
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        _v14 = _v12.right_up
        _x = _v14
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v12.cornerTranslates = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Vector3()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v12.cornerTranslates.append(val3)
        _v15 = val1.contour
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v15.image_points = []
        for i in range(0, length):
          val3 = extended_object_detection.msg.ImagePoint()
          _x = val3
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
          _v15.image_points.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v15.contourTranslates = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Vector3()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v15.contourTranslates.append(val3)
        _v16 = val1.track
        _x = _v16
        start = end
        end += 5
        (_x.id, _x.status,) = _get_struct_iB().unpack(str[start:end])
        self.objects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.type_id
      buff.write(_get_struct_i().pack(_x))
      _x = self.type_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d4i().pack(_x.score, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y))
      length = len(self.rect.cornerTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.rect.cornerTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_7d().pack(_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w))
      length = len(self.objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects:
        _x = val1.type_id
        buff.write(_get_struct_i().pack(_x))
        _x = val1.type_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.score
        buff.write(_get_struct_d().pack(_x))
        length = len(val1.extracted_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.extracted_info:
          _x = val2.sub_id
          buff.write(_get_struct_i().pack(_x))
          _x = val2.text
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v17 = val1.transform
        _v18 = _v17.translation
        _x = _v18
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v19 = _v17.rotation
        _x = _v19
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v20 = val1.rect
        _v21 = _v20.left_bottom
        _x = _v21
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
        _v22 = _v20.right_up
        _x = _v22
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
        length = len(_v20.cornerTranslates)
        buff.write(_struct_I.pack(length))
        for val3 in _v20.cornerTranslates:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v23 = val1.contour
        length = len(_v23.image_points)
        buff.write(_struct_I.pack(length))
        for val3 in _v23.image_points:
          _x = val3
          buff.write(_get_struct_2i().pack(_x.x, _x.y))
        length = len(_v23.contourTranslates)
        buff.write(_struct_I.pack(length))
        for val3 in _v23.contourTranslates:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v24 = val1.track
        _x = _v24
        buff.write(_get_struct_iB().pack(_x.id, _x.status))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.objects is None:
        self.objects = None
      end = 0
      start = end
      end += 4
      (self.type_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type_name = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.score, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y,) = _get_struct_d4i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rect.cornerTranslates = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.rect.cornerTranslates.append(val1)
      _x = self
      start = end
      end += 56
      (_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.objects = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.SimpleObject()
        start = end
        end += 4
        (val1.type_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type_name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.type_name = str[start:end]
        start = end
        end += 8
        (val1.score,) = _get_struct_d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.extracted_info = []
        for i in range(0, length):
          val2 = extended_object_detection.msg.ExtractedInfo()
          start = end
          end += 4
          (val2.sub_id,) = _get_struct_i().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.text = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.text = str[start:end]
          val1.extracted_info.append(val2)
        _v25 = val1.transform
        _v26 = _v25.translation
        _x = _v26
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v27 = _v25.rotation
        _x = _v27
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v28 = val1.rect
        _v29 = _v28.left_bottom
        _x = _v29
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        _v30 = _v28.right_up
        _x = _v30
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v28.cornerTranslates = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Vector3()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v28.cornerTranslates.append(val3)
        _v31 = val1.contour
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v31.image_points = []
        for i in range(0, length):
          val3 = extended_object_detection.msg.ImagePoint()
          _x = val3
          start = end
          end += 8
          (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
          _v31.image_points.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v31.contourTranslates = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Vector3()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v31.contourTranslates.append(val3)
        _v32 = val1.track
        _x = _v32
        start = end
        end += 5
        (_x.id, _x.status,) = _get_struct_iB().unpack(str[start:end])
        self.objects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_d4i = None
def _get_struct_d4i():
    global _struct_d4i
    if _struct_d4i is None:
        _struct_d4i = struct.Struct("<d4i")
    return _struct_d4i
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_iB = None
def _get_struct_iB():
    global _struct_iB
    if _struct_iB is None:
        _struct_iB = struct.Struct("<iB")
    return _struct_iB
