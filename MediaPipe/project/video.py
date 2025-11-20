import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
h = mp_draw.DrawingSpec(color=(0, 0, 0), thickness=2)  
l = mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4) 

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    c = 0

    if results.multi_hand_landmarks:
        c = len(results.multi_hand_landmarks)
        for hand_landmarks in results.multi_hand_landmarks:mp_draw.draw_landmarks(image=frame,landmark_list=hand_landmarks,connections=mp_hands.HAND_CONNECTIONS,landmark_drawing_spec=l,connection_drawing_spec=h)

    cv2.putText(frame,f'Hands detected: {c}',(10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0),1)

    cv2.imshow('Hands Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







