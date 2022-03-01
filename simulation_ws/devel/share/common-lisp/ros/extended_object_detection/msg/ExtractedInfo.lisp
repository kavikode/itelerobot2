; Auto-generated. Do not edit!


(cl:in-package extended_object_detection-msg)


;//! \htmlinclude ExtractedInfo.msg.html

(cl:defclass <ExtractedInfo> (roslisp-msg-protocol:ros-message)
  ((sub_id
    :reader sub_id
    :initarg :sub_id
    :type cl:integer
    :initform 0)
   (text
    :reader text
    :initarg :text
    :type cl:string
    :initform ""))
)

(cl:defclass ExtractedInfo (<ExtractedInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExtractedInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExtractedInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name extended_object_detection-msg:<ExtractedInfo> is deprecated: use extended_object_detection-msg:ExtractedInfo instead.")))

(cl:ensure-generic-function 'sub_id-val :lambda-list '(m))
(cl:defmethod sub_id-val ((m <ExtractedInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader extended_object_detection-msg:sub_id-val is deprecated.  Use extended_object_detection-msg:sub_id instead.")
  (sub_id m))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <ExtractedInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader extended_object_detection-msg:text-val is deprecated.  Use extended_object_detection-msg:text instead.")
  (text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExtractedInfo>) ostream)
  "Serializes a message object of type '<ExtractedInfo>"
  (cl:let* ((signed (cl:slot-value msg 'sub_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExtractedInfo>) istream)
  "Deserializes a message object of type '<ExtractedInfo>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sub_id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExtractedInfo>)))
  "Returns string type for a message object of type '<ExtractedInfo>"
  "extended_object_detection/ExtractedInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExtractedInfo)))
  "Returns string type for a message object of type 'ExtractedInfo"
  "extended_object_detection/ExtractedInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExtractedInfo>)))
  "Returns md5sum for a message object of type '<ExtractedInfo>"
  "185b73de2075ebcbf80e7c87c570695a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExtractedInfo)))
  "Returns md5sum for a message object of type 'ExtractedInfo"
  "185b73de2075ebcbf80e7c87c570695a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExtractedInfo>)))
  "Returns full string definition for message of type '<ExtractedInfo>"
  (cl:format cl:nil "int32 sub_id~%string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExtractedInfo)))
  "Returns full string definition for message of type 'ExtractedInfo"
  (cl:format cl:nil "int32 sub_id~%string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExtractedInfo>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExtractedInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'ExtractedInfo
    (cl:cons ':sub_id (sub_id msg))
    (cl:cons ':text (text msg))
))
