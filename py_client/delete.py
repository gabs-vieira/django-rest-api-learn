import requests

product_id = input("Thisi field is done\n")
endpoint = "http://localhost:8000/api/products/1/update"


try:
    product_id = int(product_id)

except:
    print("Invalid ID")
    product_id = None


if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"    

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code == 204)