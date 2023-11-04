import argparse
import zmq
from stabley_discordant_cluster import utils
import json

logger = utils.setup_logger()


def loop(host_ip: str, host_port: str):
    context = zmq.Context()
    sock = context.socket(zmq.DEALER)
    sock.connect(f"tcp://{host_ip}:{host_port}")

    print('Initialized')
    while True:
        print('Sending READY')
        sock.send(json.dumps({'type': 'READY'}).encode('utf-8'))

        work_unit = json.loads(sock.recv().decode('utf-8'))
        print('Work unit received:', work_unit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logging-level", dest="logging_level", default="INFO")
    parser.add_argument("--host-ip", dest="host_ip", type=str)
    parser.add_argument("--host-port", dest="host_port", type=str, default="5555")
    args = vars(parser.parse_args())
    logger.setLevel(args.pop("logging_level"))

    loop(**args)
