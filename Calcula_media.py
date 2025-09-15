def calcula_media (n1: float,n2: float,n3: float,n4: float):
        return (n1,n2,n3,n4)/4

def situacao_media(media):

    if media >= 7:
            return "Aprovado"
    elif media >= 5:
            return "Recuperação"
    else:
        return("Reprovado(a)")

def programa_terminal():  
    nome = str(input(""))
    nota1 = (input("Digite a primeira nota:"))
    nota2 = (input("Digite a primeira nota:"))
    nota3 = (input("Digite a primeira nota:"))
    nota4 = (input("Digite a primeira nota:"))

    media = calcula_media(nota1, nota2, nota3, nota4)
    situação = situacao_media(media)

    print(f"{nome} está {situação} com média: {media}")                  

if __name__ == "__main__":
        programa_terminal()
