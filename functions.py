import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
import shutil

matplotlib.use('Agg')

custom_font = font_manager.FontProperties(fname="static/fonts/Poppins-Bold.ttf")

# Path to the plots folder
plots_folder = "static/plots/"

# Step 0: Clear the 'plots' folder before starting
def clear_plots_folder():
    if os.path.exists(plots_folder):
        # Remove all files in the plots folder
        for filename in os.listdir(plots_folder):
            file_path = os.path.join(plots_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    if not os.path.exists("static/plots"):
        os.makedirs("static/plots")

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['txt']

# Save the uploaded file to the 'uploads' folder
def save_file(file):
    filename = f"uploads/{file.filename}"
    file.save(filename)
    return filename

# Parse points from the uploaded file
def parse_points_from_file(filepath):
    points = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            coords = list(map(int, line.strip().split()))
            points.append(coords)
    return points

# Brute force method to find the closest pair when there are 3 or fewer points
def brute_force(points):
    min_dist = float('inf')
    closest_pair = None
    n = len(points)
    
    # Check all pairs and find the minimum distance
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = [points[i], points[j]]
    
    return closest_pair, min_dist

# Calculate the closest pair using divide and conquer algorithm
def closest_pair_algorithm(points):
    points_sorted_by_x = sorted(points, key=lambda point: point[0])
    points_sorted_by_y = sorted(points, key=lambda point: point[1])
    return closest_pair_rec(points_sorted_by_x, points_sorted_by_y)

def closest_pair_rec(sorted_by_x, sorted_by_y, step=0):
    n = len(sorted_by_x)
    if n <= 3:
        closest_pair, min_dist = brute_force(sorted_by_x)
        plot_closest_pair(sorted_by_x, closest_pair, min_dist, f"{plots_folder}step_{step}.png")
        return closest_pair, min_dist

    mid = n // 2
    left_x = sorted_by_x[:mid]
    right_x = sorted_by_x[mid:]

    left_y = [point for point in sorted_by_y if point[0] <= left_x[-1][0]]
    right_y = [point for point in sorted_by_y if point[0] > left_x[-1][0]]

    left_pair, left_dist = closest_pair_rec(left_x, left_y, step + 1)
    right_pair, right_dist = closest_pair_rec(right_x, right_y, step + 1)

    # Find the closest pair across the divide
    if left_dist < right_dist:
        closest_pair = left_pair
        min_dist = left_dist
    else:
        closest_pair = right_pair
        min_dist = right_dist

    # Check the strip area
    strip = [point for point in sorted_by_y if abs(point[0] - sorted_by_x[mid][0]) < min_dist]
    strip_pair, strip_dist = closest_strip(strip, min_dist)

    if strip_dist < min_dist:
        closest_pair = strip_pair
        min_dist = strip_dist

    # Save the plot at the current recursive step
    plot_closest_pair(sorted_by_x, closest_pair, min_dist, f"{plots_folder}step_{step}.png")

    return closest_pair, min_dist

# Function to check closest pair in the strip (vertical line area)
def closest_strip(strip, d):
    min_dist = d
    closest_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = [strip[i], strip[j]]
    return closest_pair, min_dist

# Function to calculate distance between two points
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Function to plot the points and the closest pair with a neon glow effect
def plot_closest_pair(points, closest_pair, distance, filename=f"static/plots/step_0.png"):
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]
    
    # Create a figure with dark background
    fig, ax = plt.subplots(figsize=(9, 7))
    fig.patch.set_facecolor('#0a0a0a')  # Dark background for neon effect
    ax.set_facecolor('#1a1a1a')         # Slightly lighter background for the plot area

    # Neon colors
    neon_blue = '#00f5ff'
    neon_purple = '#d400ff'
    neon_green = '#39ff14'

    # Plot a "glow" effect by layering larger and more transparent points behind
    for glow_size, alpha in [(40, 0.03), (30, 0.05), (20, 0.08), (10, 0.1)]:
        plt.scatter(x_vals, y_vals, color=neon_blue, s=glow_size, alpha=alpha, edgecolors='none')
    plt.scatter(x_vals, y_vals, color=neon_blue, s=8, label="Points", edgecolors='none')  # Main layer of points

    # Highlight the closest pair with an extra neon effect
    if closest_pair:
        x_vals_pair = [closest_pair[0][0], closest_pair[1][0]]
        y_vals_pair = [closest_pair[0][1], closest_pair[1][1]]
        
        # Add multiple lines for the glow effect around the closest pair
        for glow_width, alpha in [(8, 0.05), (6, 0.1), (4, 0.2)]:
            plt.plot(x_vals_pair, y_vals_pair, color=neon_green, linestyle='-', linewidth=glow_width, alpha=alpha)
        
        plt.plot(x_vals_pair, y_vals_pair, color=neon_green, linestyle='-', linewidth=2, label="Closest Pair")

        # Add glow effect around closest points with circles
        for size, alpha in [(100, 0.05), (80, 0.1), (60, 0.15)]:
            plt.scatter(x_vals_pair, y_vals_pair, s=size, color=neon_purple, alpha=alpha, edgecolors='none')
        plt.scatter(x_vals_pair, y_vals_pair, s=20, color=neon_purple, label="Closest Points")

        # Label the endpoints with coordinates in brackets
        for i, point in enumerate(closest_pair):
            plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color=neon_green, fontsize=10, ha='right' if i == 0 else 'left', va='bottom')

    # Draw a vertical line dividing the plot into two parts (divide and conquer partition)
    # Use the x-coordinate of the midpoint
    mid_x = (sorted(points, key=lambda point: point[0])[len(points)//2][0])
    plt.axvline(x=mid_x, color='orange', linestyle='--', label="Divide Line", linewidth=2)

    # Set labels and title with neon colors
    plt.title(f"Closest Pair (Distance: {distance:.2f})", color=neon_green, fontproperties=custom_font, fontsize=12)
    plt.xlabel("X-axis", color=neon_purple, fontproperties=custom_font, fontsize=12)
    plt.ylabel("Y-axis", color=neon_purple, fontproperties=custom_font, fontsize=12)
    
    # Adjust ticks to neon color
    ax.tick_params(axis='x', colors=neon_blue)
    ax.tick_params(axis='y', colors=neon_blue)

    # Show legend with neon colors
    legend = plt.legend()
    legend.get_frame().set_facecolor('#424242')
    for text in legend.get_texts():
        text.set_color(neon_green)

    # Save the plot
    plt.savefig(filename, facecolor=fig.get_facecolor())
    plt.close()
