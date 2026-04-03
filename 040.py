nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'O aluno tirou {nota1:.1f} e {nota2:.1f}. A média ficou {media:.1f}')
    print('\033[0;31;41mREPROVADO\033[0m')
elif media >= 5 and media <= 6.9:
    print(f'O aluno tirou {nota1:.1f} e {nota2:.1f}. A média ficou {media:.1f}')
    print('\033[0;33;43mRECUPERAÇÃO\033[0m')
elif media >= 7:
    print(f'O aluno tirou {nota1:.1f} e {nota2:.1f}. A média ficou {media:.1f}')
    print('\033[0;32;42mAPROVADO\033[0m')