#Atividade 1 - Cripto - Ana Carolina de Araújo Nunes

#Range com caracteres do alfabeto
def charRange(c1, c2):
    lista = []
    for c in range (ord(c1), ord(c2)+1):
        lista = lista + [chr(c)]
    return lista

#print(charRange('A', 'Z'))


#Função limpar:

def limpar(texto):
    

    acentos = {
        "Á": "A", "À": "A", "Ã": "A", "Â": "A", "Ä": "A",
        "É": "E", "È": "E", "Ê": "E", "Ë": "E",
        "Í": "I", "Ì": "I", "Î": "I", "Ï": "I",
        "Ó": "O", "Ò": "O", "Õ": "O", "Ô": "O", "Ö": "O",
        "Ú": "U", "Ù": "U", "Û": "U", "Ü": "U",
        "Ç": "C"
    }
    
    texto_limpo = ""
    for char in texto:
        if char != " ":
            if char.isalpha():
                char_sem_acento = acentos.get(char.upper(), char.upper())
                texto_limpo += char_sem_acento


    texto_limpo = texto_limpo.upper()
    return texto_limpo


texto_usuario = input()
texto_limpo = limpar(texto_usuario)
print(texto_limpo)
