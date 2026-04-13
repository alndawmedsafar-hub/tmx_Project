import os
import time
import sys

def tmx_intro():
    # ڕەنگەکان
    RASH = "\033[40m"    # باکگراوندی ڕەش
    ZARD = "\033[1;33m"  # نووسینی زەرد
    SIPE = "\033[1;37m"  # نووسینی سپی
    KOTAYI = "\033[0m"   # گەڕانەوە بۆ دۆخی ئاسایی

    os.system('clear')
    
    # دروستکردنی باکگراوندە ڕەشەکە
    print(RASH + "\n" * 5)
    
    # نیشاندانی ناوی TMX KURDISH بە جوانی
    logo = f"""
    {ZARD}        ====================================
    {ZARD}        ||                                ||
    {SIPE}        ||         TMX KURDISH          ||
    {SIPE}        ||       COMMANDER EDITION      ||
    {ZARD}        ||                                ||
    {ZARD}        ====================================
    """
    print(logo)
    
    # ئەنیمەیشنێکی کورت بۆ بارکردن
    print(f"\n{SIPE}          Loading assets from GitHub...")
    for i in range(5):
        sys.stdout.write(" █")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print(f"\n\n{ZARD}          READY TO PLAY!{KOTAYI}")
    time.sleep(2)

# بانگکردنی فەرمانەکە پێش دەستپێکی یاری
tmx_intro()
