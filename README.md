# 🔐 RSA Encryption & Decryption Platform

## 📖 Introduction
This project is a mini RSA encryption and decryption platform developed during the **GoMyCode Cyber Security Bootcamp**.  
The objective was to implement the RSA algorithm **from scratch**, without external cryptographic libraries, to gain a deep understanding of the mathematical foundations behind public‑key cryptography.

The application includes a **Tkinter GUI** that allows users to generate RSA keys, encrypt plaintext, and decrypt ciphertext with real‑time validation and feedback.

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **Tkinter** – Graphical User Interface (GUI)  
- **Pure Python mathematics** – No external crypto libraries  
- **Custom utility module** – Number theory operations (GCD, primality test, modular inverse)  

---

## ✨ Features
- Manual input of **p**, **q**, and **e**  
- Automatic computation of:
  - Modulus **n**
  - Euler’s totient **φ(n)**
  - Public and private keys  
- Encrypt plaintext messages using the public key  
- Decrypt ciphertext using the private key  
- Real‑time warnings for:
  - Non‑prime inputs  
  - Duplicate primes  
  - Invalid public exponent  
  - Small modulus values (<255) causing unreadable output  
- Demonstrates the impact of **small vs large primes** on RSA behavior  

---

## ⚙️ Development Process
1. **Mathematical Design**  
   Defined RSA parameters (p, q, n, φ(n), e, d) and implemented modular arithmetic manually.  

2. **Core RSA Logic**  
   Built functions for key generation, encryption, and decryption. Ensured coprimality and modular inverse correctness.  

3. **Utility Functions**  
   Implemented primality testing, GCD, and modular inverse without recursion or external libraries.  

4. **GUI Integration**  
   Designed an intuitive Tkinter interface, connected inputs to RSA logic, and added validation/error handling.  

5. **Testing & Improvements**  
   Tested with different prime sizes, handled edge cases, and added warnings for invalid inputs.  

---

## 📚 What I Learned
- Deep understanding of **RSA cryptography and number theory**  
- How public‑key encryption works internally  
- Importance of parameter validation in cryptographic systems  
- Building interactive GUIs in Python with error handling  
- Debugging mathematical and logical edge cases  

### 🔮 Possible Improvements
- Automatic large prime generation  
- Support for larger messages and block encryption  
- Performance optimization for large key sizes  
- Enhanced GUI styling and UX  
- Export/import of keys  

---

## ▶️ How to Run
1. Install **Python** on your machine  
2. Clone or download the repository  
3. Open the project folder  
4. Run `main.py`  
5. Use the GUI to generate keys, encrypt messages, and decrypt them  

---

## 🎥 Project Demonstration
Add your demo video link here:  
**▶️ [<!-- Failed to upload "0117(1).mp4" -->]

---

## 👤 Author
**Malek Khadhraoui**  
Cyber Security Bootcamp – GoMyCode  

---

