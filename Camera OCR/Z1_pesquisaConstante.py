import cv2
import tkinter as tk
from tkinter import messagebox
import pytesseract as ocr

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

captura = cv2.VideoCapture(0)

mensagemBox = tk.Tk()
mensagemBox.geometry('300x200')

while True:
    ret, frame = captura.read()#Pega o frame
    cv2.imshow('Captura:', frame)#Transmiti o frame
    frase = ocr.image_to_string(frame)#Lê o frame
    if len(frase) > 0:#Verifica se há texto na variavel frase
        print(frase)
    if cv2.waitKey(1) & 0xFF == 27:#Se apertar ESC saí da aplicação/https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
        msg = messagebox.askokcancel('OCR Teste', 'Aplicação Finalizada')
        if msg == 'ok':
            break
        else:
            mensagemBox.destroy()


captura.release()
cv2.destroyAllWindows()
