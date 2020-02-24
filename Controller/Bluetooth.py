import sys

import bluetooth

# this class handles bloothtooth connections

class AppConnector:
    def bluetooth_scanner(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices.".format(len(nearby_devices)))

        for addr, name in nearby_devices:
            print("  {} - {}".format(addr, name))

    def bluetooth_server(self):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                                    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

        print("Waiting for connection on RFCOMM channel", port)

        client_sock, client_info = server_sock.accept()
        print("Accepted connection from", client_info)

        try:
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                print("Received", data)
        except OSError:
            pass

        print("Disconnected.")

        client_sock.close()
        server_sock.close()
        print("All done.")

    def bluetooth_client(self):
        addr = None

        if len(sys.argv) < 2:
            print("No device specified. Searching all nearby bluetooth devices for "
                  "the SampleServer service...")
        else:
            addr = sys.argv[1]
            print("Searching for SampleServer on {}...".format(addr))

        # search for the SampleServer service
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        service_matches = bluetooth.find_service(uuid=uuid, address=addr)

        if len(service_matches) == 0:
            print("Couldn't find the SampleServer service.")
            sys.exit(0)

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        print("Connecting to \"{}\" on {}".format(name, host))

        # Create the client socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))

        print("Connected. Type something...")
        while True:
            data = input()
            if not data:
                break
            sock.send(data)

        sock.close()