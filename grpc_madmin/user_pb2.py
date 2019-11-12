# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_madmin/user.proto

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
  name='grpc_madmin/user.proto',
  package='grpc_madmin.user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16grpc_madmin/user.proto\x12\x10grpc_madmin.user\x1a\x19grpc_madmin/generic.proto\"G\n\x10RoleAccessUpdate\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\x12\x10\n\x08guild_id\x18\x02 \x01(\x03\x12\r\n\x05roles\x18\x03 \x03(\x03\"\xc2\x01\n\x11UserAccessUpdated\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\x05\x12\x10\n\x08sso_uuid\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\ndiscord_id\x18\x04 \x01(\x03\x12\x1e\n\x16primary_character_name\x18\x05 \x01(\t\x12 \n\x18primary_corporation_name\x18\x06 \x01(\t\x12\"\n\x1aprimary_corporation_ticker\x18\x07 \x01(\t\"I\n\x10UserGroupRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08guild_id\x18\x02 \x01(\x03\x12\x12\n\ngroup_name\x18\x03 \x01(\t\"O\n\x13ServerSpecificGroup\x12\x10\n\x08guild_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10requestable_name\x18\x03 \x01(\t\"%\n\x11RequestSSGListing\x12\x10\n\x08guild_id\x18\x01 \x01(\x03\x32\x9e\x02\n\x0bUserService\x12Y\n\x0cOnUpdateUser\x12#.grpc_madmin.user.UserAccessUpdated\x1a$.grpc_madmin.generic.GenericResponse\x12Z\n\rOnDisableUser\x12#.grpc_madmin.user.UserAccessUpdated\x1a$.grpc_madmin.generic.GenericResponse\x12X\n\x08ListSSGs\x12#.grpc_madmin.user.RequestSSGListing\x1a%.grpc_madmin.user.ServerSpecificGroup0\x01\x32i\n\nBotService\x12[\n\x0fUpdateUserRoles\x12\".grpc_madmin.user.RoleAccessUpdate\x1a$.grpc_madmin.generic.GenericResponseb\x06proto3')
  ,
  dependencies=[grpc__madmin_dot_generic__pb2.DESCRIPTOR,])




_ROLEACCESSUPDATE = _descriptor.Descriptor(
  name='RoleAccessUpdate',
  full_name='grpc_madmin.user.RoleAccessUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discord_id', full_name='grpc_madmin.user.RoleAccessUpdate.discord_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='grpc_madmin.user.RoleAccessUpdate.guild_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles', full_name='grpc_madmin.user.RoleAccessUpdate.roles', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=71,
  serialized_end=142,
)


_USERACCESSUPDATED = _descriptor.Descriptor(
  name='UserAccessUpdated',
  full_name='grpc_madmin.user.UserAccessUpdated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_id', full_name='grpc_madmin.user.UserAccessUpdated.auth_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sso_uuid', full_name='grpc_madmin.user.UserAccessUpdated.sso_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc_madmin.user.UserAccessUpdated.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discord_id', full_name='grpc_madmin.user.UserAccessUpdated.discord_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_character_name', full_name='grpc_madmin.user.UserAccessUpdated.primary_character_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_corporation_name', full_name='grpc_madmin.user.UserAccessUpdated.primary_corporation_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_corporation_ticker', full_name='grpc_madmin.user.UserAccessUpdated.primary_corporation_ticker', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=145,
  serialized_end=339,
)


_USERGROUPREQUEST = _descriptor.Descriptor(
  name='UserGroupRequest',
  full_name='grpc_madmin.user.UserGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grpc_madmin.user.UserGroupRequest.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='grpc_madmin.user.UserGroupRequest.guild_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='grpc_madmin.user.UserGroupRequest.group_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=341,
  serialized_end=414,
)


_SERVERSPECIFICGROUP = _descriptor.Descriptor(
  name='ServerSpecificGroup',
  full_name='grpc_madmin.user.ServerSpecificGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='grpc_madmin.user.ServerSpecificGroup.guild_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc_madmin.user.ServerSpecificGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestable_name', full_name='grpc_madmin.user.ServerSpecificGroup.requestable_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=416,
  serialized_end=495,
)


