import socket

def urls_to_ips_from_file(input_file, output_file):
    try:
        # Read URLs from the input file
        with open(input_file, 'r') as file:
            urls = file.read().splitlines()
        
        ips = []
        for url in urls:
            try:
                # Convert each URL to an IP address
                ip = socket.gethostbyname(url)
                ips.append(ip)
            except socket.gaierror:
                print(f"Error: Unable to resolve {url}")
        
        # Write IPs to the output file
        with open(output_file, 'w') as file:
            for ip in ips:
                file.write(ip + '\n')
        
        print(f"IPs have been saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")

# Example usage
if __name__ == "__main__":
    input_file = input("What is the list of URLS you want to conver to to ipv4?: ") # Input file containing URLs (one per line)
    output_file = "iplist" # Output file for IPs
    urls_to_ips_from_file(input_file, output_file)
