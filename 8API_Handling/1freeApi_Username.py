import requests

def fetch_user_data():
    
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and 'data' in data:
        user_data = data['data']
        username = user_data['login']['username']
        age = user_data['dob']['age']
        return username,age
    else:
        raise Exception("Failed to fetch user data!!")

def main():
    try:
        username,age = fetch_user_data()
        print(f'Username: {username} \nAge: {age}')
    except Exception as e:
        print(str(e))
        
if __name__ == '__main__':
    main()