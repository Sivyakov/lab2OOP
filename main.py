import cv2
import numpy as np

image = cv2.imread('Beluga_premier.gov.ru-2.jpeg')
mean = 0
stddev = 0.2
noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)
filtered_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()