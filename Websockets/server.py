import asyncio
import websockets
import lxml.objectify

async def handle_connection(websocket, path):
    async for message in websocket:
        print(message)

if __name__ == "__main__":
    future = websockets.serve(handle_connection, "localhost", 8000)
    asyncio.get_event_loop().run_until_complete(future)
    asyncio.get_event_loop().run_forever()