_REQUESTSSGLISTING = _descriptor.Descriptor(
  name='RequestSSGListing',
  full_name='grpc_madmin.user.RequestSSGListing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='grpc_madmin.user.RequestSSGListing.guild_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=497,
  serialized_end=534,
)

DESCRIPTOR.message_types_by_name['RoleAccessUpdate'] = _ROLEACCESSUPDATE
DESCRIPTOR.message_types_by_name['UserAccessUpdated'] = _USERACCESSUPDATED
DESCRIPTOR.message_types_by_name['UserGroupRequest'] = _USERGROUPREQUEST
DESCRIPTOR.message_types_by_name['ServerSpecificGroup'] = _SERVERSPECIFICGROUP
DESCRIPTOR.message_types_by_name['RequestSSGListing'] = _REQUESTSSGLISTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAccessUpdate = _reflection.GeneratedProtocolMessageType('RoleAccessUpdate', (_message.Message,), {
  'DESCRIPTOR' : _ROLEACCESSUPDATE,
  '__module__' : 'grpc_madmin.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.user.RoleAccessUpdate)
  })
_sym_db.RegisterMessage(RoleAccessUpdate)

UserAccessUpdated = _reflection.GeneratedProtocolMessageType('UserAccessUpdated', (_message.Message,), {
  'DESCRIPTOR' : _USERACCESSUPDATED,
  '__module__' : 'grpc_madmin.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.user.UserAccessUpdated)
  })
_sym_db.RegisterMessage(UserAccessUpdated)

UserGroupRequest = _reflection.GeneratedProtocolMessageType('UserGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPREQUEST,
  '__module__' : 'grpc_madmin.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.user.UserGroupRequest)
  })
_sym_db.RegisterMessage(UserGroupRequest)

ServerSpecificGroup = _reflection.GeneratedProtocolMessageType('ServerSpecificGroup', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSPECIFICGROUP,
  '__module__' : 'grpc_madmin.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.user.ServerSpecificGroup)
  })
_sym_db.RegisterMessage(ServerSpecificGroup)

RequestSSGListing = _reflection.GeneratedProtocolMessageType('RequestSSGListing', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSSGLISTING,
  '__module__' : 'grpc_madmin.user_pb2'
  # @@protoc_insertion_point(class_scope:grpc_madmin.user.RequestSSGListing)
  })
_sym_db.RegisterMessage(RequestSSGListing)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='grpc_madmin.user.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=537,
  serialized_end=823,
  methods=[
  _descriptor.MethodDescriptor(
    name='OnUpdateUser',
    full_name='grpc_madmin.user.UserService.OnUpdateUser',
    index=0,
    containing_service=None,
    input_type=_USERACCESSUPDATED,
    output_type=grpc__madmin_dot_generic__pb2._GENERICRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='OnDisableUser',
    full_name='grpc_madmin.user.UserService.OnDisableUser',
    index=1,
    containing_service=None,
    input_type=_USERACCESSUPDATED,
    output_type=grpc__madmin_dot_generic__pb2._GENERICRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListSSGs',
    full_name='grpc_madmin.user.UserService.ListSSGs',
    index=2,
    containing_service=None,
    input_type=_REQUESTSSGLISTING,
    output_type=_SERVERSPECIFICGROUP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE


_BOTSERVICE = _descriptor.ServiceDescriptor(
  name='BotService',
  full_name='grpc_madmin.user.BotService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=825,
  serialized_end=930,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateUserRoles',
    full_name='grpc_madmin.user.BotService.UpdateUserRoles',
    index=0,
    containing_service=None,
    input_type=_ROLEACCESSUPDATE,
    output_type=grpc__madmin_dot_generic__pb2._GENERICRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOTSERVICE)

DESCRIPTOR.services_by_name['BotService'] = _BOTSERVICE

# @@protoc_insertion_point(module_scope)
