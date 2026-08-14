import streamlit as st
import speech_recognition as sr
import io

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Voice Controlled Library",
    page_icon="📚",
    layout="centered"
)

# ---------------------------
# Library Storage
# ---------------------------
if "library" not in st.session_state:
    st.session_state.library = {}

library = st.session_state.library


# ---------------------------
# Voice Recognition
# ---------------------------
def recognize_audio(audio_file):
    recognizer = sr.Recognizer()

    try:
        audio_bytes = audio_file.getvalue()

        audio_source = sr.AudioFile(io.BytesIO(audio_bytes))

        with audio_source as source:
            audio_data = recognizer.record(source)

        command = recognizer.recognize_google(audio_data)

        return command.lower().strip()

    except sr.UnknownValueError:
        st.error("❌ Sorry, I could not understand the audio.")
        return ""

    except sr.RequestError:
        st.error("❌ Speech recognition service is unavailable.")
        return ""

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        return ""


# ---------------------------
# Add Book
# ---------------------------
def add_book(title):
    title = title.title()

    if title in library:
        return f"⚠️ '{title}' already exists."

    library[title] = "Available"
    return f"✅ '{title}' added successfully."


# ---------------------------
# Borrow Book
# ---------------------------
def borrow_book(title):
    title = title.title()

    if title not in library:
        return "❌ Book not found."

    if library[title] == "Borrowed":
        return "❌ Book is already borrowed."

    library[title] = "Borrowed"
    return f"📕 You borrowed '{title}'."


# ---------------------------
# Return Book
# ---------------------------
def return_book(title):
    title = title.title()

    if title not in library:
        return "❌ Book not found."

    library[title] = "Available"
    return f"✅ '{title}' returned successfully."


# ---------------------------
# Main UI
# ---------------------------
st.title("🎙️ Voice Controlled Library System")

st.write(
    "Manage your library using voice commands."
)

st.divider()

# ---------------------------
# Authentication
# ---------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:

    st.subheader("🔐 Voice Authentication")

    st.info("Say the password: 1234")

    audio = st.audio_input("🎤 Record Password")

    if audio:

        password = recognize_audio(audio)

        if password in ["1234", "one two three four"]:
            st.session_state.authenticated = True
            st.success("✅ Access Granted!")
            st.rerun()

        else:
            st.error("❌ Wrong password.")

    st.stop()


# ---------------------------
# Main Library
# ---------------------------
st.success("🔓 Access Granted")

st.subheader("🎤 Voice Command")

st.write("Try commands such as:")

st.code(
    "Add book Python Programming\n"
    "Borrow book Python Programming\n"
    "Return book Python Programming\n"
    "Show books"
)

audio = st.audio_input("🎙️ Record your command")

if audio:

    command = recognize_audio(audio)

    if command:

        st.write("🗣️ You said:", command)

        # Show books
        if "show" in command or "display" in command:
            if library:
                st.subheader("📚 Library")

                for book, status in library.items():
                    st.write(f"**{book}** → {status}")

            else:
                st.info("📚 No books in the library.")

        # Add book
        elif "add" in command:

            title = command.replace("add book", "").replace("add", "").strip()

            if title:
                st.success(add_book(title))
            else:
                st.warning("Please say the book title.")

        # Borrow book
        elif "borrow" in command:

            title = command.replace("borrow book", "").replace("borrow", "").strip()

            if title:
                st.success(borrow_book(title))
            else:
                st.warning("Please say the book title.")

        # Return book
        elif "return" in command:

            title = command.replace("return book", "").replace("return", "").strip()

            if title:
                st.success(return_book(title))
            else:
                st.warning("Please say the book title.")

        # Exit / logout
        elif "exit" in command or "logout" in command:

            st.session_state.authenticated = False
            st.rerun()

        else:
            st.warning("⚠️ Command not recognized.")


# ---------------------------
# Current Library
# ---------------------------
st.divider()

st.subheader("📖 Current Library")

if library:

    for book, status in library.items():
        st.write(f"📘 **{book}** — {status}")

else:
    st.info("No books added yet.")


# ---------------------------
# Logout
# ---------------------------
if st.button("🔒 Logout"):

    st.session_state.authenticated = False
    st.rerun()
