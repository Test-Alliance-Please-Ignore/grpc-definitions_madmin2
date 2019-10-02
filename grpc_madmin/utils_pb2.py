# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_madmin/utils.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_madmin import generic_pb2 as grpc__madmin_dot_generic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_madmin/utils.proto',
  package='grpc_madmin.utils',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17grpc_madmin/utils.proto\x12\x11grpc_madmin.utils\x1a\x19grpc_madmin/generic.proto\"5\n\x12RandomWordsRequest\x12\x0c\n\x04seed\x18\x01 \x01(\x03\x12\x11\n\tnum_words\x18\x02 \x01(\x05\x32r\n\x0cUtilsService\x12\x62\n\x13GenerateRandomWords\x12%.grpc_madmin.utils.RandomWordsRequest\x1a$.grpc_madmin.generic.GenericResponseb\x06proto3')
  ,
  dependencies=[grpc__madmin_dot_generic__pb2.DESCRIPTOR,])




_RANDOMWORDSREQUEST = _descriptor.Descriptor(
  name='RandomWordsRequest',
  full_name='grpc_madmin.utils.RandomWordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed', full_name='grpc_madmin.utils.RandomWordsRequest.seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_words', full_name='grpc_madmin.utils.RandomWordsRequest.num_words', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=73,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['RandomWordsRequest'] = _RANDOMWORDSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RandomWordsRequest = _reflection.GeneratedProtocolMessageType('RandomWordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMWORDSREQUEST,
  '__module__' : 'grpc_madmin.utils_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.utils.RandomWordsRequest)
  })
_sym_db.RegisterMessage(RandomWordsRequest)



_UTILSSERVICE = _descriptor.ServiceDescriptor(
  name='UtilsService',
  full_name='grpc_madmin.utils.UtilsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=128,
  serialized_end=242,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateRandomWords',
    full_name='grpc_madmin.utils.UtilsService.GenerateRandomWords',
    index=0,
    containing_service=None,
    input_type=_RANDOMWORDSREQUEST,
    output_type=grpc__madmin_dot_generic__pb2._GENERICRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UTILSSERVICE)

DESCRIPTOR.services_by_name['UtilsService'] = _UTILSSERVICE

# @@protoc_insertion_point(module_scope)
