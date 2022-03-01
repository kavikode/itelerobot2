;; Auto-generated. Do not edit!


(when (boundp 'extended_object_detection::ExtractedInfo)
  (if (not (find-package "EXTENDED_OBJECT_DETECTION"))
    (make-package "EXTENDED_OBJECT_DETECTION"))
  (shadow 'ExtractedInfo (find-package "EXTENDED_OBJECT_DETECTION")))
(unless (find-package "EXTENDED_OBJECT_DETECTION::EXTRACTEDINFO")
  (make-package "EXTENDED_OBJECT_DETECTION::EXTRACTEDINFO"))

(in-package "ROS")
;;//! \htmlinclude ExtractedInfo.msg.html


(defclass extended_object_detection::ExtractedInfo
  :super ros::object
  :slots (_sub_id _text ))

(defmethod extended_object_detection::ExtractedInfo
  (:init
   (&key
    ((:sub_id __sub_id) 0)
    ((:text __text) "")
    )
   (send-super :init)
   (setq _sub_id (round __sub_id))
   (setq _text (string __text))
   self)
  (:sub_id
   (&optional __sub_id)
   (if __sub_id (setq _sub_id __sub_id)) _sub_id)
  (:text
   (&optional __text)
   (if __text (setq _text __text)) _text)
  (:serialization-length
   ()
   (+
    ;; int32 _sub_id
    4
    ;; string _text
    4 (length _text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sub_id
       (write-long _sub_id s)
     ;; string _text
       (write-long (length _text) s) (princ _text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sub_id
     (setq _sub_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get extended_object_detection::ExtractedInfo :md5sum-) "185b73de2075ebcbf80e7c87c570695a")
(setf (get extended_object_detection::ExtractedInfo :datatype-) "extended_object_detection/ExtractedInfo")
(setf (get extended_object_detection::ExtractedInfo :definition-)
      "int32 sub_id
string text

")



(provide :extended_object_detection/ExtractedInfo "185b73de2075ebcbf80e7c87c570695a")


