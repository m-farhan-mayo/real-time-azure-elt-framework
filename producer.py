from azure.eventhub import EventHubProducerClient, EventData
import json
import time
import random

connection_str = (
    "Endpoint=sb://{EventHubName}.servicebus.windows.net/;"
    "SharedAccessKeyName=RootManageSharedAccessKey;"
    "SharedAccessKey={ConnectionKey};"
    "EntityPath=Name"
)
eventhub_name = "Name"

producer = EventHubProducerClient.from_connection_string(
    conn_str=connection_str,
    eventhub_name=eventhub_name
)

while True:
    message = {
        "order_id": random.randint(1000, 9999),
        "amount": random.randint(50, 500),
        "timestamp": time.time()
    }

    batch = producer.create_batch()
    batch.add(EventData(json.dumps(message)))
    producer.send_batch(batch)

    print("Sent:", message)
    time.sleep(1)
