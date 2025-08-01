import time
import random
import threading
import pygame
import pygetwindow as gw
from screeninfo import get_monitors

# === Constants ===
AUDIO_FILE = "C:/Users/LENOVO/Desktop/python/audio.mp3"  # Make sure this file exists in your working directory

intrusive_thoughts = [
    "Are you sure you're breathing right?",
    "What if your mouth is full of air only?",
    "Oooohhh gadddd, ur eating up airrr...",
    "Did you forget to chew your thoughts?",
    "Hey, control your air intake, beta!",
    "Air is precious, don’t waste it!",
    "Maybe you should swallow less air next time.",
    "Imagine if air was calories... trouble!",
]

# === Initialize pygame mixer ===
pygame.mixer.init()

def play_audio():
    try:
        pygame.mixer.music.load(AUDIO_FILE)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error playing audio: {e}")

def show_intrusive_thought():
    thought = random.choice(intrusive_thoughts)
    print(f"[Intrusive Thought] {thought}")

def random_voice_note():
    while True:
        wait_time = random.randint(10, 60)
        time.sleep(wait_time)
        threading.Thread(target=play_audio).start()

def random_intrusive_thoughts():
    while True:
        wait_time = random.randint(5, 30)
        time.sleep(wait_time)
        show_intrusive_thought()

def contains_vowels(text):
    vowels = "aeiouAEIOU"
    return any(char in vowels for char in text)

def generate_vowel_emojis(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    emojis = ['😵‍💫', '😹', '🤯', '🫢', '🙃', '😂', '😳', '😈', '😴', '👀']
    return ' '.join(random.choice(emojis) for _ in range(vowel_count))

def delayed_trigger(delay):
    time.sleep(delay)
    choice = random.choice(['audio', 'thought', 'both'])
    if choice == 'audio':
        play_audio()
    elif choice == 'thought':
        show_intrusive_thought()
    else:
        play_audio()
        time.sleep(2)
        show_intrusive_thought()

def monitor_active_window():
    last_window = None
    while True:
        time.sleep(1)
        try:
            window = gw.getActiveWindow()
            if window:
                title = window.title.strip()
                if title != last_window and title:
                    last_window = title
                    print(f"Detected new active window: {title}")
                    
                    # Vowel detection and emoji spam
                    if contains_vowels(title):
                        print(f"🔍 Detected vowels in: '{title}'")
                        emoji_line = generate_vowel_emojis(title)
                        print(f"Vowel chaos: {emoji_line}")

                    # Random delayed intrusive thought or audio
                    delay = random.randint(3, 10)
                    threading.Thread(target=delayed_trigger, args=(delay,)).start()
        except Exception as e:
            print(f"Error getting active window: {e}")

def print_screen_resolution():
    try:
        monitors = get_monitors()
        primary = monitors[0]  # primary monitor
        width, height = primary.width, primary.height
        total_pixels = width * height
        print(f"Your primary screen resolution is {width}x{height} pixels.")
        print(f"That means you have {total_pixels:,} pixels on your screen.")
    except Exception as e:
        print(f"Could not get screen resolution: {e}")

if __name__ == "__main__":
    print("🌀 Useless app with voice notes, intrusive thoughts, and app-open triggers started!")
    print_screen_resolution()

    threading.Thread(target=random_voice_note, daemon=True).start()
    threading.Thread(target=random_intrusive_thoughts, daemon=True).start()
    monitor_active_window()
