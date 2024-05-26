import math
from Symbols.CalculateDistance import calculate_distance
from Symbols.FingersClosed import fingers_closed

def classify_a_gesture(landmarks1, landmarks2, h, w):
    thumb_tip_1 = landmarks1[4]
    thumb_tip_2 = landmarks2[4]

    # Calculate distance between the thumb tips of both hands
    distance_threshold = 0.15  # Adjust this threshold as needed

    # Initialize a list to track correctness of landmarks
    correct1 = [1] * 21
    correct2 = [1] * 21

    distance = calculate_distance(thumb_tip_1, thumb_tip_2)

    # Check if the thumb tips of both hands are touching and all other fingers are closed
    if distance < distance_threshold and fingers_closed(landmarks1) and fingers_closed(landmarks2):
        accuracy = 100 - (distance * 100 / 2)
        
        return "A", correct1, correct2, accuracy
    else:
        if not fingers_closed(landmarks1):
            for i in range(6, 9):
                correct1[i] = 0  # Index tip of hand 1
            for i in range(10, 13):
                correct1[i] = 0  # middle tip of hand 1
            for i in range(14, 17):
                correct1[i] = 0  # ring tip of hand 1
            for i in range(18, 21):
                correct1[i] = 0  # pinky tip of hand 1

        if not fingers_closed(landmarks2):
            for i in range(6, 9):
                correct2[i] = 0  # Index tip of hand 2
            for i in range(10, 13):
                correct2[i] = 0  # middle tip of hand 2
            for i in range(14, 17):
                correct2[i] = 0  # ring tip of hand 2
            for i in range(18, 21):
                correct2[i] = 0  # pinky tip of hand 2

        if distance >= distance_threshold:
            for i in range(2, 5):
                correct1[i] = 0
                correct2[i] = 0
        if fingers_closed(landmarks1) or fingers_closed(landmarks2):
            accuracy = 50
        elif not fingers_closed(landmarks1) and not fingers_closed(landmarks2):
            accuracy = 0
        else:
            accuracy = 0  # Set accuracy to 0 when the gesture is not "A"
        return "Not A", accuracy, correct1, correct2