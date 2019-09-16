# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_madmin import generic_pb2 as grpc__madmin_dot_generic__pb2
from grpc_madmin import user_pb2 as grpc__madmin_dot_user__pb2


class UserServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.OnUpdateUser = channel.unary_unary(
        '/grpc_madmin.user.UserService/OnUpdateUser',
        request_serializer=grpc__madmin_dot_user__pb2.UserAccessUpdated.SerializeToString,
        response_deserializer=grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
        )


class UserServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def OnUpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'OnUpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.OnUpdateUser,
          request_deserializer=grpc__madmin_dot_user__pb2.UserAccessUpdated.FromString,
          response_serializer=grpc__madmin_dot_generic__pb2.GenericResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_madmin.user.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))