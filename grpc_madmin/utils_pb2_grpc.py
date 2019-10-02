# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_madmin import generic_pb2 as grpc__madmin_dot_generic__pb2
from grpc_madmin import utils_pb2 as grpc__madmin_dot_utils__pb2


class UtilsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenerateRandomWords = channel.unary_unary(
        '/grpc_madmin.utils.UtilsService/GenerateRandomWords',
        request_serializer=grpc__madmin_dot_utils__pb2.RandomWordsRequest.SerializeToString,
        response_deserializer=grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
        )


class UtilsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GenerateRandomWords(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UtilsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenerateRandomWords': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateRandomWords,
          request_deserializer=grpc__madmin_dot_utils__pb2.RandomWordsRequest.FromString,
          response_serializer=grpc__madmin_dot_generic__pb2.GenericResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_madmin.utils.UtilsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
