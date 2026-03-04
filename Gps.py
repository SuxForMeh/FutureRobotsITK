from serial import Serial
from pynmeagps import NMEAReader
while True:
    with Serial('/dev/ttyAMA0', 9600, timeout=3) as stream:
        nmr = NMEAReader(stream)
        raw_data, parsed_data = nmr.read()
        if parsed_data is not None:
            try:
              print(parsed_data)
              print(f"Latitude: {parsed_data.lat}")
              print(f"Longitude: {parsed_data.lon}")
            except:
              print("no location yet...")
