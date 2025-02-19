FROM confluentinc/cp-kafka-connect:7.5.0

# Install the MQTT Connector from Confluent Hub
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-mqtt:latest
