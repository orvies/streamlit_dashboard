import sys
import os

# Add the parent directory of `src` to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st  # Import Streamlit for building the web application
import asyncio  # Import the asyncio library for asynchronous programming
from kraken_websocket import subscribe_ticker  # Import the subscribe_ticker function

# Main function for the Streamlit application
def main():
    st.title("Kraken WebSocket API with Streamlit")  # Set the title of the web application

    st.write("Fetching real-time ticker information from Kraken...")  # Display a message

    # Define the pairs you want to subscribe to
    pairs = ["XBT/USD", "ETH/USD"]

    # Create a container for displaying the updates
    placeholder = st.empty()

    # Define an asynchronous function to display ticker updates
    async def display_ticker_updates():
        async for update in subscribe_ticker(pairs):
            with placeholder.container():
                st.write(update)

    # Run the async function in the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(display_ticker_updates())

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()
