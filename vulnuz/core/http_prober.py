import requests as req

# Function to identify status codes
def status_code_ident(status_code):
    if 100 <= status_code < 200:
        print(f'Status code: {status_code} -- INFORMATIONAL')
        return False
    elif 200 <= status_code < 300:
         print(f'Status code: {status_code} -- SUCCESSFUL')
         return True
    elif 300 <= status_code < 400:
         print(f'Status code: {status_code} -- REDIRECTION')
         return False
    elif 400 <= status_code < 500:
         print(f'Status code: {status_code} -- CLIENT ERROR')
         return False
    elif 500 <= status_code < 600:
         print(f'Status code: {status_code} -- SERVER ERROR')
         return False


def http_probe(url):
    # GET HTTP conn
    try:
        conn = req.get(url)
    except Exception as e:
        print(f"ERROR: {e}")
        return -1

    print("Connection established with success!")
    # Print status code
    can_continue = status_code_ident(conn.status_code)
    if not can_continue:
        return -1
    # Print raw headers
    print(f"Raw Headers: {conn.headers}")

    # The main differnce between .content and .text, is mainly beacuse content is returned
    # in bytes, and text is returned in string, so because we want text, for now, we'll
    # use .text, considering .content still has useful info like binary

# for testing reasons:
if __name__ == "__main__":
     url = input("URL - ")
     http_probe(url)