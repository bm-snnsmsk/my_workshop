import cv2

cam = cv2.VideoCapture(0)  ## veya video yolu eklenip videodaki yüzlerde tarama yapılabilir
face_cascade = cv2.CascadeClassifier("haars_cascades/haarcascade_frontalface_default.xml")

while True :
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    if ret == False :
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 3) ## img, ölçek, arama_matrixi_algoritma( = en az üç düktürtgende bir yüz keşfedilirse sonucu true olarak döndür)
    #print(faces) ## yüzün bulunduğu diktörtgenin sol-üst(x ve y) değerleri ve bulunan dikdörtgenin w ve h
    for (x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

    cv2.imshow("Detected Faces", frame)
    if cv2.waitKey(30) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()






 