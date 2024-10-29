import json

with open("dados.json", 'r') as f:
    DATA = json.loads(f.read())

def avg(data):
    """Retorna a média geral de faturamento no mês.
        Ignora dias com faturamento igual a 0."""
    total = 0
    i = 0
    for day in data:
        if day['valor'] != 0:
            total += day['valor']
            i += 1
    return total/i

def greater_fat(data):
    """Retorna o dia com maior valor de faturamento ocorrido em um dia do mês."""
    return max(data, key=lambda x: x['valor'])

def less_fat(data):
    """Retorna o dia com menor valor de faturamento ocorrido em um dia do mês."""
    return min(data, key=lambda x: x['valor'])

def less_fat_nonzero(data):
    """Retorna o dia com menor valor de faturamento ocorrido em um dia do mês.
        Ignora dias com faturamento igual a 0."""
    nonzero_days = [day for day in data if day['valor'] > 0]
    return min(nonzero_days, key=lambda x: x['valor'])

def above_avg(data):
    """Retorna o número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""
    return len([day for day in data if day['valor'] > avg(data)])

def main():
    print(f"Menor valor de faturamento no mês foi: R${less_fat(DATA)['valor']} ocorrido no dia {less_fat(DATA)['dia']}.")
    print(f"Menor valor de faturamento no mês (ignorando dias sem faturamento) foi: R${less_fat_nonzero(DATA)['valor']} ocorrido no dia {less_fat_nonzero(DATA)['dia']}.")
    print(f"Maior valor de faturamento no mês foi: R${greater_fat(DATA)['valor']} ocorrido no dia {greater_fat(DATA)['dia']}.")
    print(f"O número de dias no mês em que o valor de faturamento foi superior à média mensal: {above_avg(DATA)}")

if __name__ == "__main__":
    main()