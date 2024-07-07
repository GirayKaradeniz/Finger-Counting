import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 1040)
cap.set(4, 720)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)


    lmList = []
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] < lmList[tipIds[4]][1]:

                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    fingers.append(1)

                else:
                    fingers.append(0)


                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                totalF = fingers.count(1)

                cv2.putText(img, str(totalF), (30,125), cv2.FONT_HERSHEY_PLAIN,10, (255,0,0), 8)

        elif lmList[tipIds[0]][1] > lmList[tipIds[4]][1]:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)

            else:
                fingers.append(0)


            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            totalF = fingers.count(1)

            cv2.putText(img, str(totalF), (30, 125), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8)


    print(lmList)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
