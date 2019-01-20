import asyncio
import darksky

from grpclib.server import Server
from grpclib.client import Channel

from proto.weather_grpc import CheckerBase
from proto.weather_pb2 import WeatherReply



class Checker(CheckerBase):
    async def check_weather(self, stream):
        request = await stream.recv_message()
        temperature_doc = await darksky.fetch()
        temperature = temperature_doc.get('currently', {}).get('temperature')
        await stream.send_message(WeatherReply(temperature=temperature))


async def main():
    # start server
    server = Server([Checker()], loop=asyncio.get_event_loop())
    await server.start('127.0.0.1', 50051)
    await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
