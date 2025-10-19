# event_bus.py - simple Kafka-like interface placeholder
class EventBus:
    def publish(self, topic, message):
        # placeholder - integrate aiokafka or confluent-kafka
        print(f"Publish to {topic}: {message}")
    def subscribe(self, topic, handler):
        # placeholder
        pass
