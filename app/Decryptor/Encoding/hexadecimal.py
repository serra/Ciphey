class Hexadecimal:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        try:
            result = bytearray.fromhex(text).decode()
        except ValueError as e:
            return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": None, "Extra Information": None}
            
        if self.lc.checkLanguage(result):
            return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": result, "Cipher": "Ascii to Hexadecimal encoded", "Extra Information": None}