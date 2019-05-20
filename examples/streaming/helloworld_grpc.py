# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: streaming/helloworld.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import streaming.helloworld_pb2


class GreeterBase(abc.ABC):

    @abc.abstractmethod
    async def UnaryUnaryGreeting(self, stream: 'grpclib.server.Stream[streaming.helloworld_pb2.HelloRequest, streaming.helloworld_pb2.HelloReply]') -> None:
        pass

    @abc.abstractmethod
    async def UnaryStreamGreeting(self, stream: 'grpclib.server.Stream[streaming.helloworld_pb2.HelloRequest, streaming.helloworld_pb2.HelloReply]') -> None:
        pass

    @abc.abstractmethod
    async def StreamUnaryGreeting(self, stream: 'grpclib.server.Stream[streaming.helloworld_pb2.HelloRequest, streaming.helloworld_pb2.HelloReply]') -> None:
        pass

    @abc.abstractmethod
    async def StreamStreamGreeting(self, stream: 'grpclib.server.Stream[streaming.helloworld_pb2.HelloRequest, streaming.helloworld_pb2.HelloReply]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/helloworld.Greeter/UnaryUnaryGreeting': grpclib.const.Handler(
                self.UnaryUnaryGreeting,
                grpclib.const.Cardinality.UNARY_UNARY,
                streaming.helloworld_pb2.HelloRequest,
                streaming.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/UnaryStreamGreeting': grpclib.const.Handler(
                self.UnaryStreamGreeting,
                grpclib.const.Cardinality.UNARY_STREAM,
                streaming.helloworld_pb2.HelloRequest,
                streaming.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/StreamUnaryGreeting': grpclib.const.Handler(
                self.StreamUnaryGreeting,
                grpclib.const.Cardinality.STREAM_UNARY,
                streaming.helloworld_pb2.HelloRequest,
                streaming.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/StreamStreamGreeting': grpclib.const.Handler(
                self.StreamStreamGreeting,
                grpclib.const.Cardinality.STREAM_STREAM,
                streaming.helloworld_pb2.HelloRequest,
                streaming.helloworld_pb2.HelloReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UnaryUnaryGreeting = grpclib.client.UnaryUnaryMethod(
            channel,
            '/helloworld.Greeter/UnaryUnaryGreeting',
            streaming.helloworld_pb2.HelloRequest,
            streaming.helloworld_pb2.HelloReply,
        )
        self.UnaryStreamGreeting = grpclib.client.UnaryStreamMethod(
            channel,
            '/helloworld.Greeter/UnaryStreamGreeting',
            streaming.helloworld_pb2.HelloRequest,
            streaming.helloworld_pb2.HelloReply,
        )
        self.StreamUnaryGreeting = grpclib.client.StreamUnaryMethod(
            channel,
            '/helloworld.Greeter/StreamUnaryGreeting',
            streaming.helloworld_pb2.HelloRequest,
            streaming.helloworld_pb2.HelloReply,
        )
        self.StreamStreamGreeting = grpclib.client.StreamStreamMethod(
            channel,
            '/helloworld.Greeter/StreamStreamGreeting',
            streaming.helloworld_pb2.HelloRequest,
            streaming.helloworld_pb2.HelloReply,
        )
