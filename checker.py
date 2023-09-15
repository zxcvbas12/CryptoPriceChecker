import tkinter as tk
import requests

# API endpoint configuration
base_url = "https://api.kucoin.com"
endpoint = "/api/v1/market/orderbook/level1"

# Create a Tkinter window
window = tk.Tk()
window.title("Coin Price Lookup")

# Set the initial window size
window.geometry("350x150")


# Function to retrieve KuCoin coin price
def get_coin_price(event=None):
    symbol = symbol_entry.get().upper()
    response = requests.get(base_url + endpoint, params={"symbol": symbol})

    if response.status_code == 200:
        result = response.json()
        result_label.config(
            text=f"Current price of {symbol}: {result['data']['price']}"
        )
    else:
        result_label.config(
            text=f"Error occurred: {response.status_code} - {response.text}"
        )


# Labels and input field
symbol_label = tk.Label(window, text="Coin Ticker:")
symbol_label.pack()

symbol_entry = tk.Entry(window)
symbol_entry.pack()

# Bind the Enter key to the get_coin_price function
symbol_entry.bind("<Return>", get_coin_price)

# Lookup button
fetch_button = tk.Button(window, text="Lookup Price", command=get_coin_price)
fetch_button.pack()

# Result display label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
