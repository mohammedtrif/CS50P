import sys
import requests
try :
    if len(sys.argv) == 1 :
        sys.exit("Missing command-line argument")
    if len(sys.argv) == 2 :
        x = sys.argv[1]
        x = float(x)
    if len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
except ValueError :
    sys.exit("Command-line argument is not a number")

try:
    resp = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    result = resp.json()
    data = result["data"]["priceUsd"]
    data = float(data)

    result1 = x * data
    print(f"${result1:,.4f}")
except requests.RequestException :
    sys.exit("Request failed")