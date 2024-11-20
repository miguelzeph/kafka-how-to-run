from confluent_kafka import Consumer
import json

# Configurações do consumidor
consumer_conf = {
    'bootstrap.servers': 'kafka:9092,kafka-broker-2:9093',  # Inclua os dois brokers
    'group.id': 'articles-processor-group',
    'auto.offset.reset': 'earliest'
}


consumer = Consumer(consumer_conf)
consumer.subscribe(['ARTICLES'])

print("Consumidor de ARTICLES está esperando mensagens...")

try:
    while True:
        msg = consumer.poll(5.0)  # Espera por 5 segundo
        if msg is None:
            continue
        if msg.error():
            print(f"Erro no consumidor: {msg.error()}")
            continue

        # Decodifica a mensagem
        article = json.loads(msg.value().decode('utf-8'))
        print(f"Mensagem recebida: {article}")

        # Processa a mensagem (exemplo: adiciona 'processed')
        article['processed'] = True
        print(f"Artigo processado: {article}")

finally:
    consumer.close()
