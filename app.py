import speech_recognition as sr

# ---------------------------
# Simple Library Storage
# ---------------------------
library = {}

# ---------------------------
# Speech Recognition Function
# ---------------------------
def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        command = recognizer.recognize_google(audio)
        command = command.lower().strip()

        print("🗣 You said:", command)
        return command

    except sr.WaitTimeoutError:
        print("⌛ No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("❌ Could not understand your voice.")
        return ""

    except sr.RequestError:
        print("❌ Internet connection required for speech recognition.")
        return ""

# ---------------------------
# Add Book
# ---------------------------
def add_book():
    print("📚 Say the book title.")

    title = listen()

    if title:
        title = title.title()

        if title in library:
            print("⚠ Book already exists.")
        else:
            library[title] = "Available"
            print(f"✅ '{title}' added successfully.")

# ---------------------------
# Borrow Book
# ---------------------------
def borrow_book():
    print("📖 Say the book title to borrow.")

    title = listen().title()

    if title in library:
        if library[title] == "Available":
            library[title] = "Borrowed"
            print(f"📕 You borrowed '{title}'.")
        else:
            print("❌ Book already borrowed.")
    else:
        print("❌ Book not found.")

# ---------------------------
# Return Book
# ---------------------------
def return_book():
    print("📘 Say the book title to return.")

    title = listen().title()

    if title in library:
        library[title] = "Available"
        print(f"✅ '{title}' returned successfully.")
    else:
        print("❌ Book not found.")

# ---------------------------
# Show Books
# ---------------------------
def show_books():
    print("\n========== LIBRARY ==========")

    if not library:
        print("No books available.")
        return

    for book, status in library.items():
        print(f"{book}  -->  {status}")

# ---------------------------
# Main Program
# ---------------------------
def main():

    print("=" * 45)
    print("🎙 VOICE CONTROLLED LIBRARY SYSTEM")
    print("=" * 45)

    print("🔐 Say the password.")

    password = listen()

    if password not in ["1234", "one two three four"]:
        print("❌ Wrong password.")
        return

    print("\n✅ Access Granted!")

    while True:

        print("\nAvailable Commands")
        print("------------------")
        print("• Add Book")
        print("• Borrow Book")
        print("• Return Book")
        print("• Show Books")
        print("• Exit")

        command = listen()

        if "add" in command:
            add_book()

        elif "borrow" in command:
            borrow_book()

        elif "return" in command:
            return_book()

        elif "show" in command:
            show_books()

        elif "exit" in command:
            print("👋 Thank you for using the Voice Controlled Library System.")
            break

        else:
            print("⚠ Command not recognized.")

# ---------------------------
# Run Program
# ---------------------------
if __name__ == "__main__":
    main()