import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
ROI_SIZE = 400

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape 

    rx1, ry1 = (w - ROI_SIZE) // 2, (h - ROI_SIZE) // 2
    rx2, ry2 = rx1 + ROI_SIZE, ry1 + ROI_SIZE
    cv2.rectangle(img, (rx1, ry1), (rx2, ry2), (255, 255, 0), 2)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            tip = landmarks[8]
            pip = landmarks[6]
            cx, cy = int(tip.x * w), int(tip.y * h)
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

            in_roi = (rx1 < cx < rx2) and (ry1 < cy < ry2)
            is_touching = tip.y < pip.y 

            if in_roi and is_touching:
                scaled_norm_x = (cx - rx1) / ROI_SIZE
                scaled_norm_y = (cy - ry1) / ROI_SIZE
                print(f"TOUCH DETECTED at MAP NORM: (X: {scaled_norm_x:.2f}, Y: {scaled_norm_y:.2f})")
                text = f"T.D.A.M.N. X: {scaled_norm_x:.2f}, Y: {scaled_norm_y:.2f}"
                cv2.putText(img, text, (cx + 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking Lab", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()