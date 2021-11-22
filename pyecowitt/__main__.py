import pyecowitt as ecowitt
import asyncio
import sys


def usage():
    print("Usage: {0} port".format(sys.argv[0]))

async def my_handler(data):
    print("In my handler")
    print(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(1)

    print("Firing up webserver to listen on port {0}".format(sys.argv[1]))
    ws = ecowitt.EcoWittListener(port=sys.argv[1])

    ws.register_listener(my_handler)
    try:
        asyncio.run(ws.start())
    except Exception as e:
        print(str(e))
    print("Exiting")
    exit(0)
