def definirRank(vitorias, derrotas):
    rankHero = ""
    saldoVitorias = vitorias - derrotas
    if (saldoVitorias <= 10):
        rankHero = "Ferro"
    elif (saldoVitorias >= 11 and saldoVitorias <= 20):
        rankHero = "Bronze"
    elif (saldoVitorias >= 21 and saldoVitorias <= 50):
        rankHero = "Prata"
    elif (saldoVitorias > 51 and saldoVitorias <= 80):
        rankHero = "Ouro"
    elif (saldoVitorias > 81 and saldoVitorias <= 90):
        rankHero = "Diamante"
    elif (saldoVitorias > 91 and saldoVitorias <= 100):
        rankHero = "Lendário"
    elif (saldoVitorias > 100):
        rankHero = "Imortal"       
    return f"O herói tem o saldo de {saldoVitorias} e está no nível de {rankHero}"

resultado = definirRank(82,35)

print(resultado)