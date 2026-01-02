import numpy as np

def bb84_key_distribution(n_bits=100, eavesdrop=False):
    alice_bits = np.random.randint(0, 2, n_bits)
    alice_bases = np.random.randint(0, 2, n_bits)
    
    qubits = alice_bits  
    if eavesdrop:
        eve_bases = np.random.randint(0, 2, n_bits)
        eve_measure = np.where(eve_bases == alice_bases, qubits, np.random.randint(0, 2, n_bits))
        qubits = eve_measure
        
    bob_bases = np.random.randint(0, 2, n_bits)
    bob_bits = np.where(bob_bases == alice_bases, qubits, np.random.randint(0, 2, n_bits))

    matching_bases = alice_bases == bob_bases
    alice_key = alice_bits[matching_bases]
    bob_key = bob_bits[matching_bases]
    
    sample_size = len(alice_key) // 2
    sample_indices = np.random.choice(len(alice_key), sample_size, replace=False)
    error_rate = np.mean(alice_key[sample_indices] != bob_key[sample_indices])
    
    if error_rate > 0.1:  
        return None, None, "Eave was found! Error rate: {:.2f}".format(error_rate)
    else:
        #fianl key
        remaining_indices = np.setdiff1d(np.arange(len(alice_key)), sample_indices)
        return alice_key[remaining_indices], bob_key[remaining_indices], "private key created!"

# Without eave
alice_key, bob_key, message = bb84_key_distribution(100, eavesdrop=False)
print(message)
print("Alice key : ", alice_key[:10]) #10 first bits
print("Bob key : ", bob_key[:10])

# With eave
alice_key_eve, bob_key_eve, message_eve = bb84_key_distribution(100, eavesdrop=True)
print(message_eve)