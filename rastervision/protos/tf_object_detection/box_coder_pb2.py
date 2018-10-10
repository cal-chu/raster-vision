# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/tf_object_detection/box_coder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rastervision.protos.tf_object_detection import faster_rcnn_box_coder_pb2 as rastervision_dot_protos_dot_tf__object__detection_dot_faster__rcnn__box__coder__pb2
from rastervision.protos.tf_object_detection import keypoint_box_coder_pb2 as rastervision_dot_protos_dot_tf__object__detection_dot_keypoint__box__coder__pb2
from rastervision.protos.tf_object_detection import mean_stddev_box_coder_pb2 as rastervision_dot_protos_dot_tf__object__detection_dot_mean__stddev__box__coder__pb2
from rastervision.protos.tf_object_detection import square_box_coder_pb2 as rastervision_dot_protos_dot_tf__object__detection_dot_square__box__coder__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/tf_object_detection/box_coder.proto',
  package='rastervision.protos.tf_object_detection',
  syntax='proto2',
  serialized_pb=_b('\n7rastervision/protos/tf_object_detection/box_coder.proto\x12\'rastervision.protos.tf_object_detection\x1a\x43rastervision/protos/tf_object_detection/faster_rcnn_box_coder.proto\x1a@rastervision/protos/tf_object_detection/keypoint_box_coder.proto\x1a\x43rastervision/protos/tf_object_detection/mean_stddev_box_coder.proto\x1a>rastervision/protos/tf_object_detection/square_box_coder.proto\"\x87\x03\n\x08\x42oxCoder\x12\\\n\x15\x66\x61ster_rcnn_box_coder\x18\x01 \x01(\x0b\x32;.rastervision.protos.tf_object_detection.FasterRcnnBoxCoderH\x00\x12\\\n\x15mean_stddev_box_coder\x18\x02 \x01(\x0b\x32;.rastervision.protos.tf_object_detection.MeanStddevBoxCoderH\x00\x12S\n\x10square_box_coder\x18\x03 \x01(\x0b\x32\x37.rastervision.protos.tf_object_detection.SquareBoxCoderH\x00\x12W\n\x12keypoint_box_coder\x18\x04 \x01(\x0b\x32\x39.rastervision.protos.tf_object_detection.KeypointBoxCoderH\x00\x42\x11\n\x0f\x62ox_coder_oneof')
  ,
  dependencies=[rastervision_dot_protos_dot_tf__object__detection_dot_faster__rcnn__box__coder__pb2.DESCRIPTOR,rastervision_dot_protos_dot_tf__object__detection_dot_keypoint__box__coder__pb2.DESCRIPTOR,rastervision_dot_protos_dot_tf__object__detection_dot_mean__stddev__box__coder__pb2.DESCRIPTOR,rastervision_dot_protos_dot_tf__object__detection_dot_square__box__coder__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BOXCODER = _descriptor.Descriptor(
  name='BoxCoder',
  full_name='rastervision.protos.tf_object_detection.BoxCoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faster_rcnn_box_coder', full_name='rastervision.protos.tf_object_detection.BoxCoder.faster_rcnn_box_coder', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_stddev_box_coder', full_name='rastervision.protos.tf_object_detection.BoxCoder.mean_stddev_box_coder', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='square_box_coder', full_name='rastervision.protos.tf_object_detection.BoxCoder.square_box_coder', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_box_coder', full_name='rastervision.protos.tf_object_detection.BoxCoder.keypoint_box_coder', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='box_coder_oneof', full_name='rastervision.protos.tf_object_detection.BoxCoder.box_coder_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=369,
  serialized_end=760,
)

_BOXCODER.fields_by_name['faster_rcnn_box_coder'].message_type = rastervision_dot_protos_dot_tf__object__detection_dot_faster__rcnn__box__coder__pb2._FASTERRCNNBOXCODER
_BOXCODER.fields_by_name['mean_stddev_box_coder'].message_type = rastervision_dot_protos_dot_tf__object__detection_dot_mean__stddev__box__coder__pb2._MEANSTDDEVBOXCODER
_BOXCODER.fields_by_name['square_box_coder'].message_type = rastervision_dot_protos_dot_tf__object__detection_dot_square__box__coder__pb2._SQUAREBOXCODER
_BOXCODER.fields_by_name['keypoint_box_coder'].message_type = rastervision_dot_protos_dot_tf__object__detection_dot_keypoint__box__coder__pb2._KEYPOINTBOXCODER
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['faster_rcnn_box_coder'])
_BOXCODER.fields_by_name['faster_rcnn_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['mean_stddev_box_coder'])
_BOXCODER.fields_by_name['mean_stddev_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['square_box_coder'])
_BOXCODER.fields_by_name['square_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['keypoint_box_coder'])
_BOXCODER.fields_by_name['keypoint_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
DESCRIPTOR.message_types_by_name['BoxCoder'] = _BOXCODER

BoxCoder = _reflection.GeneratedProtocolMessageType('BoxCoder', (_message.Message,), dict(
  DESCRIPTOR = _BOXCODER,
  __module__ = 'rastervision.protos.tf_object_detection.box_coder_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.BoxCoder)
  ))
_sym_db.RegisterMessage(BoxCoder)


# @@protoc_insertion_point(module_scope)