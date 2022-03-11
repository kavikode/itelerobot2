// Auto-generated. Do not edit!

// (in-package extended_object_detection.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ExtractedInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sub_id = null;
      this.text = null;
    }
    else {
      if (initObj.hasOwnProperty('sub_id')) {
        this.sub_id = initObj.sub_id
      }
      else {
        this.sub_id = 0;
      }
      if (initObj.hasOwnProperty('text')) {
        this.text = initObj.text
      }
      else {
        this.text = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExtractedInfo
    // Serialize message field [sub_id]
    bufferOffset = _serializer.int32(obj.sub_id, buffer, bufferOffset);
    // Serialize message field [text]
    bufferOffset = _serializer.string(obj.text, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExtractedInfo
    let len;
    let data = new ExtractedInfo(null);
    // Deserialize message field [sub_id]
    data.sub_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [text]
    data.text = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.text);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'extended_object_detection/ExtractedInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '185b73de2075ebcbf80e7c87c570695a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 sub_id
    string text
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ExtractedInfo(null);
    if (msg.sub_id !== undefined) {
      resolved.sub_id = msg.sub_id;
    }
    else {
      resolved.sub_id = 0
    }

    if (msg.text !== undefined) {
      resolved.text = msg.text;
    }
    else {
      resolved.text = ''
    }

    return resolved;
    }
};

module.exports = ExtractedInfo;
