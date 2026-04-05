import requests as req

def analyze_headers(url):
   findings = []

   # HTTP GET request
   try:
      conn = req.get(url)
   except Exception as e:
      print(f"ERROR: {e}")

    print("Connection done with sucess!")
    

if __name__ == "__main__":
   url = input("URL - ")
   analyze_headers(url)
