import random
import time
import uuid

paises = ["BR", "US", "FR", "DE"]
dispositivos = ["mobile", "desktop"]

def gerar_transacao():
    valor = round(random.uniform(10, 5000), 2)
    hora = random.randint(0, 23)
    pais = random.choice(paises)
    dispositivo = random.choice(dispositivos)
    tentativas = random.randint(1, 5)
    cartao_presente = random.choice([True, False])

    # lógica de fraude
    fraude = 0

    if valor > 3000 and hora < 6:
        fraude = 1
    if tentativas > 3:
        fraude = 1
    if pais != "BR" and valor > 2000:
        fraude = 1
    if cartao_presente:
        fraude = 1

    return {
        "id": str(uuid.uuid4()),
        "valor": valor,
        "hora": hora,
        "pais": pais,
        "dispositivo": dispositivo,
        "tentativas": tentativas,
        "cartao_presente": cartao_presente,
        "fraude": fraude
    }

# simulação contínua
while True:
    transacao = gerar_transacao()
    print(transacao)
    time.sleep(1)

    import csv

    with open("data/transacoes.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=transacao.keys())

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(transacao)