times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Cinco primerios colocados: ', times[:5])
print('Os quatro últimos colocados: ', times[-4:])
ordem = sorted(times)
print('Lista dos times em ordem alfebética: ', ordem)
print('Chapecoense está na posição: ', times.index('Chapecoense'))
