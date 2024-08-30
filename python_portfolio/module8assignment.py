#Julie Sakai
#Module 8.2 Assignment

#Create a dictionary of stock ticker symbols and prices.
stock_prices = {
    "DIS": 119.10,
    "UVV": 50.20,
    "NFLX": 310.40,
    "AMZN": 921.00,
    "AAPL": 200.50,
    "ABNB": 95.10,
    "AEO": 60.20,
    "CAKE": 330.70,
    "BZFD": 120.00,
    "CROX": 220.90,
}

#Ask the user to enter a ticker symbol.
user_input = input("Enter a stock ticker symbol: ")

#Search the dictionary for the ticker symbol and print ticker symbol
#and the stock price.
#Ticker symbol not located print message that it was not found. 
if user_input in stock_prices:
    print(f"Ticker symbol: {user_input}, Stock price: ${stock_prices[user_input]:.2f}")
else:
    print(f"Ticker symbol '{user_input}' not found.")