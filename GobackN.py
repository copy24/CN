import time
import random

total_frames = 10
window_size = 3
base = 0
next_frame = 0

def receive_ack(frame):

    if random.randint(1, 10) == 3:
        print(f"Frame {frame} lost! No ACK received.")
        return False
    else:
        print(f"ACK received for Frame {frame}")
        return True

print("\n--- Sliding Window Protocol Simulation ---\n")

while base < total_frames:


    while next_frame < base + window_size and next_frame < total_frames:
        print(f"Sending Frame {next_frame}")
        next_frame += 1
        time.sleep(1)

    ack = receive_ack(base)

    if ack:
        base += 1
    else:
        print("Timeout! Retransmitting from Frame", base)
        next_frame = base 


print("\nAll Frames Sent Successfully!")










"""Select REpeat protocol is a more efficient version of the Go-Back-N protocol. In Select Repeat, the sender can retransmit only the specific frames 
that were lost or corrupted, rather than retransmitting all frames from the point of error as in Go-Back-N. This allows for better utilization of the network and reduces
 unnecessary retransmissions, making it more efficient in scenarios with higher error rates."""




import time
import random

total_frames = 10
window_size = 4
base = 0
ack_status = [False] * total_frames

def receive_ack(frame):
    if random.randint(1, 10) <3:
        print(f"Frame {frame} lost! No ACK received.")
        return False
    else:
        print(f"ACK received for Frame {frame}")
        return True

print("\n--- Selective Repeat Protocol Simulation ---\n")

while base < total_frames:

    # send frames within window
    for frame in range(base, min(base + window_size, total_frames)):

        if not ack_status[frame]: 
            print(f"Sending Frame {frame}")
            time.sleep(1)

            ack = receive_ack(frame)

            if ack:
                ack_status[frame] = True
            else:
                print(f"Frame {frame} will be retransmitted later.")

    while base < total_frames and ack_status[base]:
        base += 1

    time.sleep(1)

print("\nAll Frames Sent Successfully!")