# Nirana – Post-Quantum Cryptography with Physical Aperture Detection 🚀 Version 1.1.0 (January 8, 2026)

A hybrid quantum-inspired encryption system that detects eavesdroppers through physical mask (aperture) mismatch.

## Overview 🕶 (•_•)

Nirana combines the BB84 quantum key distribution protocol with a deterministic random aperture mask (random hole pattern) generated from the shared key as seed.

Binary messages are transmitted via simulated photons sent from the sender's mask positions.  
If the receiver's mask differs (eavesdropper), most photons hit the mask body instead of passing through holes, corrupting the message and automatically detecting intrusion.

Developed in January 2026 by a 15-year-old self-taught developer in Iran (Tehran & Chabahar Freezone).



## Key Features 🔑

- Full BB84 implementation with QBER-based eavesdropper detection
- Deterministic generation of identical random aperture masks on both sides (no physical transmission needed)
- Photon transmission for both 0 and 1 bits (full message length preserved)
- Large grid (1000×1000) + 1024 holes for high density
- Increased tolerance (5.0) for improved noise resistance compared to previous version
- Automatic intrusion detection: mismatched mask → blocked photons → corrupted message

## What's New in Version 1.1.0 (January 8, 2026) 🎇

- Significantly improved noise resistance: Larger grid size (1000), more holes (1024), and higher tolerance (5.0) make the system much more robust against small deviations and floating-point precision issues compared to the previous version.
- Better real-world simulation readiness while maintaining perfect message recovery for the legitimate receiver.

## Demo Output Example 🚦

```
private key created!
Alice key :  [1 1 0 0 0 0 0 0 0 1]
Bob key :  [1 1 0 0 0 0 0 0 0 1]
Eave was found! Error rate: 0.11

      NIRANA ENCRYPTION - 1.1.1
      Version 1.1.0 (January 8, 2026)
      Iran(Tehran(+3:30 UTC)), Baluchistan, Chabahar freezone
      Developed by Arman Baadpa

Kate masks :  [(319.35, 929.69), (646.2, 961.92), (281.05, 805.89), (84.31, 117.99), (238.88, 703.09), (128.1, 527.46), (376.45, 390.53), (819.04, 368.95), (111.41, 646.45), (324.91, 219.38)] , ...
Shon masks :  [(319.35, 929.69), (646.2, 961.92), (281.05, 805.89), (84.31, 117.99), (238.88, 703.09), (128.1, 527.46), (376.45, 390.53), (819.04, 368.95), (111.41, 646.45), (324.91, 219.38)] , ...
Sended message : [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 
1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
Shon receive : [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
Shon receive = message ✔
David receive: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
David was found!!!
```

## Technologies 💻

- Python 3.8+
- NumPy – for array handling
- random module – with fixed seed for reproducible masks

## How to Run 📐

```bash
git clone https://github.com/Alendra405/Nirana.git
cd Nirana

pip install numpy

python main.py
```

## Why It Matters ¯\\_(ツ)_/¯

As quantum computers threaten classical cryptography, Nirana explores a creative hybrid: information-theoretically secure BB84 + active physical-layer detection through aperture mismatch.

The enhanced noise resistance in this version brings the simulation one step closer to real-world feasibility.

Star ⭐ this repo if you find it interesting!  
Feedback & contributions are welcome.

```bash
MIT License

Copyright (c) 2026 Arman Baadpa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
