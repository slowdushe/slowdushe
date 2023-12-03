import csv
import httpx

def save_user_data(users):
    for user in users:
        username = user['username']
        user_data = {
            'id': user['id'],
            'username': username,
            'email': user['email'],
            'phone': user['phone'],
            'website': user['website'],
            'company_name': user['company']['name']
        }
        with open(f'users/{username}.csv', 'w', newline='') as csv_file:
            fieldnames = ['id', 'username', 'email', 'phone', 'website', 'company_name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(user_data)

response = httpx.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
save_user_data(users)
