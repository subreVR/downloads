import ctypes
import random
import time
import threading
import winsound
import os

# Load necessary Windows API functions
user32 = ctypes.windll.user32
gdi = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

# Get screen size
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Get device context for the screen
hdc = user32.GetDC(0)

# Path to your sound file (Make sure "hydro1.wav" is in the same folder as the script)
sound_file_path = os.path.join(os.getcwd(), "hydro1.wav")

# Function to show warning messages
def show_warning(title, message):
    response = ctypes.windll.user32.MessageBoxW(0, message, title, 0x4 | 0x30)  # 0x4 = Yes/No, 0x30 = Warning icon
    return response == 6  # Returns True if "Yes" is clicked

# First warning
if not show_warning("⚠ FIRST WARNING", "This is malware. Run?\n\n(You may need to run it twice if effects don't start.)"):
    exit()

# Second warning
if not show_warning("⚠ LAST WARNING", "Are you sure? I AM NOT RESPONSIBLE FOR DAMAGES!"):
    exit()

# Function to play glitchy, distorted phonk sounds in a loop
def play_phonk_sounds():
    # Lower frequencies for a deeper bass "phonk" feel
    low_frequencies = [250, 350, 500, 700]
    snare = [1000, 1200, 1500]  # Higher snare-like frequencies for rhythm

    while True:
        # Play bass-like deep tones for a phonk rhythm
        for freq in low_frequencies:
            winsound.Beep(freq, 150)  # Bass notes with longer duration
            time.sleep(random.uniform(0.3, 0.7))  # Slight delay for rhythm

        # Play snare-like higher frequencies for beats
        for beat in snare:
            winsound.Beep(beat, 100)  # Shorter duration for snare hits
            time.sleep(0.3)  # Snare delay

# Function to create extreme screen distortion and effects
def extreme_screen_effects():
    balls = []
    while True:
        try:
            # Create random balls that bounce around the screen
            if random.random() < 0.05:  # Create new balls with a small probability
                ball = {
                    "x": random.randint(0, width),
                    "y": random.randint(0, height),
                    "dx": random.choice([-1, 1]) * random.randint(10, 15),  # Speed of balls
                    "dy": random.choice([-1, 1]) * random.randint(10, 15),  # Speed of balls
                    "radius": random.randint(30, 100),  # Ball size (randomized to be bigger)
                    "color": random.choice([0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF])  # Random color
                }
                balls.append(ball)

            # Update and draw all balls
            for ball in balls:
                ball["x"] += ball["dx"]
                ball["y"] += ball["dy"]
                
                # Bounce the balls off screen edges
                if ball["x"] <= 0 or ball["x"] >= width:
                    ball["dx"] = -ball["dx"]
                if ball["y"] <= 0 or ball["y"] >= height:
                    ball["dy"] = -ball["dy"]
                
                # Draw the ball on the screen
                gdi.Ellipse(hdc, ball["x"], ball["y"], ball["x"] + ball["radius"], ball["y"] + ball["radius"])  # Bigger balls

            # Create random duplicating blocks with changing colors
            x = random.randint(0, width - 100)
            y = random.randint(0, height - 100)
            w = random.randint(50, 400)
            h = random.randint(50, 400)
            color = random.choice([0xFF0000, 0x00FF00, 0x0000FF, 0xFFFFFF, 0xFFFF00])
            gdi.PatBlt(hdc, x, y, w, h, color)
            time.sleep(random.uniform(0.05, 0.1))  # Super fast screen updates to induce insanity
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to simulate insane random window popping with changing text
def random_window_flash():
    messages = ["SYSTEM ERROR", "MALWARE DETECTED", "YOU'VE BEEN PUNKED!", "CRITICAL ERROR", "SCREEN HACKED", "USER IN DANGER"]
    while True:
        try:
            message = random.choice(messages)
            # Random message box with changing text
            ctypes.windll.user32.MessageBoxW(0, message, "WARNING", 0x10)
            time.sleep(random.uniform(0.5, 1))  # Delay between message box spams for chaos
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to show bouncing colored text "unrohydro!!!" on screen
def random_text_overlay():
    text = "unrohydro!!!"
    colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
    while True:
        try:
            x = random.randint(0, width - 100)
            y = random.randint(0, height - 50)
            color = random.choice(colors)
            # Create the text overlay with random color and position
            gdi.SetTextColor(hdc, color)
            gdi.TextOutW(hdc, x, y, text, len(text))  # Draw the text on the screen
            time.sleep(random.uniform(0.1, 0.5))  # Random delay between text displays
        except Exception as e:
            print(f"Error: {e}")
            break

# Start sound effects in a separate thread
sound_thread = threading.Thread(target=play_phonk_sounds, daemon=True)
sound_thread.start()

# Start screen effects in a separate thread
screen_thread = threading.Thread(target=extreme_screen_effects, daemon=True)
screen_thread.start()

# Start random window popups in a separate thread
window_thread = threading.Thread(target=random_window_flash, daemon=True)
window_thread.start()

# Start text overlay in a separate thread
text_thread = threading.Thread(target=random_text_overlay, daemon=True)
text_thread.start()

# Keep the script running forever
try:
    while True:
        time.sleep(1)  # Keeping the main thread alive
except KeyboardInterrupt:
    print("Script interrupted by user.")
