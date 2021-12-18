import cv2  # open cv library , import

cam = cv2.VideoCapture(0) # passing a constant -> 0 which signifies that we are starting our webcam

cv2.namedWindow("testing")

img_counter = 0

while True:
    ret, frame = cam.read() # two variables and using read function to read camera
    if not ret:
        print("failed to snatch frame")
        break
    cv2.imshow("testing", frame) # this screen appears to user

    k = cv2.waitKey(1) # space key
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing.")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release() #releasing the camera

cv2.destroyAllWindows() # destroying i.e clearing all the windows