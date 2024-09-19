# Programa para calcular a idade em dias

# Leitura da idade em anos, meses e dias
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

# Cálculo da idade total em dias
idade_em_dias = (anos * 365) + (meses * 30) + dias

# Exibição do resultado
print("A idade expressa em dias é: ", idade_em_dias)
