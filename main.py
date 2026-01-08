import numpy as np
import random
from ShareKey import*
print("""
__________                                     ________  ________
\______   \_____ _______  ____   ____   ____   \_____  \/  _____/
 |     ___/\__  \\_  __ \/ ___\ /  _ \ /    \   /  ____/   __  \ 
 |    |     / __ \|  | \/ /_/  >  <_> )   |  \ /       \  |__\  \\
 |____|    (____  /__|  \___  / \____/|___|  / \_______ \_____  /
                \/     /_____/             \/          \/     \/ 
      Version 1.1.0 (January 8, 2026)
      Iran(Tehran(+3:30 UTC)), Baluchistan, Chabahar freezone
      Developed by Arman Baadpa
""")
def generate_mask(key, num_holes=1024, grid_size=1000):

    seed = int(''.join(map(str, key)), 2)  
    random.seed(seed)
    
    holes = set()
    while len(holes) < num_holes:
        x = random.uniform(0, grid_size)
        y = random.uniform(0, grid_size)
        holes.add((round(x, 2), round(y, 2))) 
    
    return list(holes)


mask_kate = generate_mask(alice_key, num_holes=1024)
mask_shon = generate_mask(bob_key, num_holes=1024)
mask_david = generate_mask(np.random.randint(0, 2, 256), num_holes=1024)

print("Kate masks : ", mask_kate[:10],", ...")
print("Shon masks : ", mask_shon[:10],", ...")

def send_message(message_bits, mask_sender, tolerance=5.0):
    if len(message_bits) > len(mask_sender):
        raise ValueError("Message is big!")
    
    photons = []
    for i, bit in enumerate(message_bits):

        photons.append(mask_sender[i]) 
    
    return photons, message_bits


def receive_message(photons, mask_receiver, original_bits, tolerance=5.0):
    received_bits = [0] * len(original_bits)  
    
    for p_idx, photon in enumerate(photons):
        for i, hole in enumerate(mask_receiver):
            if abs(photon[0] - hole[0]) < tolerance and abs(photon[1] - hole[1]) < tolerance:

                received_bits[p_idx] = original_bits[p_idx]
                break
    
    return received_bits



message = [0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1]
photons, original_bits = send_message(message, mask_kate)

received_shon = receive_message(photons, mask_shon, original_bits, tolerance=5.0)
print("Sended message :", message)
print("Shon receive :", received_shon)

if received_shon == message:
    print("Shon receive = message ✔")
else:
    print("Shon recieve is imperfect ✘")


received_david = receive_message(photons, mask_david, original_bits, tolerance=5.0)
print("David receive:", received_david)
if received_david != message:
    print("David was found!!!")
