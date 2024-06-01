from datetime import datetime  # Call the now() method to get the current the computer's operating system time.
current_date_and_time = datetime.now(tz=None)

# print(f"{current_date_and_time:%Y-%m-%d}")
current_date = current_date_and_time.strftime("%Y-%m-%d")

print(current_date)