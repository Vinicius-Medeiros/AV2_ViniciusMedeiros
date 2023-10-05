import cv2

ajustaBrilho = lambda img, value : cv2.convertScaleAbs(img, alpha = 1, beta = value)
mensagem_erro = lambda: print("Não foi possível carregar a imagem.")
mensagem_finalizacao = lambda: print("\nQuando quiser finalizar o programa, selecione uma imagem e pressione qualquer tecla!\n")

nome_arquivo = input("Coloque o caminho absoluto da imagem de entrada: ")
imagem = cv2.imread(nome_arquivo)
cv2.imshow("Imagem Original", imagem)

imagem is not None or mensagem_erro()
valor_brilho = float(input("Digite o valor de ajuste de brilho (-127 : 127, -300 para mostrar as imagens): "))

while valor_brilho != -300:
    imagem_ajustada = ajustaBrilho(imagem, valor_brilho)
    title = "Imagem Ajustada, Brilho = " + str(valor_brilho)
    cv2.imshow(title, imagem_ajustada)
    valor_brilho = float(input("Digite o valor de ajuste de brilho (-127 : 127, -300 para mostrar as imagens): ")) 

mensagem_finalizacao()
cv2.waitKey(0) 
cv2.destroyAllWindows()