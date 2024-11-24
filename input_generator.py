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
point_counts = range(100, 901, 100)  # 100 to 800 points in increments of 100
for i, num_points in enumerate(point_counts):
    range_limit = 1000
    # Create points with random distribution
    points = generate_random_points(num_points, range_limit, clustered=False)

    # Save points to a text file
    with open(f'closest_pair_inputs/points_input_{num_points}.txt', 'w') as f:
        for x, y in points:
            f.write(f"{x} {y}\n")

# Generate input files for the integer multiplication problem
digit_counts = range(10, 101, 10)  # 10 to 100 digits in increments of 10
for i, digit_count in enumerate(digit_counts):
    # Generate large random numbers
    num1 = generate_random_large_integers(digit_count)
    num2 = generate_random_large_integers(digit_count)
    
    # Save numbers to a text file
    with open(f'integer_multiplication_inputs/integers_input_{digit_count}_digits.txt', 'w') as f:
        f.write(f"{num1}\n{num2}\n")

print("Sample input files generated successfully.")
