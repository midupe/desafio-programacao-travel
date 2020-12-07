print()
print("------[ TRAVEL ]------")
print()

h_partida, m_partida, s_partida = input("Partida? ").split()
h_chegada, m_chegada, s_chegada = input("Chegada? ").split()

partida = int(s_partida) + int(m_partida)*60 + int(h_partida)*60*60
chegada = int(s_chegada) + int(m_chegada)*60 + int(h_chegada)*60*60

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