from Symbols.CalculateDistance import calculate_distance

def fingers_closed(landmarks, threshold=0.1):
    finger_tips = [landmarks[i] for i in [8, 12, 16, 20]]  # Tips of index, middle, ring, and pinky fingers
    finger_mcp = [landmarks[i] for i in [5, 9, 13, 17]]    # MCP joints of index, middle, ring, and pinky fingers

    return all(calculate_distance(tip, mcp) < threshold for tip, mcp in zip(finger_tips, finger_mcp))