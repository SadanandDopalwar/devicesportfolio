# from opcua import Client

# # OPC UA Server URL (Replace with your PLC's IP)
# OPC_UA_SERVER = "opc.tcp://192.168.6.150:4840"

# def connect_opcua():
#     """Connect to OPC UA Server and return the client instance."""
#     client = Client(OPC_UA_SERVER)
#     try:
#         client.connect()
#         print("Connected to OPC UA Server")
#         return client
#     except Exception as e:
#         print(f"Connection error: {e}")
#         return None

# def browse_node(node, level=0):
#     """Recursively browse and print all child nodes."""
#     try:
#         children = node.get_children()
#         for child in children:
#             browse_name = child.get_browse_name()
#             node_id = child.nodeid
#             print(f"{'  ' * level}- Tag Name: {browse_name}, Node ID: {node_id}")
#             # Recursively browse child nodes
#             browse_node(child, level + 1)
#     except Exception as e:
#         print(f"Error browsing nodes: {e}")

# def list_all_tags(client):
#     """List all available tags under a specific node."""
#     try:
#         root_node = client.get_objects_node()  # Root of OPC UA Objects
#         print("\nBrowsing OPC UA Nodes...\n")
        
#         # Locate the "ServerInterfaces" node
#         target_node = None
#         for node in root_node.get_children():
#             browse_name = node.get_browse_name().Name
#             if browse_name == "ServerInterfaces":
#                 target_node = node
#                 break

#         if target_node:
#             print(f"Found 'ServerInterfaces' Node: {target_node.nodeid}")
#             browse_node(target_node)
#         else:
#             print("ServerInterfaces node not found!")

#     except Exception as e:
#         print(f"Error browsing nodes: {e}")

# def main():
#     """Main function to list all available OPC UA tags."""
#     client = connect_opcua()
#     if not client:
#         return

#     try:
#         list_all_tags(client)
#     except KeyboardInterrupt:
#         print("\nStopping OPC UA connection...")
#     finally:
#         client.disconnect()
#         print("Disconnected from OPC UA Server")

# if __name__ == "__main__":
#     main()


from opcua import Client, ua
import time
import datetime
OPC_UA_SERVER = "opc.tcp://192.168.6.150:4840"

BARCODE_NODE_ID = "ns=4;i=22"
NEW_BARCODE_AVAILABLE_NODE_ID = "ns=5;i=13"
SHIPMENT_BARCODE_VALIDATION_NODE_ID = "ns=5;i=3"

def connect_opcua():
    client = Client(OPC_UA_SERVER)
    try:
        client.connect()
        client.session_timeout = 3600000
        print("✅ Connected to OPC UA Server")
        return client
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None

def check_access_level(client, node_id):
    try:
        node = client.get_node(node_id)
        access_level = int(node.get_attribute(ua.AttributeIds.AccessLevel).Value.Value)
        print(f"🔍 Access Level of {node_id}: {bin(access_level)}")
        return access_level
    except Exception as e:
        print(f"❌ Error checking AccessLevel for {node_id}: {e}")
        return None

def read_barcode_data(client):
    try:
        node = client.get_node(BARCODE_NODE_ID)
        barcode_value = node.get_value()
        print(f"📌 Barcode Data: {barcode_value}")
        return barcode_value
    except Exception as e:
        print(f"❌ Error reading Barcode Data: {e}")
        return None
def write_new_barcode_available(client):
    """Set 'New Barcode Available' to True."""
    try:
        node = client.get_node(NEW_BARCODE_AVAILABLE_NODE_ID)
        node.set_value(ua.Variant(True, ua.VariantType.Boolean))  # ✅ Ensure correct type
        print("✅ 'New Barcode Available' set to True")
    except Exception as e:
        print(f"❌ Error setting 'New Barcode Available': {e}")

def write_shipment_barcode_validation(client):
    """Set 'Shipment Barcode Validation' to 1."""
    try:
        node = client.get_node(SHIPMENT_BARCODE_VALIDATION_NODE_ID)
        node.set_value(ua.Variant(1, ua.VariantType.Int16))  # ✅ Ensure correct type
        print("✅ 'Shipment Barcode Validation' set to 1")
    except Exception as e:
        print(f"❌ Error setting 'Shipment Barcode Validation': {e}")



def main():
    client = connect_opcua()
    if not client:
        return
    
    try:
        check_access_level(client, NEW_BARCODE_AVAILABLE_NODE_ID)
        check_access_level(client, SHIPMENT_BARCODE_VALIDATION_NODE_ID)

        barcode_value = read_barcode_data(client)
        if barcode_value:
            write_new_barcode_available(client)
            time.sleep(0.5)
            write_shipment_barcode_validation(client)
    finally:
        client.disconnect()
        print("🔌 Disconnected from OPC UA Server")

if __name__ == "__main__":
    main()
