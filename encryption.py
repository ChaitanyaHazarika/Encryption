from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import messagebox, filedialog

import os 
root= Tk()
root.geometry("400x250")
root.config(bg= "blue")

file_name_entry= ""
encryption_text_data= ""
decryption_text_data=""

def savedata():
    global file_name_entry
    global encryption_text_data
    file_name= file_name_entry.get()
    file= open(file_name+".txt","w")
    data= encryption_text_data.get("1.0", END)
    ciphercode= encrypt('miku', data)
    hex_string= ciphercode.hex()
    print(hex_string)
    print(ciphercode)
    file.write(hex_string)
    file_name_entry.delete(0,END)
    encryption_text_data.delete(1.0,END)
    messagebox.showinfo('Update', "Success")


def viewData():
    global decryption_text_data
    text_file= filedialog.askopenfilename(title= "Open Text File",filetypes=(("Text File", "*.txt"),))
    name= os.path.basename(text_file)
    print(name)
    text_file= open(name,"r")
    paragraph= text_file.read()
    byte_str= bytes.fromhex(paragraph)
    original= decrypt('miku', byte_str)
    final_data= original.decode("utf-8")
    decryption_text_data.insert(END, final_data) 
    text_file.close()


def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
    decryption_window= Tk()
    decryption_window.config(bg= "green")
    decryption_window.geometry("600x500")

    decryption_text_data= Text(decryption_window, height= 20, width=72)
    decryption_text_data.place(relx= 0.5, rely= 0.35, anchor=CENTER)

    button_openfile= Button(decryption_window, text="Choose File", font=("Arial", 30), bg= "Dark Green", padx=10, relief=FLAT, command=viewData)
    button_openfile.place(relx= 0.5, rely= 0.8, anchor=CENTER)

    decryption_window.mainloop()

def startEncryption():
    global file_name_entry
    global encryption_text_data

    root.destroy()
    ecryption_window= Tk()
    ecryption_window.config(bg= "pink")
    ecryption_window.geometry("600x500")

    file_name_label= Label(ecryption_window, text="File name", font=("Arial", 13),bg= "pink")
    file_name_label.place(relx= 0.1, rely= 0.15, anchor=CENTER)

    file_name_entry= Entry(ecryption_window, font=("Arial", 15))
    file_name_entry.place(relx= 0.38, rely= 0.15, anchor=CENTER)

    button_create= Button(ecryption_window, text="Create" , font= ("Arial", 13), padx= 10, bg= "green", relief=FLAT, command=savedata )
    button_create.place(relx= 0.5, rely= 0.15, anchor=CENTER)

    encryption_text_data= Text(ecryption_window, height= 20, width=72)
    encryption_text_data.place(relx= 0.5, rely= 0.55, anchor=CENTER)
    ecryption_window.mainloop()
heading_label= Label(root, text= "Encryption Decryption", font= ("Arial", 18, "italic"), bg= "green")
heading_label.place(relx= 0.5, rely= 0.2, anchor=CENTER)

button=Button(root, text= "Start Encryption", font= ("Arial", 13), bg= "white", command=startEncryption, relief=FLAT, padx= 10)
button.place(relx= 0.3, rely= 0.6, anchor=CENTER)

button1=Button(root, text= "Start Decryption", font= ("Arial", 13), bg= "white", command=startDecryption, relief=FLAT, padx= 10)
button1.place(relx= 0.7, rely= 0.6, anchor=CENTER)











root.mainloop()