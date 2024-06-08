import asyncio  # Import the asyncio library for asynchronous programming
import websockets  # Import the websockets library for WebSocket communication
import json  # Import the json library for encoding and decoding JSON data

# URL for the Kraken WebSocket API
KRAKEN_WS_URL = "wss://ws.kraken.com"

# Asynchronous function to subscribe to the ticker information
async def subscribe_ticker(pairs):
    # Connect to the Kraken WebSocket server
    async with websockets.connect(KRAKEN_WS_URL) as websocket:
        # Prepare the subscription message in the required JSON format
        subscribe_message = {
            "event": "subscribe",
            "pair": pairs,  # List of currency pairs to subscribe to, e.g., ["XBT/USD", "ETH/USD"]
            "subscription": {"name": "ticker"}  # Specify the type of data to subscribe to (ticker information)
        }
        # Send the subscription message to the WebSocket server
        await websocket.send(json.dumps(subscribe_message))
        
        # Continuously receive messages from the WebSocket server
        async for message in websocket:
            # Decode the JSON message
            data = json.loads(message)
            # Yield the decoded data to the caller
            yield data
