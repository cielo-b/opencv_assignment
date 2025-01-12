import cv2

image = cv2.imread("assignment-001-given.jpg")

cv2.putText(
    image,
    "RAH972U",
    (830, 180),
    cv2.FONT_HERSHEY_SIMPLEX,
    3,
    (0, 255, 0),
    5,
    cv2.LINE_4,
)

cv2.rectangle(image, (250, 200), (980, 920), (0, 255, 0), 8)

cv2.namedWindow("My Result", cv2.WINDOW_NORMAL)
cv2.imshow("My Result", image)

cv2.waitKey(0)

cv2.imwrite("final_image.jpg", image)

cv2.destroyAllWindows()
