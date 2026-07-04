from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    source_lang = comb_sor.get().lower()
    target_lang = comb_dest.get().lower()

    text = Sor_txt.get("1.0", END).strip()

    if text == "":
        return

    try:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        dest_txt.delete("1.0", END)
        dest_txt.insert(END, translated)

    except Exception as e:
        dest_txt.delete("1.0", END)
        dest_txt.insert(END, f"Error:\n{e}")


root = Tk()
root.title("Language Translator")
root.geometry("500x600")
root.configure(bg="pink")

Label(
    root,
    text="Language Translator",
    font=("Times New Roman", 28, "bold"),
    bg="pink"
).pack(pady=10)

Label(
    root,
    text="Source Text",
    font=("Times New Roman", 16, "bold"),
    bg="pink"
).pack()

Sor_txt = Text(root, font=("Arial", 14), height=7)
Sor_txt.pack(padx=10, fill=X)

languages = GoogleTranslator().get_supported_languages()

frame = Frame(root, bg="pink")
frame.pack(pady=15)

comb_sor = ttk.Combobox(frame, values=languages, state="readonly", width=18)
comb_sor.grid(row=0, column=0, padx=5)
comb_sor.set("english")

Button(
    frame,
    text="Translate",
    command=translate_text
).grid(row=0, column=1, padx=10)

comb_dest = ttk.Combobox(frame, values=languages, state="readonly", width=18)
comb_dest.grid(row=0, column=2, padx=5)
comb_dest.set("hindi")

Label(
    root,
    text="Translated Text",
    font=("Times New Roman", 16, "bold"),
    bg="pink"
).pack()

dest_txt = Text(root, font=("Arial", 14), height=7)
dest_txt.pack(padx=10, fill=X)

root.mainloop()