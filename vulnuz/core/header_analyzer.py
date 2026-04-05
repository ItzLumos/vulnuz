import requests as req

def analyze_headers(headers):
    findings = []

    print("Analyzing headers...")

    if 'X-Frame-Options' not in headers:
        findings.append("VULNERABILITY: X-Frame-Options not found in headers (clickjacking risk)")
    if 'Content-Security-Policy' not in headers:
        findings.append("VULNERABILITY: Content-Security-Policy not found in headers (XSS risk)")
    if 'Strict-Transport-Security' not in headers:
        findings.append("VULNERABILITY: Strict-Transport-Security not found in headers (downgrade attack risk)")
    if 'X-Content-Type-Options' not in headers:
        findings.append("VULNERABILITY: X-Content-Type-Options not found in headers (MIME sniffing risk)")
    if 'Set-Cookie' not in headers:
        findings.append("VULNERABILITY: Set-Cookie not found in headers (cookie theft risk)")
    if 'Server' in headers:
        findings.append("VULNERABILITY: Server found in headers (information leak risk)")

   
    if findings == []:
        return "NO VULNERABILITY FOUND IN HEADERS: your site is safe ^-^"
    
    return findings