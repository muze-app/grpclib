# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dummy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dummy.proto',
  package='dummy',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x64ummy.proto\x12\x05\x64ummy\"\x1d\n\x0c\x44ummyRequest\x12\r\n\x05value\x18\x01 \x01(\t\"\x1b\n\nDummyReply\x12\r\n\x05value\x18\x01 \x01(\t2\xfa\x01\n\x0c\x44ummyService\x12\x36\n\nUnaryUnary\x12\x13.dummy.DummyRequest\x1a\x11.dummy.DummyReply\"\x00\x12\x39\n\x0bUnaryStream\x12\x13.dummy.DummyRequest\x1a\x11.dummy.DummyReply\"\x00\x30\x01\x12\x39\n\x0bStreamUnary\x12\x13.dummy.DummyRequest\x1a\x11.dummy.DummyReply\"\x00(\x01\x12<\n\x0cStreamStream\x12\x13.dummy.DummyRequest\x1a\x11.dummy.DummyReply\"\x00(\x01\x30\x01\x62\x06proto3')
)




_DUMMYREQUEST = _descriptor.Descriptor(
  name='DummyRequest',
  full_name='dummy.DummyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dummy.DummyRequest.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=51,
)


_DUMMYREPLY = _descriptor.Descriptor(
  name='DummyReply',
  full_name='dummy.DummyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dummy.DummyReply.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['DummyRequest'] = _DUMMYREQUEST
DESCRIPTOR.message_types_by_name['DummyReply'] = _DUMMYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DummyRequest = _reflection.GeneratedProtocolMessageType('DummyRequest', (_message.Message,), dict(
  DESCRIPTOR = _DUMMYREQUEST,
  __module__ = 'dummy_pb2'
  # @@protoc_insertion_point(class_scope:dummy.DummyRequest)
  ))
_sym_db.RegisterMessage(DummyRequest)

DummyReply = _reflection.GeneratedProtocolMessageType('DummyReply', (_message.Message,), dict(
  DESCRIPTOR = _DUMMYREPLY,
  __module__ = 'dummy_pb2'
  # @@protoc_insertion_point(class_scope:dummy.DummyReply)
  ))
_sym_db.RegisterMessage(DummyReply)



_DUMMYSERVICE = _descriptor.ServiceDescriptor(
  name='DummyService',
  full_name='dummy.DummyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=83,
  serialized_end=333,
  methods=[
  _descriptor.MethodDescriptor(
    name='UnaryUnary',
    full_name='dummy.DummyService.UnaryUnary',
    index=0,
    containing_service=None,
    input_type=_DUMMYREQUEST,
    output_type=_DUMMYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnaryStream',
    full_name='dummy.DummyService.UnaryStream',
    index=1,
    containing_service=None,
    input_type=_DUMMYREQUEST,
    output_type=_DUMMYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUnary',
    full_name='dummy.DummyService.StreamUnary',
    index=2,
    containing_service=None,
    input_type=_DUMMYREQUEST,
    output_type=_DUMMYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamStream',
    full_name='dummy.DummyService.StreamStream',
    index=3,
    containing_service=None,
    input_type=_DUMMYREQUEST,
    output_type=_DUMMYREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DUMMYSERVICE)

DESCRIPTOR.services_by_name['DummyService'] = _DUMMYSERVICE

# @@protoc_insertion_point(module_scope)
