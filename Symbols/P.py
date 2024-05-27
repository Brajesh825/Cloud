from Symbols.CalculateDistance import calculate_distance


def classify_p_gesture(landmarks1, landmarks2, h, w):
    thumb_tip_1 = landmarks1[4]
    index_tip_1 = landmarks1[8]
    thumb_tip_2 = landmarks2[4]
    index_tip_2 = landmarks2[8]

    # Calculate the distance threshold
    distance_threshold = 0.1

    # Initialize a list to track correctness of landmarks
    correct1 = [1] * 21
    correct2 = [1] * 21

    # Check if the index finger of both hands is touching either hand's thumb
    if (calculate_distance(index_tip_1, thumb_tip_1) < distance_threshold and calculate_distance(index_tip_2,
                                                                                                 thumb_tip_1) < distance_threshold) or \
            (calculate_distance(index_tip_1, thumb_tip_2) < distance_threshold and calculate_distance(index_tip_2,
                                                                                                      thumb_tip_2) < distance_threshold):  # Mark relevant landmarks as correct
        return "P", 100, correct1, correct2
    else:
        # Mark relevant landmarks as incorrect
        for i in range(6, 9):
            correct2[i] = 0  # Index tip of hand 2

        for i in range(6, 9):
            correct1[i] = 0  # Index tip of hand 1

        for i in range(2, 5):
            correct1[i] = 0  # Thumb tip of hand 1

        return "Not P", 100, correct1, correct2
