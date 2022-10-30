from tkinter import Tk, Label, PhotoImage, messagebox, Canvas, Entry, Button


def validate():
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    card_number = card_entry.get()
    try:
        if card_number == "x":
            valid_or_invalid.itemconfig(the_text, text="Goodbye")
            exit()
        card_number = card_number.replace(" ", "")
        card_number = card_number[::-1]

        for x in card_number[::2]:
            sum_odd_digits += int(x)
        for x in card_number[1::2]:
            x = int(x) * 2
            if x >= 10:
                sum_even_digits += (1+(x % 10))
            else:
                sum_even_digits += x
        total = sum_odd_digits + sum_even_digits

        if total % 10 == 0:
            valid_or_invalid.itemconfig(the_text, text="VALID")
        else:
            valid_or_invalid.itemconfig(the_text, text="INVALID")
    except ValueError:
        messagebox.showerror(title="Error", message="Sorry there was an unrecognized character. Please make sure that the input is all numbers.")


window = Tk()
window.config(width=600, height=400, bg="black",)
window.title("Credit Card Validation")

image = "35-351784_credit-card-payment-bank-credit-history-transparent-background.png"
pic = PhotoImage(file=image)
canvas = Canvas(width=300, height=200, bg="black", highlightthickness=0)
canvas.place(x=150, y=25)
canvas.create_image(150,25, image=pic)

card_entry = Entry(width=35)
card_entry.place(x=178, y=245)


validate_button = Button(width=10, text="validate", command=validate)
validate_button.place(x=415, y=242) 

valid_or_invalid = Canvas(width=200, height=100, bg="black", highlightthickness=0)
the_text = valid_or_invalid.create_text(100, 50, text="", width=180, font=("Arial", 30, "bold"), fill="white")
valid_or_invalid.place(x=190, y=265)

directions_label = Label(text="Please type in the credit card number you would like to check. \nOr type 'x' in the entry box and press the 'validate' button to exit.")
directions_label.config(bg="black", fg="white")
directions_label.place(x=120, y=190)




window.mainloop()