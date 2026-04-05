from core.http_prober import http_probe
from core.header_analyzer import analyze_headers

def main():
    while True:
        cmd = input("vulnuz> ")
        args = cmd.split()

        if not args:
            continue

        if args[0] == "exit":
            break
    
        if args[0] == "analyze-headers":
            if len(args) < 2:
                print("Usage: analyze-headers <url>")
                continue

            headers = http_probe(args[1])

            if headers == -1:
                print("ERROR: Could not resolve/connect to the given URL")
                continue

            findings = analyze_headers(headers)

            for finding in findings:
                print(finding)
        
        else:
            print(f'ERROR: "{cmd}" is not a command/external module')
            continue


if __name__ == "__main__":
    main()