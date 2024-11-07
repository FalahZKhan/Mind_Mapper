import random
import os

def generate_random_points(num_points, range_limit, clustered=False):
    points = []
    if clustered:
        # Cluster points within a limited range for edge case testing
        cluster_center = (random.randint(0, range_limit), random.randint(0, range_limit))
        points = [(cluster_center[0] + random.randint(-5, 5), cluster_center[1] + random.randint(-5, 5)) for _ in range(num_points)]
    else:
        # Spread points randomly across the range
        points = [(random.randint(0, range_limit), random.randint(0, range_limit)) for _ in range(num_points)]
    return points

def generate_random_large_integers(digit_count):
    # Generate large random integers with the specified number of digits
    return random.randint(10**(digit_count - 1), 10**digit_count - 1)

# File directories for saving the samples
os.makedirs('closest_pair_inputs', exist_ok=True)
os.makedirs('integer_multiplication_inputs', exist_ok=True)

# Generate input files for the closest pair of points problem
for i in range(10):
    num_points = random.randint(100, 200)  # Number of points between 100 and 200
    range_limit = 1000
    
    # Create various complexities and edge cases
    if i < 3:
        points = generate_random_points(num_points, range_limit, clustered=False)
    elif i < 6:
        points = generate_random_points(num_points, range_limit, clustered=True)
    elif i < 8:
        # Points that align closely on a single line
        points = [(x, x) for x in range(num_points)]
    else:
        # Duplicate points edge case
        duplicate_point = (random.randint(0, range_limit), random.randint(0, range_limit))
        points = [duplicate_point for _ in range(num_points)]

    # Save points to a text file
    with open(f'closest_pair_inputs/points_input_{i+1}.txt', 'w') as f:
        for x, y in points:
            f.write(f"{x} {y}\n")

# Generate input files for the integer multiplication problem
for i in range(10):
    # Different complexities and edge cases for integer multiplication
    if i < 3:
        # Large random numbers
        num1 = generate_random_large_integers(100)
        num2 = generate_random_large_integers(100)
    elif i < 6:
        # Leading and trailing zero cases
        num1 = int(str(generate_random_large_integers(98)) + "00")
        num2 = int("00" + str(generate_random_large_integers(98)))
    else:
        # Extremely large numbers (up to 500 digits)
        num1 = generate_random_large_integers(500)
        num2 = generate_random_large_integers(500)
    
    # Save numbers to a text file
    with open(f'integer_multiplication_inputs/integers_input_{i+1}.txt', 'w') as f:
        f.write(f"{num1}\n{num2}\n")

print("Sample input files generated successfully.")
