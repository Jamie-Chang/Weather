import asyncio

from grpclib.client import Channel
from proto.weather_pb2 import WeatherRequest
from proto.weather_grpc import CheckerStub


async def main():
    loop = asyncio.get_event_loop()
    # perform request
    channel = Channel('127.0.0.1', 50051, loop=loop)
    stub = CheckerStub(channel)
    response = await stub.check_weather(WeatherRequest(end=False))
    print(f"Weather is now {response.temperature}")

    async with stub.stream_weather.open() as stream:
        await stream.send_message(WeatherRequest(end=False))
        for i in range(10):
            message = await stream.recv_message()
            print(f"Weather is now {message.temperature}")
        await stream.send_message(WeatherRequest(end=True))

    channel.close()


if __name__ == '__main__':
    asyncio.run(main())
