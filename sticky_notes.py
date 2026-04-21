# Sticky Notes App
# Author: ashiyafarhin-blip
# Project 2 - GitHub Portfolio

import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content
    }
    notes.append(note)
    save_notes(notes)
    print("✅ Note added successfully!")

def view_notes(notes):
    if not notes:
        print("❌ No notes found!")
        return
    print("\n========= YOUR STICKY NOTES =========")
    for note in notes:
        print(f"\n📌 [{note['id']}] {note['title']}")
        print(f"    {note['content']}")
    print("=====================================")

def delete_note(notes):
    view_notes(notes)
    if not notes:
        return
    try:
        note_id = int(input("\nEnter note ID to delete: "))
        note_found = False
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                save_notes(notes)
                print("🗑️ Note deleted successfully!")
                note_found = True
                break
        if not note_found:
            print("❌ Note not found!")
    except ValueError:
        print("❌ Invalid input!")

def search_note(notes):
    keyword = input("Enter keyword to search: ").lower()
    results = [n for n in notes if 
               keyword in n["title"].lower() or 
               keyword in n["content"].lower()]
    if results:
        print("\n🔍 Search Results:")
        for note in results:
            print(f"\n📌 [{note['id']}] {note['title']}")
            print(f"    {note['content']}")
    else:
        print("❌ No matching notes found!")

def main():
    notes = load_notes()
    while True:
        print("\n======= STICKY NOTES APP =======")
        print("1. ➕ Add Note")
        print("2. 📋 View All Notes")
        print("3. 🗑️  Delete Note")
        print("4. 🔍 Search Note")
        print("5. 🚪 Exit")
        print("=================================")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            search_note(notes)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

main()
