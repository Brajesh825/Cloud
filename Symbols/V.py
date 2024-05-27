from Symbols.Calculate2DAngle import calculate_2d_angle

def classify_v_gesture(landmarks,landmarks2, h, w):
    # Extract landmarks for fingers, thumb, and wrist
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    index_dip = landmarks[7]
    index_mcp = landmarks[5]

    middle_tip = landmarks[12]
    middle_dip = landmarks[11]
    middle_pip = landmarks[10]
    middle_mcp = landmarks[9]

    ring_tip = landmarks[16]
    ring_dip = landmarks[15]
    ring_pip = landmarks[14]
    ring_mcp = landmarks[13]
    
    pinky_tip = landmarks[20]
    pinky_dip = landmarks[19]
    pinky_mcp = landmarks[17]
    wrist = landmarks[0]

    a2 = calculate_2d_angle(index_tip, index_mcp, wrist, index_mcp, h, w)

    # Calculate distances from wrist to finger MCP joints
    w_middle_mcp = wrist['y'] - middle_mcp['y']
    if(w_middle_mcp < 0):
        w_middle_mcp = -w_middle_mcp
    
    w_middle_tip = wrist['y'] - middle_tip['y']
    if(w_middle_tip < 0):
        w_middle_tip = -w_middle_tip

    w_middle_dip = wrist['y'] - middle_dip['y']
    if(w_middle_dip < 0):
        w_middle_dip = -w_middle_dip
    
    w_ring_mcp = wrist['y'] - ring_mcp['y']
    if(w_ring_mcp < 0):
        w_ring_mcp = -w_ring_mcp
    
    w_ring_tip = wrist['y'] - ring_tip['y']
    if(w_ring_tip < 0):
        w_ring_tip = -w_ring_tip

    w_ring_dip = wrist['y'] - ring_dip['y']
    if(w_ring_dip < 0):
        w_ring_dip = -w_ring_dip

    w_pinky_mcp = wrist['y'] - pinky_mcp['y']
    if(w_pinky_mcp < 0):
        w_pinky_mcp = -w_pinky_mcp
    
    w_pinky_tip = wrist['y'] - pinky_tip['y']
    if(w_pinky_tip < 0):
        w_pinky_tip = -w_pinky_tip

    w_pinky_dip = wrist['y'] - pinky_dip['y']
    if(w_pinky_dip < 0):
        w_pinky_dip = -w_pinky_dip

    w_index_tip = wrist['y'] - index_tip['y']
    if(w_index_tip < 0):
        w_index_tip = -w_index_tip

    w_index_dip = wrist['y'] - index_dip['y']
    if(w_index_dip < 0):
        w_index_dip = -w_index_dip

    # Initialize a list to track correctness of landmarks
    correct = [0]*21
    correct[0] = 1
    correct[1] = 1
    correct[5] = 1
    correct[9] = 1
    correct[13] = 1
    correct[17] = 1
    
    # Classify based on angles and distances
    for i in range(6,9):
        correct[i] = 1
        
    if a2 < 160:
        for i in range(2, 5):
            correct[i] = 1
    
    if (w_middle_mcp > w_ring_tip):
        for i in range(14, 17):
            correct[i] = 1
    
    if (w_middle_mcp > w_pinky_tip):
        for i in range(18, 21):
            correct[i] = 1
    
    if (w_index_dip < w_index_tip):
        for i in range(6, 9):
            correct[i] = 1
    
    if (w_middle_dip < w_middle_tip):
        for i in range(10, 13):
            correct[i] = 1

    d1 = (ring_dip['y'] - ring_pip['y'])**2 + (ring_dip['x'] - ring_pip['x'])**2
    d2 = (index_tip['y'] - middle_tip['y'])**2 + (index_tip['x'] - middle_tip['x'])**2

    if d2 < d1:
        for i in range(9):
            correct[i] = 0

    a = 0
    for i in range(21):
        a = a + correct[i]
        
    accuracy = (a / 21) * 100
    
    if a == 21:
        return "V", accuracy, correct, correct
    else:
        return "Not V", accuracy, correct, correct
