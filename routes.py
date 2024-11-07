from flask import Blueprint, request, jsonify
import math

api = Blueprint('api', __name__)

# Euclidean distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Brute force solution for small number of points
def brute_force(points):
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist

# Recursive closest pair function using divide and conquer
def recursive_closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    Qx, Rx = px[:mid], px[mid:]
    Qy, Ry = [], []

    midpoint = px[mid][0]
    for point in py:
        if point[0] <= midpoint:
            Qy.append(point)
        else:
            Ry.append(point)

    (pair_left, dist_left) = recursive_closest_pair(Qx, Qy)
    (pair_right, dist_right) = recursive_closest_pair(Rx, Ry)

    if dist_left <= dist_right:
        min_dist = dist_left
        min_pair = pair_left
    else:
        min_dist = dist_right
        min_pair = pair_right

    strip = [point for point in py if abs(point[0] - midpoint) < min_dist]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (strip[i], strip[j])

    return min_pair, min_dist

# Closest Pair function (used by API)
def closest_pair(points):
    # Sort points based on x-coordinate
    points.sort(key=lambda p: p[0])

    # Sort points based on y-coordinate
    py = sorted(points, key=lambda p: p[1])

    return recursive_closest_pair(points, py)

@api.route('/closest-pair', methods=['POST'])
def api_closest_pair():
    data = request.json
    points = data.get("points")
    
    # Log the incoming data for debugging
    print("Parsed points:", points)
    
    # Ensure points are a valid list of tuples
    if not points or not all(isinstance(point, list) and len(point) == 2 for point in points):
        return jsonify({"error": "Invalid points data. Points should be an array of [x, y] pairs."}), 400
    
    try:
        result_pair, min_distance = closest_pair(points)
        return jsonify({
            "closest_pair": result_pair,
            "distance": min_distance
        })
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify({"error": str(e)}), 500

# Karatsuba integer multiplication
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high_x, low_x = divmod(x, 10**half)
    high_y, low_y = divmod(y, 10**half)

    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

@api.route('/integer-multiplication', methods=['POST'])
def api_integer_multiplication():
    data = request.json
    x = data.get("x")
    y = data.get("y")
    
    # Ensure both integers x and y are provided
    if x is None or y is None:
        return jsonify({"error": "Both integers x and y are required"}), 400
    
    try:
        result = karatsuba(x, y)
        return jsonify({
            "result": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
