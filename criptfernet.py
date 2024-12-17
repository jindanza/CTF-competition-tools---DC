try:
    from cryptography.fernet import Fernet
    import base64
except ImportError:
    print("Error: Library cryptography tidak terpasang.")
    print("Silakan jalankan: pip install cryptography")
    exit()

def decrypt_fernet(ciphertext, symmetric_key):
    try:
        key = base64.urlsafe_b64decode(symmetric_key)
        f = Fernet(base64.urlsafe_b64encode(key))
        decrypted_message = f.decrypt(ciphertext.encode('utf-8')).decode('utf-8')
        
        return decrypted_message
    
    except Exception as e:
        return f"Error dalam dekripsi: {e}"

ciphertext = "gAAAAABnXQhJXHMmG_4MBU8M8alqSqMSt8SwgDgz0P1VqFGO6FknbfDBj4WjpPvFXecySjEkO87dN_HdATp1vGETCL0kK-VxpbcEx9hSYXIpVju95P97kkfWdlly_ZVNC614e7hzbIR5"
symmetric_key = "VHTvOGAHs6QBn3px_GiGFUNCudFES_6RYhLaTXVDY6k="

result = decrypt_fernet(ciphertext, symmetric_key)

print("Pesan Terdekripsi:", result)