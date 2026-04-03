palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'treinar', 'programador', 'futuro')

for p in palavras:
    print(f'\nAs vogais da palavra {p.upper()} são: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')