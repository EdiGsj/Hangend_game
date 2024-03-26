import os
import random as rm

random_number = rm.randint(0, 50)

word_array = [
    'caçada', 'carro', 'futebol', 'escola', 'bicicleta', 
    'banana', 'computador', 'livro', 'janela', 'porta', 
    'cidade', 'telefone', 'lua', 'sol', 'praia', 
    'gato', 'cachorro', 'amigo', 'chocolate', 'camiseta', 
    'sapato', 'jardim', 'parque', 'piano', 'viagem',
    'mão', 'ação', 'anão', 'pão', 'agência',
    'coração', 'floresta', 'beleza', 'álcool', 'coruja', 
    'pássaro', 'cachecol', 'pá', 'louco', 'amor', 'nômade',
    'café', 'avião', 'ilusão', 'cão', 'paçoca',
    'canção', 'cidadão', 'irmã', 'aniversário'
]
word = word_array[random_number].lower()
word_key = ['_ ' for _ in range(len(word))]

chance = 5

def render_interface(chance):
    os.system('cls')
    if chance > 0:
        print(f"Você tem {chance} chances" if chance > 1 else f"Você tem {chance} chance")
    print('_Forca_')
    print('  ____'if chance <= 5 else '|')
    print('  |  |'if chance <= 5 else ' |')
    print('  |  |'if chance <= 4 else '  |')
    print('  |  O' if chance <= 3 else '  |')
    print('  | /|\\' if chance <= 2 else '  |')
    print('  |  |' if chance <= 1 else '  |')
    print('  | / \\' if chance <= 0 else '  |')
    print('__|__'if chance <= 5 else '')
    word_key_formated = ' '.join(word_key)
    print(word_key_formated)
    
def convert_letter(user_letra, word):
    if user_letra == 'a':
        if 'á' in word:
            return 'á'
        elif 'ã' in word:
            return 'ã'
        elif 'â' in word:
            return 'â' 
        else:
            return user_letra
        
    elif user_letra == 'e':
        if 'é' in word:
            return 'é'
        elif 'e' and 'ê' in word:
            return 'ê'
        else:
            return user_letra
        
    elif user_letra == 'i':
        if 'í' in word:
            return 'í'
        elif 'î' in word:
            return 'î'
        else:
            return user_letra
        
    elif user_letra == 'o':
        if 'ó' in word:
            return 'ó'
        elif 'ô' in word:
            return 'ô'
        elif 'õ' in word:
            return 'õ' 
        else:
            return user_letra
        
    elif user_letra == 'u':
        if 'ú' in word:
            return 'ú'
        elif 'û' in word:
            return 'û' 
        else:
            return user_letra
        
    elif user_letra == 'c':
        if 'ç' in word:
            return 'ç'
        else:
            return user_letra
        
    else:
        return user_letra

def change_victory():
    if ''.join(word_key) == word:
        render_interface(chance)
        print(word)
        print("Você venceu!")
        exit()

def change_lose():
    if chance == 0:
        render_interface(chance)
        print('Você perdeu. Tente novamente')
        exit() 

while chance > 0:
    render_interface(chance)
    user_letra = input('Diga uma letra: ').lower()
    #Aqui é a idéia de colocar tudo abaixo dentro de um for
    #Para executar mais de uma vez

    if len(user_letra) == 1 and user_letra.isalpha(): # obs no == 1
        if user_letra in word:
            for i in range(len(word)):
                if word[i] == user_letra:
                    word_key[i] = user_letra            
        user_letra = convert_letter(user_letra, word)
        if user_letra in word:
            for i in range(len(word)):
                if word[i] == user_letra:
                    word_key[i] = user_letra
            change_victory()
        else:
            chance -= 1
            change_lose()
    else:
        print('DIGITE APENAS UMA LETRA')
