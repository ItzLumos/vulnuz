import requests as req

def status_code_ident(status_code):
    if 100 <= status_code < 200:
        return f'Status code: {status_code} -- INFORMATIONAL'
    elif 200 <= status_code < 300:
        return f'Status code: {status_code} -- SUCCESSFUL'
    elif 300 <= status_code < 400:
        return f'Status code: {status_code} -- REDIRECTION'
    elif 400 <= status_code < 500:
        return f'Status code: {status_code} -- ClENT ERROR'
    elif 500 <= status_code < 600:
        return f'Status code: {status_code} -- SERVER ERROR'


def http_probe(url):
    # GET HTTP conn
    try:
        conn = req.get(url)
    except Exception as e:
        print(f"ERROR: {e}")
        return -1

    print("Connection established with sucess!")
    # Print status code
    print(status_code_ident(conn.status_code))
    # Print raw headers
    print(f"Raw Headers: {conn.headers}")

    # The main differnce between .content and .text, is mainly beacuse content is returned
    # in bytes, and text is returned in string, so because we want text, for now, we'll
    # use .text, considering .content still has useful info like binary

# YK what this does
if __name__ == "__main__":
    url = input("URL - ")
    http_probe(url)