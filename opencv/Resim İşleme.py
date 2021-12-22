import cv2
resim= cv2.imread("bilsem.jpg",0)
cv2.imshow("bilsem<33",resim)
cv2.imwrite("bilsem2.jpg",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
