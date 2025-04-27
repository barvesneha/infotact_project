from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import login_page  # Import the login module


root = Tk()
root.withdraw()  
login_win = login_page.open_login_window(root)
root.wait_window(login_win)


if not getattr(login_win, "authenticated", False):
    root.destroy()
    exit()




root.deiconify()  
root.state("zoomed")  
root['bg'] = 'orchid'  
root.title('Real-time Translator')  


Label(root, text="Language Translator", font="Arial 28 bold", bg='lavender').pack(pady=20)


frame = Frame(root, bg='lavender')
frame.pack(pady=20)

left_frame = Frame(frame, bg='lavender')
left_frame.grid(row=0, column=0, padx=50)

Label(left_frame, text="Enter Text", font='arial 16 bold', bg='white smoke').pack()
Input_text = Text(left_frame, font='arial 14', height=10, width=50)
Input_text.pack(pady=10)


right_frame = Frame(frame, bg='lavender')
right_frame.grid(row=0, column=1, padx=50)

Label(right_frame, text="Output", font='arial 16 bold', bg='white smoke').pack()
Output_text = Text(right_frame, font='arial 14', height=10, width=50, wrap=WORD, padx=5, pady=5)
Output_text.pack(pady=10)


lang_frame = Frame(root, bg='lavender')
lang_frame.pack(pady=10)


language = list(LANGUAGES.values())


Label(lang_frame, text="Select Source Language:", font='arial 14 bold', bg='lavender').pack(side=LEFT, padx=10)
src_lang = ttk.Combobox(lang_frame, values=language, width=25, font="arial 12")
src_lang.pack(side=LEFT)
src_lang.set('Auto Detect')  


Label(lang_frame, text="Select Target Language:", font='arial 14 bold', bg='lavender').pack(side=LEFT, padx=10)
dest_lang = ttk.Combobox(lang_frame, values=language, width=25, font="arial 12")
dest_lang.pack(side=LEFT)
dest_lang.set('Choose Language')  


def Translate():
    try:
        translator = Translator()
        src_language = src_lang.get()
        dest_language = dest_lang.get()

        
        src_code = [code for code, lang in LANGUAGES.items() if lang == src_language]
        dest_code = [code for code, lang in LANGUAGES.items() if lang == dest_language]

        if src_code:
            src_code = src_code[0]
        else:
            src_code = 'auto'  

        if dest_code:
            dest_code = dest_code[0]
        else:
            Output_text.delete("1.0", END)
            Output_text.insert(END, "Please select a valid target language.")
            return

        translation = translator.translate(Input_text.get("1.0", END), src=src_code, dest=dest_code)
        Output_text.delete("1.0", END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        print(f"Translation error: {e}")


trans_btn = Button(root, text='Translate', font='arial 16 bold', pady=10, padx=20, command=Translate, bg='orange', activebackground='green')
trans_btn.pack(pady=20)


root.mainloop()
