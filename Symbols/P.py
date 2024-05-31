from Symbols.CalculateDistance import calculate_distance


def classify_p_gesture(landmarks1, landmarks2, h, w):
    thumb_tip_1 = landmarks1[4]
    index_tip_1 = landmarks1[8]
    thumb_tip_2 = landmarks2[4]
    index_tip_2 = landmarks2[8]

    # Calculate the distance threshold
    distance_threshold = calculate_distance(landmarks1[1],landmarks1[2])/1.25 

    # Initialize a list to track correctness of landmarks
    correct1 = [1] * 21
    correct2 = [1] * 21

    # Calculate accuracy as the minimum distance between index fingers and thumbs
    index_finger_1_thumb_1_dist = calculate_distance(landmarks1[4], landmarks1[8])
    index_finger_2_thumb_1_dist = calculate_distance(landmarks2[4], landmarks1[8])

    min_dist = min(index_finger_1_thumb_1_dist, index_finger_2_thumb_1_dist)
    accuracy = 100 - (min_dist * 100)


    # Check if the index finger of both hands is touching either hand's thumb
    if (calculate_distance(index_tip_1, thumb_tip_1) < distance_threshold and calculate_distance(index_tip_2, thumb_tip_1) < distance_threshold) :
        a = sum(correct1) + sum(correct2)
        accuracy = (a / 42) * 100 
        if landmarks2[12].y < landmarks2[9].y or landmarks2[16].y < landmarks2[13].y or landmarks2[20].y < landmarks2[17].y or landmarks1[12].y < landmarks1[9].y or landmarks1[16].y < landmarks1[13].y or landmarks1[20].y < landmarks1[17].y:
            if landmarks2[12].y < landmarks2[9].y:
                for i in range(10, 13):
                    correct2[i] = 0  # middle tip of hand 2
            if landmarks2[16].y < landmarks2[13].y:
                for i in range(14, 17):
                    correct2[i] = 0  # ring tip of hand 2
            if landmarks2[20].y < landmarks2[17].y:
                for i in range(18, 21):
                    correct2[i] = 0  # pinky tip of hand 2
            if landmarks1[12].y < landmarks1[9].y:
                for i in range(10, 13):
                    correct1[i] = 0  # middle tip of hand 1
            if landmarks1[16].y < landmarks1[13].y:
                for i in range(14, 17):
                    correct1[i] = 0  # ring tip of hand 1
            if landmarks1[20].y < landmarks1[17].y:
                for i in range(18, 21):
                    correct1[i] = 0  # pinky tip of hand 1
            a = sum(correct1) + sum(correct2)
            accuracy = (a / 42) * 100 
            return "Not P", correct1, correct2 ,accuracy

        return "P", correct1, correct2 ,accuracy
    else:

        if landmarks2[12].y < landmarks2[9].y:
            for i in range(10, 13):
                correct2[i] = 0  # middle tip of hand 2
        if landmarks2[16].y < landmarks2[13].y:
            for i in range(14, 17):
                correct2[i] = 0  # ring tip of hand 2
        if landmarks2[20].y < landmarks2[17].y:
            for i in range(18, 21):
                correct2[i] = 0  # pinky tip of hand 2
        if landmarks1[12].y < landmarks1[9].y:
            for i in range(10, 13):
                correct1[i] = 0  # middle tip of hand 1
        if landmarks1[16].y < landmarks1[13].y:
            for i in range(14, 17):
                correct1[i] = 0  # ring tip of hand 1
        if landmarks1[20].y < landmarks1[17].y:
            for i in range(18, 21):
                correct1[i] = 0  # pinky tip of hand 1

        # Mark relevant landmarks as incorrect
        for i in range(6, 9):
            correct2[i] = 0  # Index tip of hand 2

        for i in range(6, 9):
            correct1[i] = 0  # Index tip of hand 1
    
        for i in range(2, 5):
            correct1[i] = 0  # Thumb tip of hand 1

        a = sum(correct1) + sum(correct2)
        accuracy = (a / 42) * 100 

        return "Not P", correct1, correct2 ,accuracy
