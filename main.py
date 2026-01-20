import tkinter as tk
from tkinter import messagebox
import traceback
import rsa_core
import utils

current_public_key = None
current_private_key = None

def compute_n_phi():
    try:
        p = int(entry_p.get().strip())
        q = int(entry_q.get().strip())

        if not utils.is_prime(p) or not utils.is_prime(q):
            messagebox.showerror("Validation Error", "p and q must be prime numbers.")
            return
        if p == q:
            messagebox.showerror("Validation Error", "p and q must be distinct primes.")
            return

        n = p * q
        phi = (p - 1) * (q - 1)
        if n <= 255:
            messagebox.showwarning(
        "Small n",
        "Your n is too small (<=255). Use larger primes so decrypted characters display correctly."
    )

        n_phi_text.set(f"n = {n}   φ(n) = {phi}")
        status_text.set("n and φ(n) computed. Now choose a valid e.")
    except Exception as e:
        messagebox.showerror("Computation Error", f"{e}\n\n{traceback.format_exc()}")

def generate_keys():
    global current_public_key, current_private_key
    try:
        # Read manual inputs
        p_str = entry_p.get().strip()
        q_str = entry_q.get().strip()
        e_str = entry_e.get().strip()

        if not p_str or not q_str or not e_str:
            messagebox.showerror("Input Error", "Please enter p, q, and e.")
            return

        p = int(p_str)
        q = int(q_str)
        e = int(e_str)

        # Validate primes and e
        if not utils.is_prime(p) or not utils.is_prime(q):
            messagebox.showerror("Validation Error", "p and q must be prime numbers.")
            return
        if p == q:
            messagebox.showerror("Validation Error", "p and q must be distinct primes.")
            return
        


        public_key, private_key, n, phi = rsa_core.generate_keys_manual(p, q, e)

        current_public_key = public_key
        current_private_key = private_key

        pub_key_text.set(f"Public Key (e, n): {public_key}")
        priv_key_text.set(f"Private Key (d, n): {private_key}")
        n_phi_text.set(f"n = {n}   φ(n) = {phi}")   # ✅ show n and φ(n)
        messagebox.showinfo("Keys", "Keys computed successfully.")
    except ValueError as ve:
        messagebox.showerror("Key Generation Error", str(ve))
    except Exception as e:
        messagebox.showerror("Key Generation Error", f"{e}\n\n{traceback.format_exc()}")

def encrypt_message():
    try:
        if current_public_key is None:
            messagebox.showerror("Error", "Generate keys first.")
            return
        message = entry_message.get()
        if not message:
            messagebox.showerror("Error", "Please enter a message to encrypt.")
            return
        ciphertext_list = rsa_core.encrypt(message, current_public_key)
        entry_cipher.delete(0, tk.END)
        entry_cipher.insert(0, ' '.join(map(str, ciphertext_list)))
        status_text.set("Encryption successful.")
    except Exception as e:
        messagebox.showerror("Encryption Error", f"{e}\n\n{traceback.format_exc()}")

def decrypt_message():
    try:
        if current_private_key is None:
            messagebox.showerror("Error", "Generate keys first.")
            return
        cipher_text = entry_cipher.get().strip()
        if not cipher_text:
            messagebox.showerror("Error", "Please enter ciphertext to decrypt.")
            return
        cipher_list = [int(x) for x in cipher_text.split()]
        plaintext = rsa_core.decrypt(cipher_list, current_private_key)
        entry_plain.delete(0, tk.END)
        entry_plain.insert(0, plaintext)
        status_text.set("Decryption successful.")
    except ValueError:
        messagebox.showerror("Decryption Error", "Ciphertext must be space-separated integers.")
    except Exception as e:
        messagebox.showerror("Decryption Error", f"{e}\n\n{traceback.format_exc()}")

# GUI setup
root = tk.Tk()
root.title("RSA Encryption/Decryption Platform by Angel")
root.geometry("820x560")
root.configure(bg="#FFF5F7")  # Light pink background

# Title
tk.Label(root, text="RSA Encryption/Decryption by Angel",
         font=("Helvetica Neue", 20, "bold"), bg="#FFF5F7", fg="#4B3F72").pack(pady=12)

# Parameters frame
frame_params = tk.Frame(root, bg="#FFF5F7")
frame_params.pack(pady=8)

tk.Label(frame_params, text="p (prime):", bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).grid(row=0, column=0, padx=6, pady=4, sticky="e")
entry_p = tk.Entry(frame_params, width=18)
entry_p.grid(row=0, column=1, padx=6, pady=4)

tk.Label(frame_params, text="q (prime):", bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).grid(row=0, column=2, padx=6, pady=4, sticky="e")
entry_q = tk.Entry(frame_params, width=18)
entry_q.grid(row=0, column=3, padx=6, pady=4)

tk.Label(frame_params, text="e (public exponent):", bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).grid(row=0, column=4, padx=6, pady=4, sticky="e")
entry_e = tk.Entry(frame_params, width=18)
entry_e.grid(row=0, column=5, padx=6, pady=4)

# Keys and status
pub_key_text = tk.StringVar(value="Public Key (e, n): —")
priv_key_text = tk.StringVar(value="Private Key (d, n): —")
n_phi_text = tk.StringVar(value="n: —   φ(n): —")
status_text = tk.StringVar(value="Status: —")

tk.Button(root, text="Compute n and φ(n)", command=compute_n_phi,
          bg="#AED9E0", fg="#1B1B1B", font=("Helvetica Neue", 10, "bold")).pack(pady=4)

tk.Label(root, textvariable=n_phi_text, bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10, "italic")).pack(pady=4)
tk.Button(root, text="Compute Keys", command=generate_keys,
          bg="#B8E2C8", fg="#1B1B1B", font=("Helvetica Neue", 10, "bold")).pack(pady=8)
tk.Label(root, textvariable=pub_key_text, bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10)).pack()
tk.Label(root, textvariable=priv_key_text, bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10)).pack()
tk.Label(root, textvariable=status_text, bg="#FFF5F7", fg="#7A7A7A", font=("Helvetica Neue", 9, "italic")).pack(pady=4)

# Message input
tk.Label(root, text="Plaintext message:", bg="#FFF5F7", fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).pack(pady=6)
entry_message = tk.Entry(root, width=90)
entry_message.pack()

btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message,
                        bg="#CBAACB", fg="#1B1B1B", font=("Helvetica Neue", 10, "bold"))
btn_encrypt.pack(pady=6)

# Ciphertext
tk.Label(root, text="Ciphertext (space-separated integers):", bg="#FFF5F7",
         fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).pack(pady=6)
entry_cipher = tk.Entry(root, width=90)
entry_cipher.pack()

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message,
                        bg="#FFDAC1", fg="#1B1B1B", font=("Helvetica Neue", 10, "bold"))
btn_decrypt.pack(pady=6)

# Plaintext output
tk.Label(root, text="Decrypted Plaintext:", bg="#FFF5F7",
         fg="#5A5A5A", font=("Helvetica Neue", 10, "bold")).pack(pady=6)
entry_plain = tk.Entry(root, width=90)
entry_plain.pack()

# Footer
tk.Label(root, text="Tip: Use small primes for demo (e.g., p=61, q=53, e=17).",
         bg="#FFF5F7", fg="#999", font=("Helvetica Neue", 9)).pack(pady=10)

root.mainloop()
