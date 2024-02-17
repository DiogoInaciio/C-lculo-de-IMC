# Calculo de IMC - Índice de Massa Corporal

altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual é seu peso em Kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC >= 18.5 and IMC < 24.9:
    print('PESO IDEAL')
elif IMC >= 25.0 and IMC < 29.9:
    print('LEVEMENTE ACIMA DO PESO')
elif IMC >= 30.0 and IMC < 34.9:
    print('OBESIDADE GRAU I ')
elif IMC >= 35.0 and IMC < 39.9:
    print('OBESIDADE GRAU II')    
else:
    print('OBESIDADE GRAU III')    
   
# MENOR QUE 18,5 ABAIXO DO PESO
# ENTRE 18,5 E 24,9 PESO IDEAL
# ENTRE 25,0 E 29,9 LEVEMENTE ACIMA DO PESO
# ENTRE 30,0 E 34,9 OBESIDADE GRAU I
# ENTRE 35,0 E 39,9 OBESIDADE GRAU II
# MAIOR QUE 40,0 OBESIDADE GRAU III