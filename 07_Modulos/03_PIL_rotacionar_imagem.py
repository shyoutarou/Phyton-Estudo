from PIL import Image #Importar a biblioteca

im = Image.open("/home/exemplo.jpg") #Abrir a imagem
im2 = im.rotate(45) #Rotacionar a imagem em 45 graus
im2.save("/home/exemploRotacionado.jpg") #Salvar imagem rotacionada