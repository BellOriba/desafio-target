fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
fat_total = sum(fat.values())
percentages = {state: (value / fat_total) * 100 for state, value in fat.items()}
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")