from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class CipherRequest(BaseModel):
    text: str
    key: str

def vigenere(message, key, direction=1):
    key_index = 0
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

@app.post("/encrypt")
def encrypt(data: CipherRequest):
    return {"encrypted_text": vigenere(data.text, data.key)}

@app.post("/decrypt")
def decrypt(data: CipherRequest):
    return {"decrypted_text": vigenere(data.text, data.key, -1)}

