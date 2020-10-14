import cv2
import pytesseract as ocr

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()#Pega o frame
    cv2.imshow('Captura:', frame)#Transmiti o frame
    if cv2.waitKey(1) & 0xFF == 32:#Se apertar ESPAÇO a aplicação le a tela/https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
        frase = ocr.image_to_string(frame)  # Lê o frame
        if len(frase) > 0:#Verifica se há texto na variavel frase
            frase.replace(" ","")
            print(frase, 0)
        else:
            print('Nada Encontrado')
    if cv2.waitKey(1) & 0xFF == 27:#Se apertar ESC saí da aplicação/https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
        print('Aplicação Finalizada')
        break


captura.release()
cv2.destroyAllWindows()
