# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_madmin import generic_pb2 as grpc__madmin_dot_generic__pb2
from grpc_madmin import user_pb2 as grpc__madmin_dot_user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

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
        self.OnDisableUser = channel.unary_unary(
                '/grpc_madmin.user.UserService/OnDisableUser',
                request_serializer=grpc__madmin_dot_user__pb2.UserAccessUpdated.SerializeToString,
                response_deserializer=grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
                )
        self.ListSSGs = channel.unary_stream(
                '/grpc_madmin.user.UserService/ListSSGs',
                request_serializer=grpc__madmin_dot_user__pb2.RequestSSGListing.SerializeToString,
                response_deserializer=grpc__madmin_dot_user__pb2.ServerSpecificGroup.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnUpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnDisableUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSSGs(self, request, context):
        """Missing associated documentation comment in .proto file."""
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
            'OnDisableUser': grpc.unary_unary_rpc_method_handler(
                    servicer.OnDisableUser,
                    request_deserializer=grpc__madmin_dot_user__pb2.UserAccessUpdated.FromString,
                    response_serializer=grpc__madmin_dot_generic__pb2.GenericResponse.SerializeToString,
            ),
            'ListSSGs': grpc.unary_stream_rpc_method_handler(
                    servicer.ListSSGs,
                    request_deserializer=grpc__madmin_dot_user__pb2.RequestSSGListing.FromString,
                    response_serializer=grpc__madmin_dot_user__pb2.ServerSpecificGroup.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_madmin.user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnUpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_madmin.user.UserService/OnUpdateUser',
            grpc__madmin_dot_user__pb2.UserAccessUpdated.SerializeToString,
            grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnDisableUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_madmin.user.UserService/OnDisableUser',
            grpc__madmin_dot_user__pb2.UserAccessUpdated.SerializeToString,
            grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSSGs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc_madmin.user.UserService/ListSSGs',
            grpc__madmin_dot_user__pb2.RequestSSGListing.SerializeToString,
            grpc__madmin_dot_user__pb2.ServerSpecificGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BotServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateUserRoles = channel.unary_unary(
                '/grpc_madmin.user.BotService/UpdateUserRoles',
                request_serializer=grpc__madmin_dot_user__pb2.RoleAccessUpdate.SerializeToString,
                response_deserializer=grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
                )
        self.KickUser = channel.unary_unary(
                '/grpc_madmin.user.BotService/KickUser',
                request_serializer=grpc__madmin_dot_user__pb2.UserKick.SerializeToString,
                response_deserializer=grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
                )


class BotServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateUserRoles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KickUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateUserRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserRoles,
                    request_deserializer=grpc__madmin_dot_user__pb2.RoleAccessUpdate.FromString,
                    response_serializer=grpc__madmin_dot_generic__pb2.GenericResponse.SerializeToString,
            ),
            'KickUser': grpc.unary_unary_rpc_method_handler(
                    servicer.KickUser,
                    request_deserializer=grpc__madmin_dot_user__pb2.UserKick.FromString,
                    response_serializer=grpc__madmin_dot_generic__pb2.GenericResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_madmin.user.BotService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BotService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateUserRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_madmin.user.BotService/UpdateUserRoles',
            grpc__madmin_dot_user__pb2.RoleAccessUpdate.SerializeToString,
            grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KickUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_madmin.user.BotService/KickUser',
            grpc__madmin_dot_user__pb2.UserKick.SerializeToString,
            grpc__madmin_dot_generic__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
