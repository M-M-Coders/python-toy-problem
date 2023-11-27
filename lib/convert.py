def convert_to_24_hour(hour, minute, period):
    # Check if it's PM and not 12
    if period.lower() == "pm" and hour != 12:
        # Convert to 24-hour format by adding 12
        hour += 12
    
    # If it's AM and 12, set hours to 0
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Return the time in 24-hour format as a four-digit string
    return f"{hour:02d}{minute:02d}"

# Example usage:
hour = 12
minute = 30
period = "am"

result = convert_to_24_hour(hour, minute, period)
print(result)
