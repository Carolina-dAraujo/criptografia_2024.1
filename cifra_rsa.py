import random

def eh_primo_probabilistico(n, k=5):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def gerar_primo_grande():
    while True:
        num = random.randint(10**9, 10**10 - 1)
        if eh_primo_probabilistico(num):
            return num

def gerar_chaves():
    p = gerar_primo_grande()
    q = gerar_primo_grande()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if mdc(e, phi) != 1:
        raise ValueError("e e φ(n) não são coprimos!")

    _, d, _ = euclides_estendido(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    return (e, n), (d, n), (p, q)

def dividir_mensagem(mensagem, n):
    tamanho_max_bloco = (n.bit_length() - 1) // 8
    mensagem_bytes = mensagem.encode('utf-8')
    return [mensagem_bytes[i:i + tamanho_max_bloco] for i in range(0, len(mensagem_bytes), tamanho_max_bloco)]

def encriptar(chave_publica, mensagem):
    e, n = chave_publica
    blocos = dividir_mensagem(mensagem, n)
    blocos_cifrados = []
    
    for bloco in blocos:
        bloco_int = int.from_bytes(bloco, 'big')
        bloco_cifrado = exp_mod(bloco_int, e, n)
        blocos_cifrados.append(bloco_cifrado)
    
    return blocos_cifrados

def descriptografar(chave_privada, blocos_cifrados):
    d, n = chave_privada
    mensagem_descriptografada = b''
    
    for bloco_cifrado in blocos_cifrados:
        bloco_int = exp_mod(bloco_cifrado, d, n)
        bloco_bytes = bloco_int.to_bytes((bloco_int.bit_length() + 7) // 8, 'big')
        mensagem_descriptografada += bloco_bytes
    
    return mensagem_descriptografada.decode('utf-8')

def exp_mod(base, expoente, modulo):
    resultado = 1
    while expoente > 0:
        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        expoente //= 2
    return resultado

def euclides_estendido(a, b):
    if b == 0:
        return a, 1, 0
    mdc_, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return mdc_, x, y

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

chave_publica, chave_privada, (p, q) = gerar_chaves()
print(f"Chave pública: {chave_publica}")
print(f"Chave privada: {chave_privada}")

while True:
    print("\nEscolha uma opção:")
    print("E: Encriptar mensagem")
    print("D: Descriptografar mensagem")
    print("F: Finalizar o programa")
    opcao = input("Opção: ").upper()

    if opcao == 'E':
        mensagem = limpar(input("Digite a mensagem a ser encriptada: "))
        cifrado = encriptar(chave_publica, mensagem)
        print(f"Mensagem encriptada: {cifrado}")
    elif opcao == 'D':
        blocos_cifrados = [int(x) for x in input("Digite os blocos cifrados separados por vírgula: ").split(",")]
        mensagem_descriptografada = descriptografar(chave_privada, blocos_cifrados)
        print(f"Mensagem descriptografada: {mensagem_descriptografada}")
    elif opcao == 'F':
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida.")
