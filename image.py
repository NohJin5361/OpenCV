import cv2
import numpy as np

# 이미지를 그레이스케일로 읽어들입니다.
image = cv2.imread('Spongebob.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("이미지를 찾을 수 없습니다.")
else:
    # 이진화로 캐릭터를 분리합니다.
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # Morphology 연산을 통해 작은 부분을 제거하고 윤곽선을 강화합니다.
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=2)

    # 윤곽선을 찾습니다.
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 가장 큰 윤곽선만 찾습니다.
    largest_contour = max(contours, key=cv2.contourArea)

    # 이미지를 컬러로 변환한 후 가장 큰 윤곽선만 그립니다.g
    color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(color_image, [largest_contour], -1, (0, 255, 0), 2)

    # 결과 이미지를 출력합니다.
    cv2.imshow('Largest Contour', color_image)
    cv2.waitKey(0)
  
