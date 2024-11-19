# Minimium Necessary to run Kafka

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

Navegue até /usr/bin/ (onde estão os scripts)
cd /usr/bin


liste os scripts disponíveis
ls


Create topic 


kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic helloworld
Explicação:
--bootstrap-server localhost:9092: Indica o servidor Kafka ao qual você está se conectando.
--replication-factor 1: Define que o fator de replicação é 1 (apenas um broker, já que você tem um único Kafka rodando).
--partitions 1: Cria o tópico com uma única partição.
--topic helloworld: Nome do tópico que será criado.


5. Agora vamos mandar mensagem no topico criado

kafka-console-producer --topic helloworld --bootstrap-server localhost:9092

E agora envie mensagens... escreva qualquer coisa e aperta enter


para visualizar as mensagens, execute

kafka-console-consumer --topic helloworld --bootstrap-server localhost:9092 --from-beginning



6. Visualizar pelo Kafka UI (interface gráfica)

localhost:8080

Nota: Se você não usar volumes locais montados, os dados já estarão no contêiner. Nesse caso, remova os contêineres para forçar a recriação: (As vezes o kafka cai quando usa o kafka ui por causa do volume do ocntainer anterior)

docker-compose down --volumes