# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_madmin/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_madmin import generic_pb2 as grpc__madmin_dot_generic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16grpc_madmin/user.proto\x12\x10grpc_madmin.user\x1a\x19grpc_madmin/generic.proto\"G\n\x10RoleAccessUpdate\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\x12\x10\n\x08guild_id\x18\x02 \x01(\x03\x12\r\n\x05roles\x18\x03 \x03(\x03\"@\n\x08UserKick\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\x12\x10\n\x08guild_id\x18\x02 \x01(\x03\x12\x0e\n\x06reason\x18\x03 \x01(\t\"\xc2\x01\n\x11UserAccessUpdated\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\x05\x12\x10\n\x08sso_uuid\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\ndiscord_id\x18\x04 \x01(\x03\x12\x1e\n\x16primary_character_name\x18\x05 \x01(\t\x12 \n\x18primary_corporation_name\x18\x06 \x01(\t\x12\"\n\x1aprimary_corporation_ticker\x18\x07 \x01(\t\"I\n\x10UserGroupRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08guild_id\x18\x02 \x01(\x03\x12\x12\n\ngroup_name\x18\x03 \x01(\t\"O\n\x13ServerSpecificGroup\x12\x10\n\x08guild_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10requestable_name\x18\x03 \x01(\t\"%\n\x11RequestSSGListing\x12\x10\n\x08guild_id\x18\x01 \x01(\x03\x32\x9e\x02\n\x0bUserService\x12Y\n\x0cOnUpdateUser\x12#.grpc_madmin.user.UserAccessUpdated\x1a$.grpc_madmin.generic.GenericResponse\x12Z\n\rOnDisableUser\x12#.grpc_madmin.user.UserAccessUpdated\x1a$.grpc_madmin.generic.GenericResponse\x12X\n\x08ListSSGs\x12#.grpc_madmin.user.RequestSSGListing\x1a%.grpc_madmin.user.ServerSpecificGroup0\x01\x32\xb7\x01\n\nBotService\x12[\n\x0fUpdateUserRoles\x12\".grpc_madmin.user.RoleAccessUpdate\x1a$.grpc_madmin.generic.GenericResponse\x12L\n\x08KickUser\x12\x1a.grpc_madmin.user.UserKick\x1a$.grpc_madmin.generic.GenericResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_madmin.user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROLEACCESSUPDATE._serialized_start=71
  _ROLEACCESSUPDATE._serialized_end=142
  _USERKICK._serialized_start=144
  _USERKICK._serialized_end=208
  _USERACCESSUPDATED._serialized_start=211
  _USERACCESSUPDATED._serialized_end=405
  _USERGROUPREQUEST._serialized_start=407
  _USERGROUPREQUEST._serialized_end=480
  _SERVERSPECIFICGROUP._serialized_start=482
  _SERVERSPECIFICGROUP._serialized_end=561
  _REQUESTSSGLISTING._serialized_start=563
  _REQUESTSSGLISTING._serialized_end=600
  _USERSERVICE._serialized_start=603
  _USERSERVICE._serialized_end=889
  _BOTSERVICE._serialized_start=892
  _BOTSERVICE._serialized_end=1075
# @@protoc_insertion_point(module_scope)
