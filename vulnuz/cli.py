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
            if len(args) < 3 or "-u" not in args:
                print("Usage: analyze-headers -u <url> -f <file-path>")
                continue

            url_index = args.index("-u") + 1
            url = args[url_index]

            headers = http_probe(url)

            if headers == -1:
                print("ERROR: Could not resolve/connect to the given URL")
                continue

            findings = analyze_headers(headers)

            if "-f" in args:
                filepath_index = args.index("-f") + 1
                filepath = args[filepath_index]

                with open(filepath, "w") as f:
                    for finding in findings:
                        f.write(f"{finding}\n")

                    f.close()

                print(f"Header analysis registered at: '{filepath}'")

                continue

            for finding in findings:
                print(finding)
        
        elif args[0] == "http-probe":
            if len(args) < 3 or "-u" not in args:
                print("Usage: http-probe -u <url> -f <file-path>")
                continue

            url_index = args.index("-u") + 1
            url = args[url_index]

            headers = http_probe(url)

            if headers == -1:
                print("ERROR: Could not resolve/connect to the given URL")
                continue

            if "-f" in args:
                filepath_index = args.index("-f") + 1
                filepath = args[filepath_index]

                with open(filepath, "w") as f:
                    f.write(str(headers))

                    f.close()
                
                print(f"Headers registered at {filepath}")
                
                continue

            print(headers)

        else:
            print(f'ERROR: "{cmd}" is not a command/external module')
            continue


if __name__ == "__main__":
    banner = """
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗██╗   ██╗███████╗
██║   ██║██║   ██║██║     ████╗  ██║██║   ██║╚══███╔╝
██║   ██║██║   ██║██║     ██╔██╗ ██║██║   ██║  ███╔╝ 
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██║   ██║ ███╔╝  
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║╚██████╔╝███████╗
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
made by: ItzLumos (GitHub)
"""
    print(banner)
    main()