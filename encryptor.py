import json
import base64

# 👇 Paste your key here
xxx = "¨8/VI{ÇbÍßtÊZðJ3ÒecOÆJâ¶Qÿ7ïs"

def encode_data(a):
    b = 0
    c = json.dumps(a, separators=(',', ':')).encode('utf-8')
    d = list(range(256))
    e = 0
    f = ""

    for h in range(256):
        e = (e + d[h] + ord(xxx[h % len(xxx)])) % 256
        b = d[h]
        d[h] = d[e]
        d[e] = b

    i = 0
    e = 0

    for j in range(len(c)):
        i = (i + 1) % 256
        e = (e + d[i]) % 256
        b = d[i]
        d[i] = d[e]
        d[e] = b
        f += chr(c[j] ^ d[(d[i] + d[e]) % 256])

    return base64.b64encode(f.encode('latin-1')).decode('latin-1')

# 🔽 Reads the fingerprint JSON from file
try:
    with open("fingerprint.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        encrypted_xal = encode_data(data)
        print("Generated XAL:")
        print(encrypted_xal)
except FileNotFoundError:
    print("Error: 'fingerprint.json' not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'fingerprint.json'.")
