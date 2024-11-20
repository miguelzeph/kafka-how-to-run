
# Minimium Necessary to run Kafka

## Overview

**Producer**: Sends messages to a **Topic**.  
**Broker**: Receives **messages** from the `Producer`, **stores** them in the `Topic`, and **sends** them to the `Consumer`.  
**Consumer**: Processes, transforms, or sends messages to another Topic, a Database, or an external system (ex: Apache Spark).

This example demonstrates a Kafka setup with two brokers.

---


1. Start Zookeeper Server 
    - search on google for **zookeeper image**
    - https://hub.docker.com/_/zookeeper (official image)
    - image name: zookeeper

2. Start Kafka Server
    - found image name: apache/kafka image
    

3. Execute docker-compose file
sudo docker-compose up --build
p.s. --build force the reconstruction of the image


4. Acesse o container kafka para ver os scripts

Entre no Container: sudo docker exec -it kafka /bin/sh

Navegue até /opt/kafka_2.13-2.8.1/bin/kafka-topics.sh
cd /opt/kafka_2.13-2.8.1/bin/kafka-topics.sh

P.S. As vezes está em outra pasta... uma dica é usar o comando find / -name "kafka-topics.sh" ou "kafka-topics"
/usr/bin/ (por exemplo, as vezes está aqui)


liste os scripts disponíveis
ls


Create topic 


kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic helloworld
Explicação:
--bootstrap-server localhost:9092: Indica o servidor Kafka ao qual você está se conectando.
--replication-factor 1: Define que o fator de replicação é 1 (apenas um broker, já que você tem um único Kafka rodando).
--partitions 1: Cria o tópico com uma única partição.
--topic helloworld: Nome do tópico que será criado.


5. Agora vamos mandar mensagem no topico criado

kafka-console-producer.sh --topic ARTICLES --bootstrap-server localhost:9092

E agora envie mensagens... Escreva quakquer coisa e aperte ENTER...

Caso queira enviar mensagem no formato <key>:<value> você tem que executar
kafka-console-producer.sh --topic ARTICLES --bootstrap-server localhost:9092 --property parse.key=true --property key.separator=:


P.S. Quando você não utiliza as propriedades específicas para a chave (parse.key=true e key.separator), o kafka-console-producer.sh interpreta tudo como o valor da mensagem, ignorando qualquer estrutura de chave.

Se quiser enviar mensagens com chave e valor, você deve incluir essas propriedades no comando do produtor. Aqui está um guia para garantir que funcione corretamente:
ex:
article-1:{"title":"Kafka Basics","content":"Introduction to Kafka"}
article-2:{"title":"Advanced Kafka","content":"Deep dive into Kafka features"}


6. para visualizar as mensagens, execute

kafka-console-consumer --topic <TOPIC_NAME> --bootstrap-server localhost:9092 --from-beginning



7. Visualizar pelo Kafka UI (interface gráfica)

localhost:8080

Nota: Se você não usar volumes locais montados, os dados já estarão no contêiner. Nesse caso, remova os contêineres para forçar a recriação: (As vezes o kafka cai quando usa o kafka ui por causa do volume do ocntainer anterior)

docker-compose down --volumes


8. CONSUMIDORES - servem para processar/transform, enviar para outro sistema, ou salvar em um DB as imagens

no exemplo anterior eu mostrei uma maneira de usar um consumer...

kafka-console-consumer --topic <TOPIC_NAME> --bootstrap-server localhost:9092 --from-beginning

Mas nós vamos criar o NOSSO CONSUMER... 
- Instale a biblioteca: pip install confluent-kafka
- Crie um Scrip Python
- Crie um docker container
- Adicione no seu docker-compose o consumidor
- Rode o serviço


----

Faça um test para parar um Broker no docker

```bash
sudo docker-compose stop kafka-broker-2
```

veja como as mensagens se comportam...

Agora ligue novamente o Broker

```bash
sudo docker-compose up kafka-broker-2
```