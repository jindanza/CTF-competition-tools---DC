import base64

def decode_base32(encoded_text):
    try:
        decoded_bytes = base64.b32decode(encoded_text)
        
        decoded_text = decoded_bytes.decode('utf-8')
        
        return decoded_text
    
    except Exception as e:
        return f"Error dalam dekripsi: {e}"

encoded_code = "MZWGCZZSPNGUEQ27LBPUISKHJFJVIQKSL5UGIYTBNQZDONBWPU======"

result = decode_base32(encoded_code)

print("Hasil Dekripsi:", result)