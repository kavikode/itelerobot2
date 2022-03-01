# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from extended_object_detection/SimpleObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import extended_object_detection.msg
import geometry_msgs.msg

class SimpleObject(genpy.Message):
  _md5sum = "025fc204af6671be7405ca314b787523"
  _type = "extended_object_detection/SimpleObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# object info
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
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

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
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

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
  __slots__ = ['type_id','type_name','score','extracted_info','transform','rect','contour','track']
  _slot_types = ['int32','string','float64','extended_object_detection/ExtractedInfo[]','geometry_msgs/Transform','extended_object_detection/Rect','extended_object_detection/Contour','extended_object_detection/Track']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type_id,type_name,score,extracted_info,transform,rect,contour,track

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SimpleObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.type_id is None:
        self.type_id = 0
      if self.type_name is None:
        self.type_name = ''
      if self.score is None:
        self.score = 0.
      if self.extracted_info is None:
        self.extracted_info = []
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.contour is None:
        self.contour = extended_object_detection.msg.Contour()
      if self.track is None:
        self.track = extended_object_detection.msg.Track()
    else:
      self.type_id = 0
      self.type_name = ''
      self.score = 0.
      self.extracted_info = []
      self.transform = geometry_msgs.msg.Transform()
      self.rect = extended_object_detection.msg.Rect()
      self.contour = extended_object_detection.msg.Contour()
      self.track = extended_object_detection.msg.Track()

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
      _x = self.score
      buff.write(_get_struct_d().pack(_x))
      length = len(self.extracted_info)
      buff.write(_struct_I.pack(length))
      for val1 in self.extracted_info:
        _x = val1.sub_id
        buff.write(_get_struct_i().pack(_x))
        _x = val1.text
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d4i().pack(_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y))
      length = len(self.rect.cornerTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.rect.cornerTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.contour.image_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.contour.image_points:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
      length = len(self.contour.contourTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.contour.contourTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_iB().pack(_x.track.id, _x.track.status))
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
      if self.extracted_info is None:
        self.extracted_info = None
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.contour is None:
        self.contour = extended_object_detection.msg.Contour()
      if self.track is None:
        self.track = extended_object_detection.msg.Track()
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
      start = end
      end += 8
      (self.score,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.extracted_info = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.ExtractedInfo()
        start = end
        end += 4
        (val1.sub_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.text = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.text = str[start:end]
        self.extracted_info.append(val1)
      _x = self
      start = end
      end += 72
      (_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y,) = _get_struct_7d4i().unpack(str[start:end])
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contour.image_points = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.ImagePoint()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        self.contour.image_points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contour.contourTranslates = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.contour.contourTranslates.append(val1)
      _x = self
      start = end
      end += 5
      (_x.track.id, _x.track.status,) = _get_struct_iB().unpack(str[start:end])
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
      _x = self.score
      buff.write(_get_struct_d().pack(_x))
      length = len(self.extracted_info)
      buff.write(_struct_I.pack(length))
      for val1 in self.extracted_info:
        _x = val1.sub_id
        buff.write(_get_struct_i().pack(_x))
        _x = val1.text
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d4i().pack(_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y))
      length = len(self.rect.cornerTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.rect.cornerTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.contour.image_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.contour.image_points:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.x, _x.y))
      length = len(self.contour.contourTranslates)
      buff.write(_struct_I.pack(length))
      for val1 in self.contour.contourTranslates:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_iB().pack(_x.track.id, _x.track.status))
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
      if self.extracted_info is None:
        self.extracted_info = None
      if self.transform is None:
        self.transform = geometry_msgs.msg.Transform()
      if self.rect is None:
        self.rect = extended_object_detection.msg.Rect()
      if self.contour is None:
        self.contour = extended_object_detection.msg.Contour()
      if self.track is None:
        self.track = extended_object_detection.msg.Track()
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
      start = end
      end += 8
      (self.score,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.extracted_info = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.ExtractedInfo()
        start = end
        end += 4
        (val1.sub_id,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.text = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.text = str[start:end]
        self.extracted_info.append(val1)
      _x = self
      start = end
      end += 72
      (_x.transform.translation.x, _x.transform.translation.y, _x.transform.translation.z, _x.transform.rotation.x, _x.transform.rotation.y, _x.transform.rotation.z, _x.transform.rotation.w, _x.rect.left_bottom.x, _x.rect.left_bottom.y, _x.rect.right_up.x, _x.rect.right_up.y,) = _get_struct_7d4i().unpack(str[start:end])
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contour.image_points = []
      for i in range(0, length):
        val1 = extended_object_detection.msg.ImagePoint()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2i().unpack(str[start:end])
        self.contour.image_points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contour.contourTranslates = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.contour.contourTranslates.append(val1)
      _x = self
      start = end
      end += 5
      (_x.track.id, _x.track.status,) = _get_struct_iB().unpack(str[start:end])
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
_struct_7d4i = None
def _get_struct_7d4i():
    global _struct_7d4i
    if _struct_7d4i is None:
        _struct_7d4i = struct.Struct("<7d4i")
    return _struct_7d4i
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
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
