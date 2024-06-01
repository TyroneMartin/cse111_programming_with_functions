"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = input("Please enter your age or type 'quit' to exit: ")

while age.lower() != "quit":
    try:
        age = int(age)
        max_heart_rate_per_minute = 220 - age
        slowest_rate_per_minute = max_heart_rate_per_minute * 0.65
        highest_rate_per_minute = max_heart_rate_per_minute * 0.85
        print(f"Keep your heart rate between {slowest_rate_per_minute:.0f} and {highest_rate_per_minute:.0f} beats per minute.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")

    age = input("Please enter your age or type 'quit' to exit: ")

