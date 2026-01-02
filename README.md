# PARGON 26 – Post-Quantum Cryptography with Physical Aperture Detection 🚀 :-D

A hybrid quantum-inspired encryption system that detects eavesdroppers through physical mask mismatch.

## Overview 🕶 (¬_¬ )

PARGON 26 combines BB84 for secure shared key generation with a deterministic random aperture mask (hole pattern) derived from the key as seed.

Messages are transmitted via simulated photons from sender's mask positions.  
If the receiver's mask differs (eavesdropper), most photons hit the wall instead of passing through holes → message corrupts → automatic detection.

## Key Features 🔑 (•_•)

- Full BB84 implementation with QBER-based eavesdropper detection
- Identical random mask generation on both sides using shared key as seed
- Photon transmission for both 0 and 1 bits (full message length preserved)
- Tolerance for simulating real-world noise/misalignment
- Automatic intrusion detection via photon blockage

## Demo Output Example 🚦 ¯\_(ツ)_/¯
```bash
private key created!
Alice key :  [0 1 1 0 0 0 0 1 1 1]
Bob key :  [0 1 1 0 0 0 0 1 1 1]
Eave was found! Error rate: 0.26
Kate masks :  [(61.95, 36.56), (68.98, 44.46), (17.73, 15.39), (22.8, 43.34), (85.02, 35.57)]
Shon masks :  [(61.95, 36.56), (68.98, 44.46), (17.73, 15.39), (22.8, 43.34), (85.02, 35.57)]
Sended message : [1, 0, 1, 1, 0]
Shon receive : [1, 0, 1, 1, 0]
Shon receive = message ✔
David receive: [0, 0, 0, 0, 0]
David was found!!!
```
## Technologies ☄

- Python 3.8+
- NumPy
- random module (fixed seed)

## How to Run 🚀

```bash
git clone https://github.com/Alendra405/pargon-26.git
```
```bash
pip install numpy
```
```bash
python/python3 main.py
```

Built by a 15-year-old self-taught developer in 2026. ;-)
