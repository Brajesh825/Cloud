from Symbols.CalculateDistance import calculate_distance


# Function to classify the "B" gesture
def classify_b_gesture(landmarks1, landmarks2, h, w):
    thumb_tip_1 = landmarks1[4]
    index_tip_1 = landmarks1[8]
    middle_tip_1 = landmarks1[12]
    ring_tip_1 = landmarks1[16]
    pinki_tip_1 = landmarks1[20]

    thumb_tip_2 = landmarks2[4]
    index_tip_2 = landmarks2[8]
    middle_tip_2 = landmarks2[12]
    ring_tip_2 = landmarks2[16]
    pinki_tip_2 = landmarks2[20]

    # Calculate distances between thumbs and index fingers
    distance_threshold = 0.2  # You can adjust this threshold based on your preference
    distance_1_1 = calculate_distance(thumb_tip_1, index_tip_1)
    distance_1_2 = calculate_distance(thumb_tip_1, middle_tip_1)
    distance_1_3 = calculate_distance(thumb_tip_1, ring_tip_1)
    distance_1_4 = calculate_distance(thumb_tip_1, pinki_tip_1)

    distance_2_1 = calculate_distance(thumb_tip_2, index_tip_2)
    distance_2_2 = calculate_distance(thumb_tip_2, middle_tip_2)
    distance_2_3 = calculate_distance(thumb_tip_2, ring_tip_2)
    distance_2_4 = calculate_distance(thumb_tip_2, pinki_tip_2)

    # Initialize a list to track correctness of landmarks
    correct1 = [1] * 21
    correct2 = [1] * 21

    # Calculate and display distances
    distances1 = [
        calculate_distance(landmarks1[4], landmarks1[8]),
        calculate_distance(landmarks1[4], landmarks1[12]),
        calculate_distance(landmarks1[4], landmarks1[16]),
        calculate_distance(landmarks1[4], landmarks1[20]),
    ]
    distances2 = [
        calculate_distance(landmarks2[4], landmarks2[8]),
        calculate_distance(landmarks2[4], landmarks2[12]),
        calculate_distance(landmarks2[4], landmarks2[16]),
        calculate_distance(landmarks2[4], landmarks2[20]),
    ]

    # Calculate averages
    accuracy = 100 - ((sum(distances1) + sum(distances2)) * 100 / (len(distances1) + len(distances2)))

    # Check if both thumbs are touching their corresponding index fingers
    if (distance_1_1 < distance_threshold
            and distance_1_2 < distance_threshold
            and distance_1_3 < distance_threshold
            and distance_1_4 < distance_threshold
            and distance_2_1 < distance_threshold
            and distance_2_2 < distance_threshold
            and distance_2_3 < distance_threshold
            and distance_2_4 < distance_threshold):

        distance_between_hands = calculate_distance(thumb_tip_1, thumb_tip_2)
        if distance_between_hands < distance_threshold:
            return "B", correct1, correct2, accuracy

    else:
        if not distance_1_1 < distance_threshold:
            for i in range(6, 9):
                correct1[i] = 0  # Index tip of hand 1
        if not distance_1_2 < distance_threshold:
            for i in range(10, 13):
                correct1[i] = 0  # middle tip of hand 1
        if not distance_1_3 < distance_threshold:
            for i in range(14, 17):
                correct1[i] = 0  # ring tip of hand 1
        if not distance_1_4 < distance_threshold:
            for i in range(18, 21):
                correct1[i] = 0  # pinki tip of hand 1
        if not distance_2_1 < distance_threshold:
            for i in range(6, 9):
                correct2[i] = 0  # Index tip of hand 2
        if not distance_2_2 < distance_threshold:
            for i in range(10, 13):
                correct2[i] = 0  # middle tip of hand 2
        if not distance_2_3 < distance_threshold:
            for i in range(14, 17):
                correct2[i] = 0  # ring tip of hand 2
        if not distance_2_4 < distance_threshold:
            for i in range(18, 21):
                correct2[i] = 0  # pinki tip of hand 2
        if not calculate_distance(thumb_tip_1, thumb_tip_2) < 0.1:
            for i in range(2, 5):
                correct1[i] = 0
                correct2[i] = 0
        return "Not B", accuracy, correct1, correct2

