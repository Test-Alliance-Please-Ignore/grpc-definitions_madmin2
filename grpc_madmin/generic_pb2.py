# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_madmin/generic.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_madmin/generic.proto',
  package='grpc_madmin.generic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x19grpc_madmin/generic.proto\x12\x13grpc_madmin.generic\"2\n\x0fGenericResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\tb\x06proto3'
)




_GENERICRESPONSE = _descriptor.Descriptor(
  name='GenericResponse',
  full_name='grpc_madmin.generic.GenericResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='grpc_madmin.generic.GenericResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_madmin.generic.GenericResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=50,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['GenericResponse'] = _GENERICRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericResponse = _reflection.GeneratedProtocolMessageType('GenericResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERICRESPONSE,
  '__module__' : 'grpc_madmin.generic_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.generic.GenericResponse)
  })
_sym_db.RegisterMessage(GenericResponse)


# @@protoc_insertion_point(module_scope)
