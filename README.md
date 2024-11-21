
# Minimium Necessary to run Kafka


This guide details how to set up and operate **Kafka**, including its main components and practical instructions for creating topics, sending messages, and consuming data.

---

## **Theoretical Introduction**

- **Cluster (Scalability):** Manages a set of brokers in Kafka.
  - **Zookeeper** or Kafka itself is responsible for managing the cluster.

- **Broker (Storage/Message Management):** 
  - A Kafka server that receives messages from **producers** and sends them to **consumers**.
  - Manages topics and retains messages for a configured period.

- **Topic (Organization):**
  - A channel where messages are organized and stored. Topics are managed by brokers.

- **Consumer (Processing):**
  - Connects to the cluster to read messages and process them. It can send data to other systems (e.g., Spark, databases, or another topic).

- **Producer (Sending):**
  - Creates and sends messages to topics.

### **Important Notes:**
1. **Zookeeper** defines an **Active Control Broker (AC)**:
   - Responsible for creating topics, altering partitions, and redistributing leaders.
   - In case of failure, **Zookeeper** automatically assigns another broker as AC.
2. **Offset:** Works as an ID for messages.

---

## **Setting Up the Environment**

### **1. Start Zookeeper Server**
- Search for the official image on Docker Hub: [Zookeeper](https://hub.docker.com/_/zookeeper)
- Image name: `zookeeper`

### **2. Start Kafka Server**
- Recommended image: `apache/kafka`

### **3. Execute `docker-compose`**
- Start services using the command:
  ```bash
  sudo docker-compose up --build
  ```
  - `--build`: Forces the reconstruction of images.

---

## **Basic Operations in Kafka**

### **4. Access the Kafka Container**
- Enter the container:
  ```bash
  sudo docker exec -it kafka /bin/sh
  ```
- Navigate to the Kafka scripts directory:
  ```bash
  cd /opt/kafka_2.13-2.8.1/bin/
  ```
  - Use `find` to locate scripts if they are in another location:
    ```bash
    find / -name "kafka-topics.sh"
    ```

### **5. Create a Topic**
- Command to create a topic:
  ```bash
  kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic helloworld
  ```
  **Explanation of parameters:**
  - `--bootstrap-server`: Kafka server.
  - `--replication-factor 1`: Replication factor (1 for a single broker).
  - `--partitions 1`: Number of partitions.
  - `--topic helloworld`: Name of the topic.

### **6. Send Messages**
- To send messages to the created topic:
  ```bash
  kafka-console-producer.sh --topic helloworld --bootstrap-server localhost:9092
  ```
  - Write any message and press ENTER to send it.

#### **Messages in <key>:<value> format**
- Use the following command to include keys and values:
  ```bash
  kafka-console-producer.sh --topic helloworld --bootstrap-server localhost:9092 --property parse.key=true --property key.separator=:
  ```
  **Example:**
  ```text
  article-1:{"title":"Kafka Basics","content":"Introduction to Kafka"}
  article-2:{"title":"Advanced Kafka","content":"Deep dive into Kafka features"}
  ```

### **7. Consume Messages**
- Command to consume messages:
  ```bash
  kafka-console-consumer.sh --topic helloworld --bootstrap-server localhost:9092 --from-beginning
  ```
  **Explanation:**
  - `--from-beginning`: Reads all messages from the beginning.

---

## **Kafka Graphical Interface**
- Access the graphical interface via the browser at `localhost:8080`.

### **Note on Volumes:**
- To avoid issues with persistent data, remove old containers:
  ```bash
  docker-compose down --volumes
  ```

---

## **Create a Custom Consumer**
- Install the Python library:
  ```bash
  pip install confluent-kafka
  ```
- Create a Python script for the consumer.
- Add the consumer to the `docker-compose` and start the service.

---

## **Testing and Failure Scenarios**

### **Stopping a Broker**
- To stop a broker:
  ```bash
  sudo docker-compose stop kafka-broker-2
  ```
  - Observe how messages behave.

### **Restarting the Broker**
- Restart the broker:
  ```bash
  sudo docker-compose up kafka-broker-2
  ```

---

This manual covers everything from basic theory to practical configurations in Kafka, helping you understand and operate its main components.