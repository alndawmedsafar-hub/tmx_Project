import tkinter as tk
import time

def start_game_intro():
    # دروستکردنی پەنجەرەی دەستپێک
    intro = tk.Tk()
    intro.title("TMX KURDISH")
    intro.geometry("400x300")
    intro.configure(bg='black') # باکگراوندێکی ڕەش [وەک وتت]
    
    # لۆگۆی TMX KURDISH بە ڕەنگی سپی یان زەردی درەوشاوە
    label = tk.Label(intro, text="TMX KURDISH", 
                     fg="yellow", bg="black", 
                     font=("Courier", 30, "bold"))
    label.pack(expand=True)
    
    # نووسینی ژێرەوە (بە کوردی)
    loading = tk.Label(intro, text="چاوەڕوان بە... سوپا خەریکی ئامادەسازییە", 
                       fg="white", bg="black", font=("Arial", 10))
    loading.pack(pady=10)

    # نوێکردنەوەی شاشەکە و چاوەڕوانکردن بۆ ٣ چرکە
    intro.update()
    time.sleep(3) 
    
    # داخستنی دەستپێک و چوونە ناو یارییەکە
    intro.destroy()
    print("🚀 فەرماندە، یارییەکە بە تەواوی دەستی پێکرد!")

# بانگکردنی فەرمانەکە
start_game_intro()
