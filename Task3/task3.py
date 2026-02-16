import json

def process_server_data(json_string):
    
    try:
        server_data = json.loads(json_string)
        print(server_data)
        
        for server in server_data['servers']:
            print(f"Server Status: {server['status']}")

    except json.JSONDecodeError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    #example usage
    mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'
    process_server_data(mock_api)
