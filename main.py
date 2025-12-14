import requests
import pandas as pd
import numpy as np

def main():
    print("Hello from Python inside Jenkins!")

    # Example: simple numpy calculation
    arr = np.array([1, 2, 3, 4, 5])
    print("Array mean:", np.mean(arr))

    # Example: fetch a webpage
    response = requests.get("https://httpbin.org/get")
    print("HTTP GET status:", response.status_code)

if __name__ == "__main__":
    main()