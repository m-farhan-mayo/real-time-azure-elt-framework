from azure.eventhub import EventHubConsumerClient
import json
import pyodbc

# 1️⃣ Azure SQL Connection String
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=lsdeh-server.database.windows.net;'
    'DATABASE=OrdersDB;'
    'UID=user;'
    'PWD=Password;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=120;'
)
cursor = conn.cursor()

# 2️⃣ Event Hub Connection
connection_str = "Endpoint=sb://{eventhubname}.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey={ConnectionKey};EntityPath=adls4lsd"
consumer_group = "$Default"
eventhub_name = "adls4lsd"

client = EventHubConsumerClient.from_connection_string(
    connection_str,
    consumer_group=consumer_group,
    eventhub_name=eventhub_name
)

# 3️⃣ Event processing function
def on_event(partition_context, event):
    data = json.loads(event.body_as_str())
    print("Received:", data)

    # Insert into SQL
    cursor.execute("""
        INSERT INTO Orders (order_id, amount, event_time)
        VALUES (?, ?, ?)
    """, data["order_id"], data["amount"], data["timestamp"])
    conn.commit()

    partition_context.update_checkpoint(event)

# 4️⃣ Start receiving
with client:
    client.receive(
    on_event=on_event,
    starting_position="-1",
    max_batch_size=50,      
    max_wait_time=5         
    )
