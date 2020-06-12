import cv2 as cv

img = cv.imread('Assets/lena.jpg', 1)

cv.imshow('Image', img)

key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
elif key == ord('s'):
    cv.imwrite('Assets/new_image_copy.png', img)
    cv.destroyAllWindows()
