import cv2
import mediapipe as mp

# Ініціалізація модулів MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Налаштування моделі
# max_num_hands=1: для керування курсором нам зазвичай потрібна одна рука
# min_detection_confidence=0.5: поріг впевненості (50%)
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Запуск камери
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        break

    # 1. Віддзеркалення зображення (Flip)
    # Це критично для зручності користувача. Коли ви рухаєте руку вправо, 
    # на екрані вона теж має рухатися вправо (як у дзеркалі).
    img = cv2.flip(img, 1)

    # 2. Конвертація в RGB для MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 3. Інференс (отримання результатів)
    results = hands.process(img_rgb)
    h, w, c = img.shape 

    # Якщо руки знайдені
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            # Перебір усіх 21 точок
            for id, lm in enumerate(hand_landmarks.landmark):
                # id - номер точки (0, 1, ... 20)
                # lm - об'єкт з координатами .x, .y, .z
                
                # Нас цікавить тільки вказівний палець (ID 8)
                if id == 8:
                    # ПЕРЕТВОРЕННЯ КООРДИНАТ (Нормалізація -> Пікселі)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    
                    print(f"ID: {id}, X: {cx}, Y: {cy}")
                    
                    # Візуалізація: малюємо велику точку на кінчику пальця
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # Малюємо скелет руки повністю (для наочності)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand_landmarks.landmark):
                if id == 4:
                    # ПЕРЕТВОРЕННЯ КООРДИНАТ (Нормалізація -> Пікселі)
                    vx, vy = int(lm.x * w), int(lm.y * h)
                    
                    print(f"ID: {id}, X: {vx}, Y: {vy}")
                    
                    # Візуалізація: малюємо велику точку на кінчику пальця
                    cv2.circle(img, (vx, vy), 15, (255, 0, 255), cv2.FILLED)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


