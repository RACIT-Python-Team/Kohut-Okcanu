import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import threading  
def speak_function(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except:
        pass
def speak(text):
    # daemon=True завершує потік автоматично
    threading.Thread(target=speak_function, args=(detected_zone,)).start()

# Ініціалізація модулів MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5)

# --- 1. Конфігурація Інтерактивних Зон (Нормалізовані Координати) ---
# [min_x, min_y, max_x, max_y] від 0.0 до 1.0 на самому макеті
INTERACTIVE_ZONES = [
    {"name": "hall", "norm_coords": [0.15, 0.11, 0.89, 0.28], "color": (79, 168, 128)},
    {"name": "1 audience", "norm_coords": [0.15, 0.29, 0.43, 0.44], "color": (133, 52, 52)},
    {"name": "2 audience", "norm_coords": [0.15, 0.46, 0.43, 0.59], "color": (0, 0, 0)},
    {"name": "3 audience", "norm_coords": [0.15, 0.60, 0.43, 0.89], "color": (168, 141, 79)},
    {"name": "4 audience", "norm_coords": [0.60, 0.30, 0.90, 0.41], "color": (79, 168, 159)},
    {"name": "5 audience", "norm_coords": [0.60, 0.42, 0.90, 0.60], "color": (41, 140, 186)},
    {"name": "corridor", "norm_coords": [0.44, 0.28, 0.60, 0.73], "color": (46, 41, 186)},
    {"name": "corridor", "norm_coords": [0.61, 0.60, 0.90, 0.68], "color": (46, 41, 186)},
    {"name": "6 audience", "norm_coords": [0.45, 0.71, 0.90, 0.90], "color": (157, 36, 201)},
    {"name": "6 audience", "norm_coords": [0.61, 0.68, 0.90, 0.90], "color": (157, 36, 201)}
    ]
INDEX_FINGER_TIP_ID = 8

# --- 2. Функція для створення віртуального макета (заглушка) ---
def create_virtual_map(W, H): 
    map_img = cv2.imread("mapa.jpg")
    map_img = cv2.resize(map_img, (W, H))
    return map_img

# --- 3. Основний цикл обробки ---
cap = cv2.VideoCapture(0)

# Глобальні налаштування ROI
ROI_WIDTH_PERCENT = 0.7 
ROI_HEIGHT_PERCENT = 0.99
TOUCH_THRESHOLD_Y_PERCENT = 0.55 # Поріг "дотику" (вище 55% висоти кадру)

last_zone = None

while cap.isOpened():
    ret, frame = cap.read()
     # запам'ятовуємо останню озвучену зону

    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    ROI_W = int(W * ROI_WIDTH_PERCENT)
    ROI_H = int(H * ROI_HEIGHT_PERCENT)
    ROI_X_START = int((W - ROI_W) / 2)
    ROI_Y_START = int((H - ROI_H) / 2)

    TOUCH_THRESHOLD_Y_ABS = int(H * TOUCH_THRESHOLD_Y_PERCENT)
    virtual_map = create_virtual_map(ROI_W, ROI_H)

    # Вставляємо віртуальний макет у кадр (область ROI)
    frame[ROI_Y_START : ROI_Y_START + ROI_H, 
          ROI_X_START : ROI_X_START + ROI_W] = virtual_map
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            tip = hand_landmarks.landmark[INDEX_FINGER_TIP_ID]
            
            # Піксельні координати кінчика пальця (всього кадру)
            abs_x = int(tip.x * W)
            abs_y = int(tip.y * H)

            # --- 6. Перевірка Умов та Масштабування ---
            # a) Умова "Дотику" (по Y-координаті)
            is_touching_y = abs_y < TOUCH_THRESHOLD_Y_ABS

            # b) Умова "Потрапляння в ROI"
            is_in_roi = (abs_x >= ROI_X_START and abs_x <= ROI_X_START + ROI_W and
                         abs_y >= ROI_Y_START and abs_y <= ROI_Y_START + ROI_H)
            
            # Малюємо палець
            finger_color = (0, 255, 0)

                # Обчислюємо відносні координати всередині ROI (пікселі)
            relative_x = abs_x - ROI_X_START
            relative_y = abs_y - ROI_Y_START
  
                # Нормалізуємо відносні координати до 0.0-1.0 (для зіставлення з зонами)
            scaled_norm_x = relative_x / ROI_W
            scaled_norm_y = relative_y / ROI_H
            finger_color = (0, 255, 255) # Жовтий, якщо умови виконані         
                # --- 7. Зіставлення з Зонами (Point-in-Rectangle Test) ---
        
        for zone in INTERACTIVE_ZONES:
                    min_x, min_y, max_x, max_y = zone["norm_coords"]
                    
                    # Умова належності точки до прямокутника
                    if (scaled_norm_x >= min_x and scaled_norm_x <= max_x and
                        scaled_norm_y >= min_y and scaled_norm_y <= max_y):
                        
                        detected_zone = zone["name"]
                        finger_color = zone["color"] # Задаємо колір зони
                        
                        cv2.putText(frame, f"Zone: {detected_zone}", (100, 30), 
                                    cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 0), 2)
                        
                        if detected_zone != last_zone:
                              
                              speak(detected_zone)
                              last_zone = detected_zone
                        else:
                            last_zone = None  
                        
        

        cv2.circle(frame, (abs_x, abs_y), 15, (255,255,255), -1)
        cv2.circle(frame, (abs_x, abs_y), 10, finger_color, -1)         

        if is_in_roi:
            cv2.putText(frame,f"x={scaled_norm_x:.2f}, y={scaled_norm_y:.2f}",(390, 30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 0, 0),2)     

    cv2.imshow('Interactive Map Detection', frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
hands.close()
cap.release()
cv2.destroyAllWindows()