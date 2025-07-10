import requests

def access_data_with_api(api_key):
    url = 'https://webpage-srishti.onrender.com/users_data'
    headers = {
        'X-API-Key': api_key
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                print(f"ID: {user['id']}")
                print(f"Name: {user['name']}")
                print(f"Gender: {user['gender']}")
                print(f"Email: {user['email']}")
                print(f"Password: {user['password']}")
                print()
        else:
            print("Failed to retrieve data. Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Replace 'API_KEY_VALUE' with the actual API key value you want to use
api_key_value = '1c92dfbe48e8efa60f7c8bb6ad55cb8775b267ebdbc1b4e2f5973f2d5a0062a5'
access_data_with_api(api_key_value)
