# Law Maker Code - Version 1.0 (Commander Edition)
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
key      = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890 "

def process(text, mode):
    result = ""
    source = alphabet if mode == "enc" else key
    target = key if mode == "enc" else alphabet
    for char in text:
        if char in source:
            result += target[source.index(char)]
        else:
            result += char
    return result

print("--- سیستەمی پاراستنی فەرماندە ---")
choice = input("بۆ کۆدکردن (1) یان کردنەوەی کۆد (2) دابگرە: ")
msg = input("دەقەکە بنووسە: ")

if choice == "1":
    print("🔐 کۆدی نهێنی: " + process(msg, "enc"))
elif choice == "2":
    print("🔓 دەقی ڕاستەقینە: " + process(msg, "dec"))
