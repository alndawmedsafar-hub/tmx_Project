import os
import time
import sys

# 1. بەشی لۆگۆ و دەستپێک (Splash Screen)
def show_intro():
    os.system('clear')
    # ڕەنگی ڕەش و سپی درەوشاوە
    print("\033[40m" + "\n" * 5) 
    logo = """
    \033[1;37m        ╔════════════════════════════════════╗
            ║                                    ║
            ║         ★ TMX KURDISH ★          ║
            ║        SYSTEM STARTING...          ║
            ║                                    ║
            ╚════════════════════════════════════╝
    """
    print(logo)
    time.sleep(3) # ٣ چرکە ناوی یارییەکە دیار دەبێت
    print("\n          \033[1;33mLoading Military Assets...")
    time.sleep(2)
    os.system('clear')

# 2. بەشی سەرەکی یاری (Game Logic)
def start_game():
    print("\033[0m") # گەڕانەوە بۆ ڕەنگی ئاسایی
    print("------------------------------------------")
    print("   بەخێربێیت فەرماندە بۆ ناو TMX KURDISH   ")
    print("------------------------------------------")
    # لێرەدا دەتوانیت کۆدی شەتڕەنج یان هەر یارییەکی تر دابنێیت
    choice = input("\n[1] دەستپێکردنی یاری\n[2] زانیاری سوپا\n[3] چوونە دەرەوە\n\nفەرماندە هەڵبژێرە: ")
    
    if choice == "1":
        print("یاری دەستی پێکرد...")
    elif choice == "2":
        print("سوپای TMX ئامادەیە!")
    else:
        sys.exit()

# جێبەجێکردنی هەمووی پێکەوە
if __name__ == "__main__":
    show_intro()
    start_game()
