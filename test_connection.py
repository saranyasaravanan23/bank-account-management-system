print("Test started", flush=True)

from database import create_connection

print("Calling connection function...", flush=True)

connection = create_connection()

print("Connection function returned.", flush=True)

if connection:
    connection.close()
    print("Connection test completed.")
else:
    print("Connection failed.")