import os

def main():
    api_key = os.getenv("API_KEY")
    if api_key:
        print("API Key ditemukan, siap digunakan!")
    else:
        print("API Key tidak tersedia.")

if __name__ == "__main__":
    main()
