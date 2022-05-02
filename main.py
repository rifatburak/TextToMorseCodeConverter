import tkinter
from tkinter import messagebox




alfabe_dict={
    "a" : "•- ",
    "b" : "-••• ",
    "c" : "-•-• ",
    "d" : "-•• ",
    "e" : "• ",
    "f" : "••-• ",
    "g" : "--• ",
    "h" : "•••• ",
    "i" : "•• ",
    "j" : "•--- ",
    "k" : "-•- ",
    "l" : "•-•• ",
    "m" : "-- ",
    "n" : "-• ",
    "o" : "--- ",
    "p" : "•--• ",
    "q" : "--•- ",
    "r" : "•-• ",
    "s" : "••• ",
    "t" : "- ",
    "u" : "••- ",
    "v" : "•••- ",
    "w" : "•-- ",
    "x" : "-••- ",
    "y" : "-•-- ",
    "z" : "--•• ",
    " " : "/"
}

def convert_to_morse(text):
    text = text.lower()
    morse_code = ""
    for char in text:
        morse_code += alfabe_dict[char]
    return morse_code

def is_program_continue():
    tekrar = input("Would you like to translate again?? y/n").lower()
    if tekrar == "y":
        return True
    elif tekrar == "n":
        return False
    else:
        print("You made a wrong choice, please re-enter")
        is_program_continue()


def get_entry():
    entry2.delete(0, "end")
    text = entry1.get()
    if text == "" or text == " ":
        error = messagebox.showerror(title="Error", message="Please enter a text.")
        return error
    text = convert_to_morse(text)
    entry2.insert(0, f"{text}")
    msg = messagebox.askquestion(title=f"Convert", message=f"Mors code:  {text} \n \n Would you like to translate again?")
    if msg == "yes":
        entry1.delete(0, "end")
    else:
        window.destroy()
    return msg

window = tkinter.Tk()

window.title("Mors Code Converter")
window.iconbitmap("icon.ico")
window.geometry("480x360")
bg = tkinter.PhotoImage(file="Your_image.png") # It's UI background image.
label1 = tkinter.Label( window, image = bg)
label1.place(x = 0, y = 0)
entry1 = tkinter.Entry()
entry1.config( width=60)
entry1.pack(pady = 50)
entry2 = tkinter.Entry()
entry2.config( width=60)
entry2.pack(pady = 50)
cevir = tkinter.Button(window,command=get_entry, text="Convert to morse code")
cevir.pack(pady = 50)

window.mainloop()





