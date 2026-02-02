import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.INDEX_FINGER_TIP_ID = 8

    def process(self, image_rgb):
        return self.hands.process(image_rgb)
    
    def close(self):
        self.hands.close()