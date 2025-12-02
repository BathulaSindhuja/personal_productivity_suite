import os
import json
from datetime import datetime
from utils import clear_screen, pause

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)

def add_note():
    clear_screen()
    title = input("Title: ").strip()
    content = input("Content: ").strip()
    if not title or not content:
        print("Title and content cannot be empty.")
        pause()
        return
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Note added!")
    pause()

def view_notes():
    clear_screen()
    notes = load_notes()
    if not notes:
        print("No notes found.")
        pause()
        return
    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Time: {note['created_at']}")
        print(f"Content: {note['content']}")
        print("-" * 30)
    pause()

def search_notes():
    clear_screen()
    word = input("Enter keyword: ").strip().lower()
    notes = load_notes()
    results = [
        note for note in notes if word in note["title"].lower() or word in note["content"].lower()
    ]
    if not results:
        print("No matching notes.")
    else:
        for note in results:
            print(f"\n{note['id']} - {note['title']} : {note['content']}")
            print("-" * 30)
    pause()

def delete_note():
    clear_screen()
    notes = load_notes()
    if not notes:
        print("No notes.")
        pause()
        return
    try:
        note_id = int(input("Enter ID to delete: "))
    except:
        print("Invalid input.")
        pause()
        return
    new_notes = [n for n in notes if n["id"] != note_id]
    for idx, note in enumerate(new_notes, start=1):  # re-assign IDs
        note["id"] = idx
    save_notes(new_notes)
    print("Note deleted.")
    pause()

def notes_menu():
    while True:
        clear_screen()
        print("=== Notes Manager ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Back")
        ch = input("\nChoice: ")
        if ch == "1":
            add_note()
        elif ch == "2":
            view_notes()
        elif ch == "3":
            search_notes()
        elif ch == "4":
            delete_note()
        elif ch == "5":
            break
