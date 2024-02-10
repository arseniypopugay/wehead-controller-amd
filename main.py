import os
import asyncio
import json
from websockets import connect
from time import sleep


HEADID = os.environ["HEADID"]
HEADTOKEN = os.environ["HEADTOKEN"]
HEADURI = os.environ["HEADURI"]

async def interact_with_websocket():
    uri = "wss://" + HEADURI + "/control/user/" + HEADID + "?token=" + HEADTOKEN
    i = 0
    while i<=10:
        async with connect(uri) as websocket:
            # send message type 'tts'
            tts_message = {
                "type": "tts",
                "data": {
                    "text": "Hello Robotics World!"
                }
            }
            await websocket.send(json.dumps(tts_message))

            # send message type 'move'
            move_message = {
                "type": "move",
                "data": {
                    "position": "velocity",
                    "pitch": 0.1,
                    "yaw": 0.2
                }
            }
            await websocket.send(json.dumps(move_message))

            # receiving messages
            async for message in websocket:
                print(f"Received message: {message}")
            sleep(5)

asyncio.run(interact_with_websocket())