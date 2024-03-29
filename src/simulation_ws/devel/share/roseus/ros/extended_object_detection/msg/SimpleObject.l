;; Auto-generated. Do not edit!


(when (boundp 'extended_object_detection::SimpleObject)
  (if (not (find-package "EXTENDED_OBJECT_DETECTION"))
    (make-package "EXTENDED_OBJECT_DETECTION"))
  (shadow 'SimpleObject (find-package "EXTENDED_OBJECT_DETECTION")))
(unless (find-package "EXTENDED_OBJECT_DETECTION::SIMPLEOBJECT")
  (make-package "EXTENDED_OBJECT_DETECTION::SIMPLEOBJECT"))

(in-package "ROS")
;;//! \htmlinclude SimpleObject.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass extended_object_detection::SimpleObject
  :super ros::object
  :slots (_type_id _type_name _score _extracted_info _transform _rect _contour _track ))

(defmethod extended_object_detection::SimpleObject
  (:init
   (&key
    ((:type_id __type_id) 0)
    ((:type_name __type_name) "")
    ((:score __score) 0.0)
    ((:extracted_info __extracted_info) ())
    ((:transform __transform) (instance geometry_msgs::Transform :init))
    ((:rect __rect) (instance extended_object_detection::Rect :init))
    ((:contour __contour) (instance extended_object_detection::Contour :init))
    ((:track __track) (instance extended_object_detection::Track :init))
    )
   (send-super :init)
   (setq _type_id (round __type_id))
   (setq _type_name (string __type_name))
   (setq _score (float __score))
   (setq _extracted_info __extracted_info)
   (setq _transform __transform)
   (setq _rect __rect)
   (setq _contour __contour)
   (setq _track __track)
   self)
  (:type_id
   (&optional __type_id)
   (if __type_id (setq _type_id __type_id)) _type_id)
  (:type_name
   (&optional __type_name)
   (if __type_name (setq _type_name __type_name)) _type_name)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:extracted_info
   (&rest __extracted_info)
   (if (keywordp (car __extracted_info))
       (send* _extracted_info __extracted_info)
     (progn
       (if __extracted_info (setq _extracted_info (car __extracted_info)))
       _extracted_info)))
  (:transform
   (&rest __transform)
   (if (keywordp (car __transform))
       (send* _transform __transform)
     (progn
       (if __transform (setq _transform (car __transform)))
       _transform)))
  (:rect
   (&rest __rect)
   (if (keywordp (car __rect))
       (send* _rect __rect)
     (progn
       (if __rect (setq _rect (car __rect)))
       _rect)))
  (:contour
   (&rest __contour)
   (if (keywordp (car __contour))
       (send* _contour __contour)
     (progn
       (if __contour (setq _contour (car __contour)))
       _contour)))
  (:track
   (&rest __track)
   (if (keywordp (car __track))
       (send* _track __track)
     (progn
       (if __track (setq _track (car __track)))
       _track)))
  (:serialization-length
   ()
   (+
    ;; int32 _type_id
    4
    ;; string _type_name
    4 (length _type_name)
    ;; float64 _score
    8
    ;; extended_object_detection/ExtractedInfo[] _extracted_info
    (apply #'+ (send-all _extracted_info :serialization-length)) 4
    ;; geometry_msgs/Transform _transform
    (send _transform :serialization-length)
    ;; extended_object_detection/Rect _rect
    (send _rect :serialization-length)
    ;; extended_object_detection/Contour _contour
    (send _contour :serialization-length)
    ;; extended_object_detection/Track _track
    (send _track :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _type_id
       (write-long _type_id s)
     ;; string _type_name
       (write-long (length _type_name) s) (princ _type_name s)
     ;; float64 _score
       (sys::poke _score (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; extended_object_detection/ExtractedInfo[] _extracted_info
     (write-long (length _extracted_info) s)
     (dolist (elem _extracted_info)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Transform _transform
       (send _transform :serialize s)
     ;; extended_object_detection/Rect _rect
       (send _rect :serialize s)
     ;; extended_object_detection/Contour _contour
       (send _contour :serialize s)
     ;; extended_object_detection/Track _track
       (send _track :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _type_id
     (setq _type_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _type_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _score
     (setq _score (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; extended_object_detection/ExtractedInfo[] _extracted_info
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _extracted_info (let (r) (dotimes (i n) (push (instance extended_object_detection::ExtractedInfo :init) r)) r))
     (dolist (elem- _extracted_info)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Transform _transform
     (send _transform :deserialize buf ptr-) (incf ptr- (send _transform :serialization-length))
   ;; extended_object_detection/Rect _rect
     (send _rect :deserialize buf ptr-) (incf ptr- (send _rect :serialization-length))
   ;; extended_object_detection/Contour _contour
     (send _contour :deserialize buf ptr-) (incf ptr- (send _contour :serialization-length))
   ;; extended_object_detection/Track _track
     (send _track :deserialize buf ptr-) (incf ptr- (send _track :serialization-length))
   ;;
   self)
  )

(setf (get extended_object_detection::SimpleObject :md5sum-) "025fc204af6671be7405ca314b787523")
(setf (get extended_object_detection::SimpleObject :datatype-) "extended_object_detection/SimpleObject")
(setf (get extended_object_detection::SimpleObject :definition-)
      "# object info
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

")



(provide :extended_object_detection/SimpleObject "025fc204af6671be7405ca314b787523")


