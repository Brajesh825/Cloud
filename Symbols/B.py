from Symbols.CalculateDistance import calculate_distance


def classify_b_gesture(landmarks1, landmarks2):
    try:
        thumb_tip_1 = landmarks1[4]
        index_tip_1 = landmarks1[8]
        middle_tip_1 = landmarks1[12]
        ring_tip_1 = landmarks1[16]
        pinky_tip_1 = landmarks1[20]

        thumb_tip_2 = landmarks2[4]
        index_tip_2 = landmarks2[8]
        middle_tip_2 = landmarks2[12]
        ring_tip_2 = landmarks2[16]
        pinky_tip_2 = landmarks2[20]

        # Calculate distances between thumbs and index fingers
        distance_threshold = calculate_distance(landmarks1[1],landmarks1[2])/1.25  # Adjust this threshold as needed
        distance_1_1 = calculate_distance(thumb_tip_1, index_tip_1)
        distance_1_2 = calculate_distance(thumb_tip_1, middle_tip_1)
        distance_1_3 = calculate_distance(thumb_tip_1, ring_tip_1)
        distance_1_4 = calculate_distance(thumb_tip_1, pinky_tip_1)

        distance_2_1 = calculate_distance(thumb_tip_2, index_tip_2)
        distance_2_2 = calculate_distance(thumb_tip_2, middle_tip_2)
        distance_2_3 = calculate_distance(thumb_tip_2, ring_tip_2)
        distance_2_4 = calculate_distance(thumb_tip_2, pinky_tip_2)

        # Initialize a list to track correctness of landmarks
        correct1 = [1] * 21
        correct2 = [1] * 21    

        

        # Check if both thumbs are touching their corresponding index fingers
        if distance_1_1 < distance_threshold and distance_1_2 < distance_threshold and distance_1_3 < distance_threshold and distance_1_4 < distance_threshold and distance_2_1 < distance_threshold and distance_2_2 < distance_threshold and distance_2_3 < distance_threshold and distance_2_4 < distance_threshold:
            distance_between_hands = calculate_distance(thumb_tip_1, thumb_tip_2)
            if distance_between_hands < distance_threshold:
                a = sum(correct1) + sum(correct2)
                accuracy = (a / 42) * 100                
                return "B", correct1, correct2, accuracy

   
        else:
            if not distance_1_1 < distance_threshold:
                for i in range(6, 9):
                    correct1[i] = 0  # Index tip of hand 1
            if not distance_1_2 < distance_threshold:
                for i in range(10, 13):
                    correct1[i] = 0  # Middle tip of hand 1
            if not distance_1_3 < distance_threshold:
                for i in range(14, 17):
                    correct1[i] = 0  # Ring tip of hand 1
            if not distance_1_4 < distance_threshold:
                for i in range(18, 21):
                    correct1[i] = 0  # Pinky tip of hand 1
            if not distance_2_1 < distance_threshold:
                for i in range(6, 9):
                    correct2[i] = 0  # Index tip of hand 2
            if not distance_2_2 < distance_threshold:
                for i in range(10, 13):
                    correct2[i] = 0  # Middle tip of hand 2
            if not distance_2_3 < distance_threshold:
                for i in range(14, 17):
                    correct2[i] = 0  # Ring tip of hand 2
            if not distance_2_4 < distance_threshold:
                for i in range(18, 21):
                    correct2[i] = 0  # Pinky tip of hand 2
            if not calculate_distance(thumb_tip_1, thumb_tip_2) < 0.1:
                for i in range(2, 5):
                    correct1[i] = 0
                    correct2[i] = 0
            a = sum(correct1) + sum(correct2)
            accuracy = (a / 42) * 100 
            return "Not B", correct1, correct2, accuracy
    except Exception as e:
        print(f"Error in classify_b_gesture: {e}")
        return "Error", [0] * 21, [0] * 21, 0
