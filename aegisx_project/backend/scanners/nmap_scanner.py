import nmap

class NmapScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan(self, target):
        self.scanner.scan(target, '1-1000')

        results = {}

        for host in self.scanner.all_hosts():
            results[host] = {
                "state": self.scanner[host].state(),
                "protocols": {}
            }

            for proto in self.scanner[host].all_protocols():
                ports = self.scanner[host][proto].keys()

                results[host]["protocols"][proto] = []

                for port in ports:
                    service = self.scanner[host][proto][port]

                    results[host]["protocols"][proto].append({
                        "port": port,
                        "state": service["state"],
                        "service": service["name"]
                    })

        return results