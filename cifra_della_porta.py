def charRange(c1, c2):
    lista = []
    for c in range(ord(c1), ord(c2) + 1):
        lista.append(chr(c))
    return lista

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
        if char.isalpha():
            char_sem_acento = acentos.get(char.upper(), char.upper())
            texto_limpo += char_sem_acento

    return texto_limpo.upper()

grelha_della_porta = {
    'A': "nopqrstuvwxyzabcdefghijklm",
    'B': "nopqrstuvwxyzabcdefghijklm",
    'C': "opqrstuvwxyzabcdefghijklm",
    'D': "opqrstuvwxyzabcdefghijklm",
    'E': "pqrstuvwxyzabcdefghijklmno",
    'F': "pqrstuvwxyzabcdefghijklmno",
    'G': "qrstuvwxyzabcdefghijklmnop",
    'H': "qrstuvwxyzabcdefghijklmnop",
    'I': "rstuvwxyzabcdefghijklmnopq",
    'J': "rstuvwxyzabcdefghijklmnopq",
    'K': "stuvwxyzabcdefghijklmnopqr",
    'L': "stuvwxyzabcdefghijklmnopqr",
    'M': "tuvwxyzabcdefghijklmnopqrs",
    'N': "tuvwxyzabcdefghijklmnopqrs",
    'O': "uvwxyzabcdefghijklmnopqrst",
    'P': "uvwxyzabcdefghijklmnopqrst",
    'Q': "vwxyzabcdefghijklmnopqrstu",
    'R': "vwxyzabcdefghijklmnopqrstu",
    'S': "wxyzabcdefghijklmnopqrstuv",
    'T': "wxyzabcdefghijklmnopqrstuv",
    'U': "xyzabcdefghijklmnopqrstuvw",
    'V': "xyzabcdefghijklmnopqrstuvw",
    'W': "yzabcdefghijklmnopqrstuvwx",
    'X': "yzabcdefghijklmnopqrstuvwx",
    'Y': "zabcdefghijklmnopqrstuvwxy",
    'Z': "zabcdefghijklmnopqrstuvwxy"
}

def repetir_palavra_chave(palavra_chave, mensagem):
    repeticao = (palavra_chave * (len(mensagem) // len(palavra_chave) + 1))[:len(mensagem)]
    return repeticao

def cifra_della_porta(mensagem, palavra_chave):
    palavra_chave_repetida = repetir_palavra_chave(palavra_chave, mensagem)
    mensagem_cifrada = []
    
    for i in range(len(mensagem)):
        letra_mensagem = mensagem[i]
        letra_chave = palavra_chave_repetida[i]
        
        if letra_mensagem.isalpha():
            index = ord(letra_mensagem) - ord('A')
            mensagem_cifrada.append(grelha_della_porta[letra_chave][index])
        else:
            mensagem_cifrada.append(letra_mensagem)
    
    return ''.join(mensagem_cifrada)

def decifra_della_porta(mensagem_cifrada, palavra_chave):
    palavra_chave_repetida = repetir_palavra_chave(palavra_chave, mensagem_cifrada)
    mensagem_decifrada = []
    
    for i in range(len(mensagem_cifrada)):
        letra_cifrada = mensagem_cifrada[i]
        letra_chave = palavra_chave_repetida[i]
        
        if letra_cifrada.isalpha():
            index = grelha_della_porta[letra_chave].index(letra_cifrada.lower())
            mensagem_decifrada.append(chr(index + ord('A')))
        else:
            mensagem_decifrada.append(letra_cifrada)
    
    return ''.join(mensagem_decifrada)

print("Bem-vindo(a) à cifra Della Porta, para cifrar, digite 'C', para decifrar, digite 'D', e para finalizar o programa, digite 'F'.")
opcao = input().upper()

if opcao == 'C':
    palavra_chave = limpar(input("Digite a palavra-chave: "))
    mensagem_original = limpar(input("Digite a mensagem original: "))
    mensagem_cifrada = cifra_della_porta(mensagem_original, palavra_chave)
    print(f"Mensagem Cifrada: {mensagem_cifrada}")
elif opcao == 'D':
    palavra_chave = limpar(input("Digite a palavra-chave: "))
    mensagem_cifrada = limpar(input("Digite a mensagem cifrada: "))
    mensagem_decifrada = decifra_della_porta(mensagem_cifrada, palavra_chave)
    print(f"Mensagem Decifrada: {mensagem_decifrada}")
elif opcao == 'F':
    print("Programa finalizado.")
else:
    print("Opção inválida.")
