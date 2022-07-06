import tkinter as tk
import random


def new_alphabet():
    global alphabet
    global temp
    if len(alphabet) == 0:
        alphabet = ["ก",'ข','ฃ','ค','ฅ','ฆ','ง','จ','ฉ','ช','ซ','ฌ','ญ','ฎ','ฏ','ฐ','ฑ','ฒ','ณ','ด','ต','ถ','ท','ธ','น',
                    'บ','ป','ผ','ฝ','พ','ฟ','ภ','ม','ย','ร','ล','ว','ศ','ษ','ส','ห','ฬ','อ','ฮ']
    temp = random.choice(alphabet)
    alphabet.remove(temp)
    greeting["text"] = temp
    ht["text"] = ""
    print(alphabet)

def hints():
    ht["text"] = hint[temp]


hint = {"ก": "kai",'ข': "khai",'ฃ': "khuot",'ค': "khvay",'ฅ': "khon",'ฆ': "rakhang",'ง': "ngu",'จ': "chan",'ฉ': "chhing",
            'ช': "chhang",'ซ': "so",'ฌ': "cher",'ญ': "ying",'ฎ': "chhakda",'ฏ': "baktak",'ฐ': "than",'ฑ': "montho",
            'ฒ': "puthav",'ณ': "nen",'ด': "dek",'ต': "tao",'ถ': "thung",'ท': "thakhan",'ธ': "thong",'น': "nu",
            'บ': "baimai",'ป': "pla",'ผ': "pheung",'ฝ': "fa",'พ': "parn",'ฟ': "fun",'ภ': "sompao",'ม': "ma",
            'ย': "yak",'ร': "reu",'ล': "ling",'ว': "vern",'ศ': "sala",'ษ': "resi",'ส': "seu",'ห': "hip",'ฬ': "chola",
            'อ': "ang",'ฮ': "nokhuuk"}
temp = "ก"
alphabet = []
window = tk.Tk()
greeting = tk.Label(
    text="สวัสดี",
    foreground="blue",
    font=("", 100),
    width=5,
    height=2)
ht = tk.Label(
    text="",
    foreground="blue")
button = tk.Button(
    text="New Alphabet",
    width=25,
    height=5,
    font=("Arial", 20),
    bg="blue",
    fg="yellow",
    command=new_alphabet
)
button2 = tk.Button(
    text="HINT",
    width=25,
    height=1,
    font=("Arial", 7),
    bg="red",
    fg="yellow",
    command=hints
)

greeting.pack()
ht.pack()
button.pack()
button2.pack()


window.mainloop()