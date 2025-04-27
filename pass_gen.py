
import tkinter as tk
from tkinter import ttk, font, messagebox, filedialog
import random
import string

class PasswordTextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator and Text Editor")
        self.root.geometry("800x600")

        self.password_storage = []

        self.tab_control = ttk.Notebook(root)

        self.tab_password = ttk.Frame(self.tab_control)
        self.tab_text_editor = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_password, text="Password Generator")
        self.tab_control.add(self.tab_text_editor, text="Text Editor")

        self.tab_control.pack(expand=1, fill="both")

        self.create_password_tab()
        self.create_text_editor_tab()

    def create_password_tab(self):
        frame = ttk.Frame(self.tab_password, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Password Length:").pack(anchor="w")
        self.pass_length = tk.IntVar(value=12)
        ttk.Spinbox(frame, from_=4, to=50, textvariable=self.pass_length, width=10).pack(anchor="w", pady=5)

        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(frame, text="Include Lowercase", variable=self.use_lower).pack(anchor="w")
        ttk.Checkbutton(frame, text="Include Uppercase", variable=self.use_upper).pack(anchor="w")
        ttk.Checkbutton(frame, text="Include Numbers", variable=self.use_digits).pack(anchor="w")
        ttk.Checkbutton(frame, text="Include Symbols", variable=self.use_symbols).pack(anchor="w")

        ttk.Button(frame, text="Generate Password", command=self.generate_password).pack(pady=10)

        self.password_output = tk.Entry(frame, font=("Arial", 14))
        self.password_output.pack(fill="x", pady=10)

        ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        ttk.Button(frame, text="Save Password", command=self.save_password).pack(pady=5)

    def generate_password(self):
        length = self.pass_length.get()
        characters = ''
        if self.use_lower.get():
            characters += string.ascii_lowercase
        if self.use_upper.get():
            characters += string.ascii_uppercase
        if self.use_digits.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_output.delete(0, tk.END)
        self.password_output.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_output.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def save_password(self):
        password = self.password_output.get()
        if password:
            self.password_storage.append(password)
            messagebox.showinfo("Saved", "Password saved securely within the app.")

    def create_text_editor_tab(self):
        self.text_editor = tk.Text(self.tab_text_editor, wrap="word", font=("Arial", 12), background="#ADD8E6", foreground="black")
        self.text_editor.pack(expand=1, fill="both")

        toolbar = tk.Frame(self.tab_text_editor)
        toolbar.pack(fill="x")

        bold_btn = ttk.Button(toolbar, text="Bold", command=self.make_bold)
        bold_btn.pack(side="left", padx=2)

        italic_btn = ttk.Button(toolbar, text="Italic", command=self.make_italic)
        italic_btn.pack(side="left", padx=2)

        open_btn = ttk.Button(toolbar, text="Open", command=self.open_file)
        open_btn.pack(side="left", padx=2)

        save_btn = ttk.Button(toolbar, text="Save", command=self.save_file)
        save_btn.pack(side="left", padx=2)

        theme_btn = ttk.Button(toolbar, text="Change Theme", command=self.change_theme)
        theme_btn.pack(side="left", padx=2)

        font_btn = ttk.Button(toolbar, text="Change Font", command=self.change_font)
        font_btn.pack(side="left", padx=2)

    def make_bold(self):
        try:
            current_tags = self.text_editor.tag_names("sel.first")
            if "bold" in current_tags:
                self.text_editor.tag_remove("bold", "sel.first", "sel.last")
            else:
                bold_font = font.Font(self.text_editor, self.text_editor.cget("font"))
                bold_font.configure(weight="bold")
                self.text_editor.tag_configure("bold", font=bold_font)
                self.text_editor.tag_add("bold", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def make_italic(self):
        try:
            current_tags = self.text_editor.tag_names("sel.first")
            if "italic" in current_tags:
                self.text_editor.tag_remove("italic", "sel.first", "sel.last")
            else:
                italic_font = font.Font(self.text_editor, self.text_editor.cget("font"))
                italic_font.configure(slant="italic")
                self.text_editor.tag_configure("italic", font=italic_font)
                self.text_editor.tag_add("italic", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "w", encoding="utf-8") as file:
                content = self.text_editor.get(1.0, tk.END)
                file.write(content.strip())

    def change_theme(self):
        current_bg = self.text_editor.cget("background")
        if current_bg == "#ADD8E6":
            self.text_editor.config(background="white", foreground="black")
        else:
            self.text_editor.config(background="#ADD8E6", foreground="black")

    def change_font(self):
        new_font = ("Courier New", 14)
        self.text_editor.config(font=new_font)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordTextEditorApp(root)
    root.mainloop()
