import cv2
import numpy as np
import mediapipe.python.solutions.hands as mp_hands

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

pieces = []
grid_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
selected_idx = None
game_started = False

# Hover logic
hover_timer = 0
current_hover_idx = None

while True:
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]
    
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if not game_started:
        cv2.putText(frame, "Show OPEN PALM to Start", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0].landmark
            if (lm[12].y < lm[0].y - 0.2): 
                box_size = 450
                start_x, start_y = (w//2 - box_size//2), (h//2 - box_size//2)
                step = box_size // 3
                for i in range(3):
                    for j in range(3):
                        pieces.append(frame[start_y+i*step:start_y+(i+1)*step, start_x+j*step:start_x+(j+1)*step])
                np.random.shuffle(grid_indices)
                game_started = True
    else:
        box_size = 450
        start_x, start_y = (w//2 - box_size//2), (h//2 - box_size//2)
        step = box_size // 3
        
        if results.multi_hand_landmarks:
            cx, cy = int(results.multi_hand_landmarks[0].landmark[8].x * w), int(results.multi_hand_landmarks[0].landmark[8].y * h)
            cv2.circle(frame, (cx, cy), 15, (255, 0, 0), -1)
            
            hovering = False
            for i in range(3):
                for j in range(3):
                    gx, gy = start_x + j*step, start_y + i*step
                    if gx < cx < gx+step and gy < cy < gy+step:
                        hovering_idx = i*3 + j
                        if hovering_idx == current_hover_idx:
                            hover_timer += 1
                        else:
                            current_hover_idx = hovering_idx
                            hover_timer = 0
                        hovering = True
                        break
            
            # TRIGGER SWAP: Now requires 60 frames (~2 seconds)
            if hovering and hover_timer > 60:
                if selected_idx is None:
                    selected_idx = current_hover_idx
                else:
                    grid_indices[selected_idx], grid_indices[current_hover_idx] = grid_indices[current_hover_idx], grid_indices[selected_idx]
                    selected_idx = None
                hover_timer = 0 
        else:
            current_hover_idx = None
            hover_timer = 0

        # Render
        for i in range(3):
            for j in range(3):
                idx = grid_indices[i*3 + j]
                color = (0, 255, 255) if selected_idx == (i*3 + j) else (255, 255, 255)
                # Draw a "loading" progress bar on the hovered piece
                frame[start_y+i*step:start_y+(i+1)*step, start_x+j*step:start_x+(j+1)*step] = pieces[idx]
                cv2.rectangle(frame, (start_x+j*step, start_y+i*step), (start_x+j*step+step, start_y+i*step+step), color, 3)
                
                # Visual Loading indicator
                if current_hover_idx == (i*3 + j) and hover_timer > 0:
                    progress = int((hover_timer / 60) * step)
                    cv2.rectangle(frame, (start_x+j*step, start_y+i*step), (start_x+j*step+progress, start_y+i*step+10), (0, 255, 0), -1)

    cv2.imshow('Live Puzzle', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()