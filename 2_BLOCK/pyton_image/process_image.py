import cv2


img = cv2.imread("aaaaa.jpg")

if img is None:
    print("Помилка: файл не знайдено або не вдалося відкрити")
    exit()  

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0) 

cv2.imshow("Original Image", img)
cv2.imshow("Gray and Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("sss.jpg", blur)
print("Оброблене зображення збережено у 'sss.jpg'")
