import socket

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            return result == 0
    except OSError:
        return False


def run_recon(target, results):
    print(f"Running reconnaissance on {target}...")

    for port in range(1, 257):
        if scan_port(target, port):
            print(f"Port {port} is open on {target}.")
            results["ports"].append(port)

    return results
