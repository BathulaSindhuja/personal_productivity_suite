import time
from utils import clear_screen, pause

def countdown_timer(seconds):
    clear_screen()
    while seconds > 0:
        m, s = divmod(seconds, 60)
        print(f"\rTime left: {m:02d}:{s:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def timer_menu():
    while True:
        clear_screen()
        print("=== Timer ===")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Back")
        ch = input("\nChoice: ")
        if ch == "3":
            break
        try:
            n = int(input("Enter duration: "))
        except:
            print("Invalid.")
            pause()
            continue
        seconds = n if ch == "1" else n * 60
        countdown_timer(seconds)
        pause()
