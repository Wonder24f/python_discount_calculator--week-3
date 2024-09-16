def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Output the result
if discount_percent >= 20:
    print(f"After applying the discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: ${price:.2f}")
