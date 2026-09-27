import json
import os

def calcular_pace(distancia_km, tempo_minuto):
    pace = tempo_minuto / distancia_km
    return pace

def formatar_pace(pace_min_km):
    minutos = int(pace_min_km) #pega o valor inteiro
    fracao = pace_min_km - minutos #pega o decimal que não esta no inteiro separadamente
    segundos = round(fracao * 60)
    return f"{minutos}:{segundos:02d} min/km"

def prever_tempo(pace_min_km, nova_distancia_km):
    #estima o tempo total para percorrer outra distancia, no mesmo pace
    tempo_previsto = pace_min_km * nova_distancia_km
    return tempo_previsto

def carregar_historico():
    if os.path.exists("historico_treino.json"):
        with open("historico_treino.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_treino(historico, treino):
    #salva os treinos no arquivo .json
    historico.append(treino)
    with open ("historico_treino.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=2)

def mostrar_historico(historico):
    if not historico:
        print ("Nenhum treino Registrado ainda.")
        return
    for i, treino in enumerate(historico, start=1):
        pace_formatado = formatar_pace(treino["pace"])
        print(f"{i}. {treino['distancia_km']} km em {treino['tempo_minuto']} min -> {pace_formatado}")

####

historico = carregar_historico()

while True:
    print("\n=== Calculadora de Pace de Corrida ===")
    print("1. Calcular pace de um treino")
    print("2. Prever tempo para outra distância")
    print("3. Ver histórico de treinos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        distancia = float(input("Distância percorrida (km): "))
        tempo = float(input("Tempo gasto (minutos): "))
        pace = calcular_pace(distancia, tempo)
        print(f"Seu pace foi de {formatar_pace(pace)}")

        salvar = input("Salvar esse treino no histórico? (s/n): ")
        if salvar == "s":
            salvar_treino(historico, {"distancia_km": distancia, "tempo_minuto": tempo, "pace": pace})
            print("Treino salvo!")

    elif opcao == "2":
        pace_atual = float(input("Seu pace atual (min/km, ex: 5.5): "))
        nova_distancia = float(input("Nova distância (km): "))
        tempo_previsto = prever_tempo(pace_atual, nova_distancia)
        print(f"Nesse pace, {nova_distancia} km levariam cerca de {tempo_previsto:.1f} minutos.")

    elif opcao == "3":
        mostrar_historico(historico)

    elif opcao == "4":
        print("Até a próxima corrida!")
        break

    else:
        print("Opção inválida, tente de novo.")