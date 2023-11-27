def exactly_two_positives(a, b, c):
    # Count the number of positive integers
    positive_count = 0

    # Check if 'a' is positive
    if a > 0:
        positive_count += 1

    # Check if 'b' is positive
    if b > 0:
        positive_count += 1

    # Check if 'c' is positive
    if c > 0:
        positive_count += 1

    # Return True if exactly two integers are positive, otherwise False
    return positive_count == 2
print(exactly_two_positives(2, 4, -3))