import cv2


img = cv2.imread("room.jpg")

if img is None:
    print("Помилка: файл не знайдено або не вдалося відкрити")
    exit()  

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0) 

cv2.imshow("Original Image", img)
cv2.imshow("Gray and Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("room_processed.jpg", blur)
print("Оброблене зображення збережено у 'room_processed.jpg'")
cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Не вдається отримати відеопотік")
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()