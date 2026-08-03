import socket

print("🔍 Simple Vulnerability (Port) Scanner")
target = input("Enter target IP or domain: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

print(f"\nScanning target: {target}\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"✅ Port {port} is OPEN (Potential Risk)")
    else:
        print(f"❌ Port {port} is CLOSED")
    
    sock.close()

print("\n🔎 Scan Completed!")