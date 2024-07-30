def a(img):
    import cv2 as cv
    img=cv.imread(img,0)
    cv.imshow("img",img)
    cv.waitKey(0)
def b(img):
    import cv2 as cv
    img1=cv.imread(img,0)
    cv.imshow("img",img1)
    img2=cv.imread(img,1)
    cv.imshow("IMG",img2)
    cv.waitKey(0)