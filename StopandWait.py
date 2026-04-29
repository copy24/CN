import time, random

total_frames = 10
frame = 0

def receive_ack(frame):
    time.sleep(1)
    if random.randint(1, 10) <= 3:
        print(f"Ack for {frame} lost")
        return False
    
    print(f"Ack for {frame} received")
    return True

while frame < total_frames:
    print(f"Sending frame {frame}")
    time.sleep(1)
    
    ack = receive_ack(frame)
    
    if ack:
        frame += 1
    else:
        print(f"Timeout! Retransmitting frame {frame}")