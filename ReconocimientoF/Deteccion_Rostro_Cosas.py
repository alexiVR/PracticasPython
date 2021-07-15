import cv2 as cv2
import numpy as np

camara = cv2.VideoCapture(0)
ruidos = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

while True:
 _,captura = camara.read()
 grises = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
 identifica = ruidos.detectMultiScale(grises, 1.3,5)
 for (x,y,e1,e2) in identifica:
  cv2.rectangle(captura, (x,y), (x+e1,y+e2), (0,0,255),2)
  cv2.putText(captura, 'Rostro encontrado', (x,y-5), 1,1.3,(0,255,0),2, cv2.LINE_AA)
 cv2.imshow("Resultados", captura)

 if cv2.waitKey(1)==ord("s"):
  break
camara.release()
cv2.destroyAllWindows()
