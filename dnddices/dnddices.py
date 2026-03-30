import random
import customtkinter

def roll(dice):
    value = random.randint(1, dice)
    textbox.delete("1.0", customtkinter.END)
    textbox.insert(customtkinter.INSERT, value, "center")

app = customtkinter.CTk()
app.geometry("400x300")
app.title("DnD-Dices")

### Layout
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

### Left Frame
left_frame = customtkinter.CTkFrame(app, fg_color="transparent")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

label_left = customtkinter.CTkLabel(left_frame, text="Wähle deinen Würfel")
label_left.grid(row=0, column=0, pady=5)

dice_values = [4, 6, 8, 10, 12, 20]

for i, dice in enumerate(dice_values, start=1):
    button = customtkinter.CTkButton(
        left_frame,
        text=f"W{dice}",
        command=lambda d=dice: roll(d)
    )
    button.grid(row=i, column=0, pady=2, sticky="w")

### Right Frame
right_frame = customtkinter.CTkFrame(app, fg_color="transparent")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

label_right = customtkinter.CTkLabel(right_frame, text="Ergebnis")
label_right.grid(row=0, column=0, pady=5)

textbox = customtkinter.CTkTextbox(right_frame, width=100, height=100, font=("Arial", 28, "bold"))
textbox.grid(row=1, column=0, pady=25)
textbox.tag_config("center", justify="center")
textbox.configure(spacing1=40)

app.mainloop()