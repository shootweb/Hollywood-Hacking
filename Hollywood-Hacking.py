import tkinter as tk
import threading
import random
import time
import secrets

# Get screen dimensions
try:
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
except:
    screen_width = 1920
    screen_height = 1080

# Calculate window dimensions
window_width = screen_width // 2
window_height = screen_height // 2

# Popup dimensions (1/6 of screen size)
popup_width = screen_width // 6
popup_height = screen_height // 6

# Global flag to check if the app is running
app_running = True

# Window Functions
def gibberish_hashes(parent):
    window = tk.Toplevel(parent)
    window.title("")
    window.geometry(f"{window_width}x{window_height}+0+0")
    text = tk.Text(window, bg="black", fg="lime", font=("Courier", 10))
    text.pack(expand=True, fill='both')

    def update_gibberish():
        while app_running:
            gibberish = secrets.token_hex(random.randint(8, 60))
            text.insert(tk.END, gibberish + "\n")
            text.see(tk.END)
            time.sleep(0.1)

    threading.Thread(target=update_gibberish, daemon=True).start()


def meaningless_memory_relocation(parent):
    window = tk.Toplevel(parent)
    window.title("")
    window.geometry(f"{window_width}x{window_height}+{window_width}+0")
    text = tk.Text(window, bg="black", fg="white", font=("Courier", 10))
    text.pack(expand=True, fill='both')

    def generate_memory_relocation():
        base_src = random.randint(0x100000000000, 0x1FFFFFFFFFFF)
        offset = random.randint(0x1000, 0xFFFF)
        base_dst = base_src + random.randint(0x10000, 0x100000)

        src_range = f"0x{base_src:012X} - 0x{(base_src + offset):012X}"
        dst_range = f"0x{base_dst:012X} - 0x{(base_dst + offset):012X}"

        return f"{src_range}  =>  {dst_range}"

    def meaningless_messages():
        packets = ["Injecting Packet...", "Cracking Password...", "Intercepting Packet...", "Grabbing Passwords...", "Decrypting Files..."]
        while app_running:
            message = random.choice(packets)
            relocation = generate_memory_relocation()
            formatted_message = f"    {message:<25} {relocation}\n"
            text.insert(tk.END, formatted_message)
            text.see(tk.END)
            time.sleep(0.7)

    threading.Thread(target=meaningless_messages, daemon=True).start()


def matrix_hashes(parent):
    window = tk.Toplevel(parent)
    window.title("")
    window.geometry(f"{window_width}x{window_height}+0+{window_height}")
    text = tk.Text(window, bg="black", fg="lime", font=("Courier", 12))
    text.pack(expand=True, fill='both')

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def matrix_effect():
        while app_running:
            line = ''.join(random.choice(chars) for _ in range(90))
            text.insert(tk.END, "  " + line + "\n")
            text.see(tk.END)
            time.sleep(0.02)

    threading.Thread(target=matrix_effect, daemon=True).start()


def random_popup(parent):
    def create_popup():
        if not app_running:
            return

        x_position = (screen_width - popup_width) // 2
        y_position = (screen_height - popup_height) // 2

        popup = tk.Toplevel(parent)
        popup.title("ALERT!")
        popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

        message, color = random.choice([("ACCESS GRANTED", "green"), ("SECURITY BREACH", "red")])
        label = tk.Label(popup, text="    " + message, fg=color, font=("Courier", 32, "bold"))
        label.pack(expand=True)

        popup.after(3000, popup.destroy)

    while app_running:
        time.sleep(random.randint(10, 30))
        try:
            parent.after(0, create_popup)
        except tk.TclError:
            break


def cool_hexes(parent):
    window = tk.Toplevel(parent)
    window.title("Hex Data")
    window.geometry(f"{window_width}x{window_height}+{window_width}+{window_height}")
    text = tk.Text(window, bg="black", font=("Courier", 10))
    text.pack(expand=True, fill='both')

    def generate_hex():
        while app_running:
            hex_pairs = [(f"{random.randint(0, 255):02X}", f"{random.randint(0, 255):02X}") for _ in range(17)]
            text.insert(tk.END, "\n")
            for pair in hex_pairs:
                color = random.choice(["red", "green"])
                text.insert(tk.END, f" {pair[0]} {pair[1]} ", (color,))

            text.see(tk.END)
            time.sleep(0.3)

    text.tag_config("red", foreground="red")
    text.tag_config("green", foreground="green")

    threading.Thread(target=generate_hex, daemon=True).start()


# Main function
def main():
    global app_running
    root = tk.Tk()
    root.withdraw()

    gibberish_hashes(root)
    meaningless_memory_relocation(root)
    matrix_hashes(root)
    cool_hexes(root)

    threading.Thread(target=random_popup, args=(root,), daemon=True).start()

    try:
        root.mainloop()
    finally:
        app_running = False


if __name__ == "__main__":
    main()
