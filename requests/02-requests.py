import requests

def main():
    payload = {"base": "USD", "symbols": "GBP"}
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP",
                            params=payload)

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        print("'Content-Type':", response.headers['Content-Type'])
        raise Exception("Error!")

    data = response.json()
    print("JSON data: ", data)

if __name__ == "__main__":
    main()
