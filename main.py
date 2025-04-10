import customtkinter as ctk

calculation = ""
history = []

def update_text(content):
    entry_box.delete(0, "end")
    entry_box.insert(0, content)

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_text(calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        history.append(f"{calculation} = {result}")
        calculation = result
        update_text(result)
        update_history()
    except:
        calculation = ""
        update_text("Error")

def clear_all():
    global calculation
    calculation = ""
    update_text("")

def backspace():
    global calculation
    calculation = calculation[:-1]
    update_text(calculation)

def update_history():
    if len(history) > 5:
        del history[0]
    history_label.configure(text="\n".join(history[-5:]))

def on_key(event):
    key = event.char
    if key in "0123456789.+-*/()":
        add_to_calculation(key)
    elif event.keysym == "Return":
        evaluate_calculation()
    elif event.keysym == "BackSpace":
        backspace()

# Application Settings
ctk.set_appearance_mode("dark")  # "light" or "dark"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("350x500")

# Entry box
entry_box = ctk.CTkEntry(app, font=("Arial", 24), justify="right")
entry_box.pack(pady=20, padx=20, fill="x")

# History Label
history_label = ctk.CTkLabel(app, text="", font=("Arial", 12), anchor="w", justify="left")
history_label.pack(padx=20, fill="x")

# Buttons
buttons = [
    ("7", lambda: add_to_calculation("7")),
    ("8", lambda: add_to_calculation("8")),
    ("9", lambda: add_to_calculation("9")),
    ("/", lambda: add_to_calculation("/")),
    ("4", lambda: add_to_calculation("4")),
    ("5", lambda: add_to_calculation("5")),
    ("6", lambda: add_to_calculation("6")),
    ("*", lambda: add_to_calculation("*")),
    ("1", lambda: add_to_calculation("1")),
    ("2", lambda: add_to_calculation("2")),
    ("3", lambda: add_to_calculation("3")),
    ("-", lambda: add_to_calculation("-")),
    (".", lambda: add_to_calculation(".")),
    ("0", lambda: add_to_calculation("0")),
    ("=", evaluate_calculation),
    ("+", lambda: add_to_calculation("+")),
    ("C", clear_all),
    ("←", backspace),
    ("(", lambda: add_to_calculation("(")),
    (")", lambda: add_to_calculation(")")),
]

# Editing Buttons
frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

for i, (text, command) in enumerate(buttons):
    row = i // 4
    col = i % 4
    btn = ctk.CTkButton(frame, text=text, command=command, width=70, height=50, font=("Arial", 16))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Keyboard listener
app.bind("<Key>", on_key)

app.mainloop()
