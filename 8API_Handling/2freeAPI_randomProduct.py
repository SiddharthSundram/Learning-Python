import requests
import random

def fetchMultipleProducts(api_url, count):
    """
    Fetches multiple products by calling the API multiple times.
    """
    products = []
    try:
        for _ in range(count):  # Make multiple API calls
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if data.get('success') and 'data' in data:
                products.append(data['data'])  # Add the single product to the list
            else:
                print("Warning: API response invalid!")
        return products
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    except ValueError:
        raise Exception("Failed to decode JSON response!")

def selectRandomProduct(products):
    """
    Selects a random product from the list of products.
    """
    if not products:
        raise Exception("Product list is empty!")
    
    product = random.choice(products)  # Picks a random product
    print("Selected product:", product)  # Debugging output
    
    # Retrieve product details with default values
    brand = product.get('brand', 'Unknown')
    price = product.get('price', 'Unknown')

    return brand, price

def main():
    api_url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    try:
        # Fetch multiple products
        products = fetchMultipleProducts(api_url, count=10)  # Fetch 10 random products
        brand, price = selectRandomProduct(products)
        print(f'Brand: {brand} \nPrice: {price}')
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
