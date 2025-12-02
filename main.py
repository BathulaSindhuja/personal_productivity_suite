from utils import clear_screen, pause
from calculator import calculator_menu
from notes_manager import notes_menu
from timer_tool import timer_menu
from file_organizer import file_organizer_menu

def main_menu():
    while True:
        clear_screen()
        print("===== Personal Productivity Suite =====")
        print("1. Calculator")
        print("2. Notes Manager")
        print("3. Timer")
        print("4. File Organizer")
        print("5. Exit")
        choice = input("\nEnter choice: ")
        if choice == "1":
            calculator_menu()
        elif choice == "2":
            notes_menu()
        elif choice == "3":
            timer_menu()
        elif choice == "4":
            file_organizer_menu()
        elif choice == "5":
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            pause()

if __name__ == "__main__":
    main_menu()

