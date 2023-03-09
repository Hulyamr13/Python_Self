# Constants
FREE_MINUTES = 60
FREE_MESSAGES = 20
PACKAGE_PRICE = 12.00
MINUTE_RATE = 0.10
MESSAGE_RATE = 0.06
TAX_RATE = 0.20

# Get text and minute inputs
messages = int(input())
minutes = int(input())

# Calculate the additional charges for text and minutes
additional_messages = max(messages - FREE_MESSAGES, 0)
additional_message_charge = additional_messages * MESSAGE_RATE

additional_minutes = max(minutes - FREE_MINUTES, 0)
additional_minute_charge = additional_minutes * MINUTE_RATE

# Calculate the tax amount
subtotal = additional_message_charge + additional_minute_charge
tax = subtotal * TAX_RATE

# Calculate the total amount paid
total = PACKAGE_PRICE + subtotal + tax

# Output the results
print(f"{additional_messages} additional messages for {additional_message_charge:.2f} levas")
print(f"{additional_minutes} additional minutes for {additional_minute_charge:.2f} levas")
print(f"{tax:.2f} additional taxes")
print(f"{total:.2f} total bill")
