import rsa_core

def test_manual_example():
    pub, priv, n, phi = rsa_core.generate_keys_manual(61, 53, 17)
    assert n == 3233 and phi == 3120
    assert pub == (17, 3233)
    assert priv[0] == 2753  # d for this example
    msg = "HELLO"
    c = rsa_core.encrypt(msg, pub)
    p = rsa_core.decrypt(c, priv)
    assert p == msg

if __name__ == "__main__":
    test_manual_example()
    print("All tests passed.")
