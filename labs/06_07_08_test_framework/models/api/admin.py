import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        response.raise_for_status()  # raises an error if request fails
        products = response.json()  # assume API returns a list of products
        return len(products)  # return an integer, not None

    def create_product(self, product_name):
        # complete logic
        pass

    def delete_product_by_name(self, product_name):
        # complete logic
        pass
