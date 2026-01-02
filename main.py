import numpy as np
import random
from ShareKey import*
def generate_mask(key, num_holes=64, grid_size=100):

    seed = int(''.join(map(str, key)), 2)  
    random.seed(seed)
    
    holes = set()
    while len(holes) < num_holes:
        x = random.uniform(0, grid_size)
        y = random.uniform(0, grid_size)
        holes.add((round(x, 2), round(y, 2))) 
    
    return list(holes)


mask_kate = generate_mask(alice_key, num_holes=70)
mask_shon = generate_mask(bob_key, num_holes=70)
mask_david = generate_mask(np.random.randint(0, 2, 256), num_holes=70)

print("Kate masks : ", mask_kate[:5])
print("Shon masks : ", mask_shon[:5])

def send_message(message_bits, mask_sender, tolerance=0.1):
    if len(message_bits) > len(mask_sender):
        raise ValueError("Message is big!")
    
    photons = []
    for i, bit in enumerate(message_bits):

        photons.append(mask_sender[i]) 
    
    return photons, message_bits


def receive_message(photons, mask_receiver, original_bits, tolerance=0.1):
    received_bits = [0] * len(original_bits)  
    
    for p_idx, photon in enumerate(photons):
        for i, hole in enumerate(mask_receiver):
            if abs(photon[0] - hole[0]) < tolerance and abs(photon[1] - hole[1]) < tolerance:

                received_bits[p_idx] = original_bits[p_idx]
                break
    
    return received_bits



message = [1, 0, 1, 1, 0]
photons, original_bits = send_message(message, mask_kate)

received_shon = receive_message(photons, mask_shon, original_bits, tolerance=0.1)
print("Sended message :", message)
print("Shon receive :", received_shon)

if received_shon == message:
    print("Shon receive = message ✔")
else:
    print("Shon recieve is imperfect ✘")


received_david = receive_message(photons, mask_david, original_bits, tolerance=0.1)
print("David receive:", received_david)
if received_david != message:
    print("David was found!!!")