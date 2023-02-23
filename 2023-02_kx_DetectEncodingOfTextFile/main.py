import tkinter as tk
import tkinter.filedialog as fd
from tkinterdnd2 import DND_FILES, TkinterDnD
from chardet.universaldetector import UniversalDetector # Импортируем субмодуль chardet.universaldetector

# Открыть диалоговое окно выбора файла и запустить определение кодировки
def choose_file_and_detect():
    filetypes = (("Текстовый файл", "*.txt *.csv *.json"),
                    ("Изображение", "*.jpg *.gif *.png"),
                    ("Любой", "*.*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                    filetypes=filetypes)
    if filename:
        return detect_encoding_of_text_file(filename)

# Автоматическое определение кодировки файла
def detect_encoding_of_text_file(filename):    
    detector = UniversalDetector()
    with open(filename, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
    result = detector.close()
    lb.insert(1, '')
    lb.insert(2, f'Файл: {filename}')
    lb.insert(3, f'Кодировка: {result}')
    lb.insert(4, '---------------------')
    

root = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()

lb = tk.Listbox(root, width= 100, height=20)
lb.insert(1, 'Перетащите файл в эту область или нажмите кнопку "Открыть файл"')
# register the listbox as a drop target
lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', lambda e: detect_encoding_of_text_file(e.data))
lb.pack(padx=10, pady=10)

btn_file = tk.Button(root, text="Выбрать файл", command=choose_file_and_detect)
btn_file.pack() #padx=60, pady=10)

root.mainloop()
