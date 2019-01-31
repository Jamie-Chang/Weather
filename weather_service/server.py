"""gRPC service."""
import asyncio
import darksky

from grpclib.server import Server
from grpclib.client import Channel

from proto.weather_grpc import CheckerBase
from proto.weather_pb2 import WeatherReply


class Checker(CheckerBase):
    """gRPC service to check the weather."""

    async def check_weather(self, stream):
        """Check the current weather."""
        request = await stream.recv_message()
        temperature = await get_temperature()
        await stream.send_message(WeatherReply(temperature=temperature))

    async def stream_weather(self, stream):
        """Stream the current weather.

        This is a stream - stream gRPC.
        """
        request = await stream.recv_message()
        stopped = False

        async def do_stream():
            while not stopped:
                temperature = await darksky.fetch_temperature()
                await stream.send_message(
                    WeatherReply(temperature=temperature)
                )
                await asyncio.sleep(2)

        task = asyncio.create_task(do_stream())
        while not stopped:
            stopped = (await stream.recv_message()).end

        await task


async def main():
    """Entry point."""
    # start server
    server = Server([Checker()], loop=asyncio.get_event_loop())
    await server.start('127.0.0.1', 50051)
    await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
