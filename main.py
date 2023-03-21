import cv2
import mediapipe as mp
import pyautogui
camera = cv2.VideoCapture(0)
face_mesh =  mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screen_width, screen_height = pyautogui.size()
while True:
    _, frames = camera.read()
    frames = cv2.flip(frames,1)
    RGB_frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(RGB_frames)
    landmarks_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frames.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frames, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_width * landmark.x
                screen_y = screen_height * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        wink = [landmarks[145], landmarks[159]]
        for landmarks in wink:
           x = int(landmark.x * frame_width)
           y = int(landmark.y * frame_height)
           cv2.circle(frames, (x, y), 3, (0, 255, 255)) 
        if (wink[0].y - wink[1].y) < 0.004: 
            pyautogui.click()
            pyautogui.sleep(1)  
    cv2.imshow("virtual-controlled-mouse",frames)
    cv2.waitKey(1)