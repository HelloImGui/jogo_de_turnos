from time import sleep
print(f'{"-" * 70}\n{" Ellement Battle ": ^70}\n{"-" * 70}')

# Atributos dos personagens
# Estão divididos em: Nome, vida, dano, defesa e velocidade
# Foi criada uma lista para cada personagem, onde podemos acessar seus atributos de forma eficiente
muriel = ['Muriel', 1500, 110, 15, 150]
atks_muriel = ['Ataque 1', 10, 2, 'Ataque 2', 15, 1]
enki = ['Enki', 1500, 120, 23, 120]
pyron = ['Pyron', 1200, 115, 19, 130]
# aires = ['Aires', 850, 75, 25, 190]


def linha():
    print(f'\n{" ":^50}\n')


def ataque():
    if winner[0] == 'Muriel':
        atk_muriel()
    elif winner[0] == 'Enki':
        atk_enki()
    elif winner[0] == 'Pyron':
        atk_pyron()
    vida = loser[1] - (winner[2] + extra)
    print(f'''{winner[0]} ataca {loser[0]} causando {winner[2]} mais {extra} de dano.
Vida de {loser[0]}: {vida}''')
    loser[1] = vida
    linha()


def defesa():
    if loser[0] == 'Muriel':
        atk_muriel()
    elif loser[0] == 'Enki':
        atk_enki()
    elif loser[0] == 'Pyron':
        atk_pyron()
    vida = winner[1] - (loser[2] + extra)
    print(f'''{loser[0]} ataca {winner[0]} causando {loser[2]} mais {extra} de dano.
Vida de {winner[0]}: {vida}''')
    winner[1] = vida



def atk_muriel():
    global extra, qnt
    choice = int(input(f'''Escolha o ataque de Muriel:
{atks_muriel[0]}:          {atks_muriel[1]} de dano.
{atks_muriel[2]}:          {atks_muriel[3]} de dano.
Ataque 1 ou Ataque 2: '''))

    if choice == 1 and atks_muriel[2] > 0:
        extra = atks_muriel[1]
        qnt = atks_muriel[2] - 1
        print(f'Você ainda tem {qnt} ataques para usar.')
    elif choice == 2:
        if atks_muriel[5] > 0:
            extra = atks_muriel[4]
            print(f'Você ainda tem {atks_muriel[5]} ataques para usar.')
            atks_muriel[5] = atks_muriel[5] - 1
    else:
        print(f'Você não pode mais usar esse ataque. {atks_muriel[5]} cargas.')
    atks_muriel[2] = qnt
    linha()


def atk_enki():
    global extra

    atks_enki = ['Ataque 1', 10, 'Ataque 2', 15]
    choice = int(input(f'''Escolha o ataque de Enki: 
{atks_enki[0]}:          {atks_enki[2]}:
Dano: {atks_enki[1]}           Dano: {atks_enki[3]}
Ataque 1 ou Ataque 2: '''))

    if choice == 1:
        extra = atks_enki[1]
    elif choice == 2:
        extra = atks_enki[3]
    linha()


def atk_pyron():
    global extra

    atks_pyron = ['Ataque 1', 10, 'Ataque 2', 15]
    choice = int(input(f'''Escolha o ataque de Pyron: 
{atks_pyron[0]}:          {atks_pyron[2]}:
Dano: {atks_pyron[1]}           Dano: {atks_pyron[3]}
Ataque 1 ou Ataque 2: '''))

    if choice == 1:
        extra = atks_pyron[1]
    elif choice == 2:
        extra = atks_pyron[3]
    linha()


def atk_aires():
    global extra

    atks_aires = ['Ataque 1', 10, 'Ataque 2', 15]
    choice = int(input(f'''Escolha o ataque de Aires: 
{atks_aires[0]}:          {atks_aires[2]}:
Dano: {atks_aires[1]}           Dano: {atks_aires[3]}
Ataque 1 ou Ataque 2: '''))

    if choice == 1:
        extra = atks_aires[1]
    elif choice == 2:
        extra = atks_aires[3]
    linha()


# Tabela com os atributos para o usuário escolher o personagem
print(f'''    
           [1]          [2]        [3]          
           Muriel       Enki       Pyron        
Elemento:   Água        Terra       Fogo         
Vida:       {muriel[1]}         {enki[1]}       {pyron[1]}             
Dano:        {muriel[2]}          {enki[2]}        {pyron[2]}    
Defesa:       {muriel[3]}           {enki[3]}         {pyron[3]}    
Velocidade:  {muriel[4]}          {enki[4]}        {pyron[4]}          
''')

# Mostra ao usuário qual personagem escolheu
# Atribui os atributos do personagem escolhido à p1 e p2
p1 = int(input('Esolha o primeiro personagem: '))
if p1 == 1:
    print('Paragéns! Você escolheu a Muriel, elemento Água.')
    p1 = muriel[:]
elif p1 == 2:
    print('Paragéns! Você escolheu o Enki, elemento Terra.')
    p1 = enki[:]
elif p1 == 3:
    print('Paragéns! Você escolheu o Pyron, elemento Fogo.')
    p1 = pyron[:]
"""else:
    print('Paragéns! Você escolheu a Aires, elemento Ar.')
    p1 = aires[:]"""

p2 = int(input('Escolha o segundo personagem: '))
if p2 == 1:
    print('Paragéns! Você escolheu a Muriel, elemento Água.')
    p2 = muriel[:]
elif p2 == 2:
    print('Paragéns! Você escolheu o Enki, elemento Terra.')
    p2 = enki[:]
elif p2 == 3:
    print('Paragéns! Você escolheu o Pyron, elemento Fogo.')
    p2 = pyron[:]
"""else:
    print(f'Paragéns! Você escolheu a Aires, elemento Ar.')
    p2 = aires[:]"""

# Após o print ele exibe um '.' de cada vez com intervalo de 0.5sec
print(end=f'O jogo já vai começar')
for c in range(0, 3):
    print(end='.')
    sleep(0.5)
print('\n')

# Com base na velocidade, é decidido quem começa atacando (quem tiver a maior vel começa)
# Atribuimos os atributos de quem tem a maior velocidade para winner e a menor para loser
winner = [0]
loser = [0]
if p1[4] > p2[4]:
    print(f'{p1[0]} tem {p1[4] - p2[4]} pontos de velocidade a mais que {p2[0]}. Por isso {p1[0]} começa o round!')
    winner = p1[:]
    loser = p2[:]
else:
    print(f'{p2[0]} tem {p2[4] - p1[4]} pontos de velocidade a mais que {p1[0]}. Por isso {p2[0]} começa o round!')
    winner = p2[:]
    loser = p1[:]

# Sistema de 3 Rounds
# Cada round é constituido por um turno de ataque e outro de defesa
for c in range(1, 4):
    print(f'{c}º Round!')
    ataque()
    defesa()


if winner[1] > loser[1]:
    print(f'{winner[0]} venceu!!!')
else:
    print(f'{loser[0]} venceu!!!')
