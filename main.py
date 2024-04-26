import cv2
import mediapipe as mp
import pyautogui 

hand_dect = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    screen_height, screen_width = pyautogui.size()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_dect.process(rgb_frame)
    hands = output.multi_hand_landmarks
    index_y = 0
    if(hands):
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmark = hand.landmark
            for id, landmark in enumerate(landmark):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                # print(x,y)
                if id==8:
                    cv2.circle(img=frame, center=(x,y), radius=20, color=0)
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img=frame, center=(x,y), radius=20, color=0)
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    # print('outside',abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 1400:
                        print("click")
                        # pyautogui.click()
                    else:
                        print("no click")
                    # pyautogui.click()

    # else:
    #     print("no hands")
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)