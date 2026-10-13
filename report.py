def generate_report(results):
    print("Scan Report:")
    print("python scanner recon")
    print("=" * 40)

    print(f"target: {results['target']}")

    print("\nOpen Ports:")
    print(f"Open ports in total: {len(results['ports'])}")

    if not results["ports"]:
        print("No open ports found.")
    else:
        for port in results["ports"]:
            service = results["services"].get(port, "Unknown Service")
            print(f"Port {port:<6} {service}")

    print("\n" + "=" * 40)