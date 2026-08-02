# Basic algorithmic trading example
# This script shows a simple moving average signal strategy.

# A list of sample prices for the example.
prices = [100, 102, 101, 105, 104, 108, 110]
# The number of days used to calculate the moving average.
window = 3

# Defines a function that calculates the average of the last few prices.
def moving_average(values, size):
    # Checks whether there are enough values to calculate the average.
    if len(values) < size:
        # Returns nothing if the list is too short.
        return None
    # Returns the average of the last 'size' values.
    return sum(values[-size:]) / size

# Loops through each price day in the list.
for i in range(len(prices)):
    # For the first few days, we do not have enough data to compare signals.
    if i < window:
        # Sets the signal to HOLD until enough data is available.
        signal = "HOLD"
    else:
        # Calculates the moving average including the current day.
        current_ma = moving_average(prices[: i + 1], window)
        # Calculates the moving average for the previous day.
        previous_ma = moving_average(prices[:i], window)

        # Compares the two averages to decide whether the trend is going up or down.
        if current_ma > previous_ma:
            # If the recent average is higher, the signal is BUY.
            signal = "BUY"
        elif current_ma < previous_ma:
            # If the recent average is lower, the signal is SELL.
            signal = "SELL"
        else:
            # If both averages are equal, the signal is HOLD.
            signal = "HOLD"

    # Prints the day number, price, and the trading signal.
    print(f"Day {i + 1}: price = {prices[i]}, signal = {signal}")

