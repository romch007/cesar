from tkinter import *

window = Tk()
window.geometry("300x500")
window.title('Projet césar')
# Frames principales
frame_crypt = Frame(window, borderwidth=2, relief=GROOVE)
frame_decrypt = Frame(window, borderwidth=2, relief=GROOVE)
frame_bt = Frame(window, borderwidth=2, relief=GROOVE)
frame_result = Frame(window, borderwidth=2, relief=GROOVE)

frame_crypt.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_decrypt.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_bt.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_result.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)

# Titres
Label(frame_crypt, text='Crypter').pack()
Label(frame_decrypt, text='Décrypter').pack()
Label(frame_bt, text='Bruteforcer').pack()
# Frames secondaires
frame_crypt_str = Frame(frame_crypt, borderwidth=2, relief=GROOVE)
frame_decrypt_str = Frame(frame_decrypt, borderwidth=2, relief=GROOVE)
frame_bt_str = Frame(frame_bt, borderwidth=2, relief=GROOVE)

frame_crypt_file = Frame(frame_crypt, borderwidth=2, relief=GROOVE)
frame_decrypt_file = Frame(frame_decrypt, borderwidth=2, relief=GROOVE)
frame_bt_file = Frame(frame_bt, borderwidth=2, relief=GROOVE)

frame_crypt_str.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_decrypt_str.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_bt_str.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)

frame_crypt_file.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_decrypt_file.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
frame_bt_file.pack(padx=3, pady=3, anchor=W, fill=BOTH, expand=False)
# Titres secondaires
Label(frame_crypt_str, text='Chaîne de caractère').pack()
Label(frame_decrypt_str, text='Chaîne de caractère').pack()
Label(frame_bt_str, text='Chaîne de caractère').pack()

Label(frame_crypt_file, text='Depuis un fichier').pack()
Label(frame_decrypt_file, text='Depuis un fichier').pack()
Label(frame_bt_file, text='Depuis un fichier').pack()
# Inputs de cryptage str
input_crypt_str = StringVar()
input_crypt_str.set("Chaîne à crypter")
entry_input_crypt_str = Entry(frame_crypt_str, textvariable= input_crypt_str)
entry_input_crypt_str.pack()

shift_crypt_str = StringVar()
shift_crypt_str.set(1)
entry_shift_crypt_str = Spinbox(frame_crypt_str, textvariable= shift_crypt_str, from_=-26,to=26,increment=1)
entry_shift_crypt_str.pack()

def start():
    window.mainloop()