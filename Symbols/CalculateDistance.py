import math

def calculate_distance(landmark1, landmark2):
    return math.sqrt((landmark1['x'] - landmark2['x'])**2 + (landmark1['y'] - landmark2['y'])**2)