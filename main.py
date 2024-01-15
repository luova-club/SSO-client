import requests

class SSOClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        endpoint = f"{self.base_url}/login"
        data = {"username": username, "password": password}
        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            self.token = response.json()["token"]
            return True
        else:
            print(f"Login failed: {response.json().get('error')}")
            return False

    def logout(self):
        endpoint = f"{self.base_url}/logout"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.token = None
            return True
        else:
            print(f"Logout failed: {response.json().get('error')}")
            return False

    def verify_token(self):
        endpoint = f"{self.base_url}/verify-token"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(endpoint, headers=headers)

        if response.status_code == 200:
            print("Token verification successful")
            return True
        else:
            print(f"Token verification failed: {response.json().get('error')}")
            return False

    def get_user_data(self):
        endpoint = f"{self.base_url}/"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            print(response.json()["message"])
        else:
            print(f"Failed to retrieve user data: {response.json().get('error')}")

# Example usage
client = SSOClient("http://localhost:5000")

# Attempt to login
if client.login("example_user", "example_password"):
    # Successfully logged in, perform other actions here
    client.get_user_data()

    # Verify token
    client.verify_token()

    # Logout
    client.logout()
