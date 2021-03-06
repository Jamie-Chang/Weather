# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: proto/weather.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import proto.weather_pb2


class CheckerBase(abc.ABC):

    @abc.abstractmethod
    async def check_weather(self, stream):
        pass

    @abc.abstractmethod
    async def stream_weather(self, stream):
        pass

    def __mapping__(self):
        return {
            '/weather.Checker/check_weather': grpclib.const.Handler(
                self.check_weather,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.weather_pb2.WeatherRequest,
                proto.weather_pb2.WeatherReply,
            ),
            '/weather.Checker/stream_weather': grpclib.const.Handler(
                self.stream_weather,
                grpclib.const.Cardinality.STREAM_STREAM,
                proto.weather_pb2.WeatherRequest,
                proto.weather_pb2.WeatherReply,
            ),
        }


class CheckerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.check_weather = grpclib.client.UnaryUnaryMethod(
            channel,
            '/weather.Checker/check_weather',
            proto.weather_pb2.WeatherRequest,
            proto.weather_pb2.WeatherReply,
        )
        self.stream_weather = grpclib.client.StreamStreamMethod(
            channel,
            '/weather.Checker/stream_weather',
            proto.weather_pb2.WeatherRequest,
            proto.weather_pb2.WeatherReply,
        )
