import cv2
ajustaBrilho = lambda img, value : cv2.convertScaleAbs(img, alpha = 1, beta = value)

nome_arquivo = input("Coloque o caminho absoluto da imagem de entrada: ")
imagem = cv2.imread(nome_arquivo)
cv2.imshow("Imagem Original", imagem)

if imagem is None :
    print("Não foi possível carregar a imagem.")
else :
    while True :
        valor_brilho = float(input("Digite o valor de ajuste de brilho (-127 : 127, -300 para mostrar as imagens): "))
        
        if valor_brilho == -300:
            break

        imagem_ajustada = ajustaBrilho(imagem, valor_brilho)
        title = "Imagem Ajustada, Brilho = " + str(valor_brilho)
        cv2.imshow(title, imagem_ajustada)
cv2.waitKey(0) 
cv2.destroyAllWindows()