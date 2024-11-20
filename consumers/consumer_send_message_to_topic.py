from confluent_kafka import Consumer, Producer
import json

# Configurações do consumidor
consumer_conf = {
    'bootstrap.servers': 'kafka:9092,kafka-broker-2:9093',  # Inclua os dois brokers
    'group.id': 'send-msg-topic-group',
    'auto.offset.reset': 'earliest'
}

# Configurações do produtor
producer_conf = {
    'bootstrap.servers': 'kafka:9092,kafka-broker-2:9093'  # Use os nomes dos contêineres
}

consumer = Consumer(consumer_conf)
producer = Producer(producer_conf)

consumer.subscribe(['ARTICLES'])

print("Consumidor de ARTICLES está esperando mensagens para enviar ao tópico ARTICLES_PROCESSED...")


# Message expected
# {"id":123, "title":"Coding Just War Theory: Artificial Intelligence in Warfare"}


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

        # Processa a mensagem (exemplo: envia ao tópico ARTICLES_PROCESSED)
        processed_message = {
            "id": article.get("id"),
            "title": article.get("title"),
            "processed": True
        }

        # Envia para o tópico ARTICLES_PROCESSED
        producer.produce(
            'ARTICLES_PROCESSED',
            key=str(article.get("id")),  # Usando 'id' como chave
            value=json.dumps(processed_message).encode('utf-8')
        )
        producer.flush()
        print(f"Mensagem enviada para ARTICLES_PROCESSED: {processed_message}")

finally:
    consumer.close()
