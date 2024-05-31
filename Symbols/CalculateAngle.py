import math

def calculate_angle(point1, point2, point3):
    # Calculate vectors
    vec1 = [point1['x'] - point2['x'], point1['y'] - point2['y']]
    vec2 = [point3['x'] - point2['x'], point3['y'] - point2['y']]
    
    # Calculate dot product
    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    
    # Calculate magnitudes
    mag1 = math.sqrt(vec1[0]**2 + vec1[1]**2)
    mag2 = math.sqrt(vec2[0]**2 + vec2[1]**2)
    
    # Calculate angle in radians
    radians = math.acos(dot_product / (mag1 * mag2))
    
    # Convert radians to degrees
    angle = math.degrees(radians)
    
    return angle