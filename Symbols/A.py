import math
from Symbols.CalculateDistance import calculate_distance
from Symbols.FingersClosed import fingers_closed
from Symbols.CalculateAngle import calculate_angle

# Function to classify the "A" gesture
def classify_a_gesture(landmarks1, landmarks2, h, w):
    try:
        thumb_tip_1 = landmarks1[4]
        thumb_tip_2 = landmarks2[4]

        # Calculate distance between the thumb tips of both hands
        distance_threshold = calculate_distance(landmarks1[1],landmarks1[2])/1.25   # Adjust this threshold as needed

        # Initialize a list to track correctness of landmarks
        correct1 = [1] * 21
        correct2 = [1] * 21

        distance = calculate_distance(thumb_tip_1, thumb_tip_2)

        angle=calculate_angle(landmarks1[3],landmarks1[4],landmarks2[3])
        # Check if the thumb tips of both hands are touching and all other fingers are closed
        if distance < distance_threshold and fingers_closed(landmarks1) and fingers_closed(landmarks2) :
            if landmarks1[4].y > landmarks1[1].y:
                for i in range(2, 5):
                        correct1[i] = 0
                a = sum(correct1) + sum(correct2)
                accuracy = (a / 42) * 100
                return "Not A", correct1, correct2, accuracy
            if landmarks2[4].y > landmarks2[1].y:
                for i in range(2, 5):
                        correct2[i] = 0
                a = sum(correct1) + sum(correct2)
                accuracy = (a / 42) * 100
                return "Not A", correct1, correct2, accuracy
            a = sum(correct1) + sum(correct2)
            accuracy = (a / 42) * 100 

            return "A", correct1, correct2, accuracy
        else:
            if landmarks1[5].y < landmarks1[0].y:
                if landmarks1[8].y < landmarks1[5].y:
                    for i in range(6, 9):
                        correct1[i] = 0  # Index tip of hand 1
                if landmarks1[12].y < landmarks1[9].y:
                    for i in range(10, 13):
                        correct1[i] = 0  # middle tip of hand 1
                if landmarks1[16].y < landmarks1[13].y:
                    for i in range(14, 17):
                        correct1[i] = 0  # ring tip of hand 1
                if landmarks1[20].y < landmarks1[17].y:
                    for i in range(18, 21):
                        correct1[i] = 0  # pinky tip of hand 1

                if landmarks2[8].y < landmarks2[5].y:
                    for i in range(6, 9):
                        correct2[i] = 0  # Index tip of hand 2
                if landmarks2[12].y < landmarks2[9].y:
                    for i in range(10, 13):
                        correct2[i] = 0  # middle tip of hand 2
                if landmarks2[16].y < landmarks2[13].y:
                    for i in range(14, 17):
                        correct2[i] = 0  # ring tip of hand 2
                if landmarks2[20].y < landmarks2[17].y:
                    for i in range(18, 21):
                        correct2[i] = 0  # pinky tip of hand 2

            #inverted hands
            if landmarks1[5].y > landmarks1[0].y:
                if landmarks1[8].y > landmarks1[7].y:
                    for i in range(6, 9):
                        correct1[i] = 0  # Index tip of hand 1
                if landmarks1[12].y > landmarks1[11].y:
                    for i in range(10, 13):
                        correct1[i] = 0  # middle tip of hand 1
                if landmarks1[16].y > landmarks1[15].y:
                    for i in range(14, 17):
                        correct1[i] = 0  # ring tip of hand 1
                if landmarks1[20].y > landmarks1[19].y:
                    for i in range(18, 21):
                        correct1[i] = 0  # pinky tip of hand 1

                if landmarks2[8].y > landmarks2[7].y:
                    for i in range(6, 9):
                        correct2[i] = 0  # Index tip of hand 2
                if landmarks2[12].y > landmarks2[11].y:
                    for i in range(10, 13):
                        correct2[i] = 0  # middle tip of hand 2
                if landmarks2[16].y > landmarks2[15].y:
                    for i in range(14, 17):
                        correct2[i] = 0  # ring tip of hand 2
                if landmarks2[20].y > landmarks2[19].y:
                    for i in range(18, 21):
                        correct2[i] = 0  # pinky tip of hand 2

                if landmarks1[4].y > landmarks1[3].y:
                    for i in range(2, 5):
                            correct1[i] = 0
                if landmarks2[4].y > landmarks2[3].y:
                    for i in range(2, 5):
                            correct2[i] = 0
             
            if landmarks1[4].y > landmarks1[3].y:
                for i in range(2, 5):
                        correct1[i] = 0
            if landmarks2[4].y > landmarks2[3].y:
                for i in range(2, 5):
                        correct2[i] = 0

            if distance >= distance_threshold:
                    for i in range(2, 5):
                        correct1[i] = 0
                        correct2[i] = 0
            a = sum(correct1) + sum(correct2)
            accuracy = (a / 42) * 100
            print(angle)
            return "Not A", correct1, correct2, accuracy
    except IndexError as e:
        print(f"IndexError in classify_a_gesture: {e}")
        return "Error", [0]*21, [0]*21, 0