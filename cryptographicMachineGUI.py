import onetimepad
from tkinter import * 
         
root = Tk()
root.title("Cryptograhy Machine")
root.geometry("800x800")
  
def encryptMsg():                      
    pt = e1.get()
    ct = onetimepad.encrypt(pt, 'random')
    e2.insert(0, ct)
  
def decryptMsg():                     
    ct1 = e3.get()
    pt1 = onetimepad.decrypt(ct1, 'random')
    e4.insert(0, pt1)
      
label1 = Label(root, text ='Plain Text')               
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Encrypted Text')
label2.grid(row = 11, column = 1)
l3 = Label(root, text ="Cipher Text")
l3.grid(row = 10, column = 10)
l4 = Label(root, text ="Decrypted text")
l4.grid(row = 11, column = 10)
  
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)
  
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 13, column = 2)
  
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage)
b2.grid(row = 13, column = 11)
  
root.mainloop()