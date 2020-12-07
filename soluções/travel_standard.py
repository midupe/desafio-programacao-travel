
print()
print("------[ TRAVEL ]------")
print()

h_partida, m_partida, s_partida = input("Partida? ").split()
h_chegada, m_chegada, s_chegada = input("Chegada? ").split()

h_partida = int(h_partida)
m_partida = int(m_partida)
s_partida = int(s_partida)
h_chegada = int(h_chegada)
m_chegada = int(m_chegada)
s_chegada = int(s_chegada)

if 0 > h_partida or 0 > h_chegada or h_partida > 23 or h_chegada > 23:
    print("Horas têm valores entre 0 e 23")
    exit(1)

if 0 > m_partida or 0 > m_chegada or 0 > s_partida or 0 > s_chegada or m_partida > 59 or m_chegada > 59 or s_partida > 59 or s_chegada > 59:
    print("Minutos e Segundos têm valores entre 0 e 59")
    exit(1)

partida = s_partida + m_partida*60 + h_partida*60*60
chegada = s_chegada + m_chegada*60 + h_chegada*60*60

if partida > chegada:
    print("Partida > Chegada")
    exit(1)

duracao = chegada - partida
s_duracao = duracao
h_duracao = int(s_duracao/60/60)
s_duracao = s_duracao - h_duracao*60*60
m_duracao = int(s_duracao/60)
s_duracao = s_duracao - m_duracao*60

print("Duração = %d:%d:%d" % (h_duracao, m_duracao, s_duracao))