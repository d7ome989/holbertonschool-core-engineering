#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in list(connected_clients):
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    pass
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
