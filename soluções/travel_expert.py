def travel():
    try:
        h_partida, m_partida, s_partida = input("Partida? ").split()
        h_chegada, m_chegada, s_chegada = input("Chegada? ").split()
    except:
        print("Não introduziste todos os dados")
        return 1

    try:
        h_partida = int(h_partida)
        m_partida = int(m_partida)
        s_partida = int(s_partida)
        h_chegada = int(h_chegada)
        m_chegada = int(m_chegada)
        s_chegada = int(s_chegada)
    except:
        print("Apenas podes utilizar números")
        return 1


    if 0 > h_partida or 0 > h_chegada or h_partida > 23 or h_chegada > 23:
        print("Horas têm valores entre 0 e 23")
        return 1

    if 0 > m_partida or 0 > m_chegada or 0 > s_partida or 0 > s_chegada or m_partida > 59 or m_chegada > 59 or s_partida > 59 or s_chegada > 59:
        print("Minutos e Segundos têm valores entre 0 e 59")
        return 1

    partida = s_partida + m_partida*60 + h_partida*60*60
    chegada = s_chegada + m_chegada*60 + h_chegada*60*60

    if partida > chegada:
        print("Partida > Chegada")
        return 1

    duracao = chegada - partida
    s_duracao = duracao
    h_duracao = int(s_duracao/60/60)
    s_duracao = s_duracao - h_duracao*60*60
    m_duracao = int(s_duracao/60)
    s_duracao = s_duracao - m_duracao*60

    if duracao == 0:
        print("És a pessoa mais rápido do mundo :p")
        print("Introduziste a mesma partida e chegada")
    else:
        print("Duração = %d:%d:%d" % (h_duracao, m_duracao, s_duracao))
    
    return 0


print()
print("------[ TRAVEL ]------")
print()

continuar = 's'
count = 0

while continuar is 's':
    t = travel()
    if t is 1:
        count += 1
    if t is 0 or count is 3:
        count = 0
        print()
        continuar = input("Realizar novos cálculos? s/n ")
    
    print()

print("Bons estudos :)")
print("by midupe")