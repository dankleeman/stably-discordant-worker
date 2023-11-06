import argparse
import base64
import json
import socket

import zmq

from stably_discordant_worker import utils  # type: ignore
from stably_discordant_worker.diffuser import Diffuser  # type: ignore

logger = utils.setup_logger()


def loop(host_ip: str, host_port: str):
    logger.info("Initializing ZeroMQ objects")
    context = zmq.Context()
    sock = context.socket(zmq.DEALER)
    sock.connect(f"tcp://{host_ip}:{host_port}")
    hostname = socket.gethostname()

    logger.info("Initializing Diffuser")
    diffuser = Diffuser()

    while True:
        logger.info("Sending READY to host.")
        sock.send(json.dumps({"type": "READY", "hostname": hostname}).encode("utf-8"))

        work_unit = json.loads(sock.recv().decode("utf-8"))
        logger.info("Work unit received: %s", work_unit)

        id_num = work_unit.pop("id_num")
        file_name = diffuser.make_image(**work_unit)
        with open(file_name, "rb") as image_file:
            image_data = image_file.read()

        image_data_base64 = base64.b64encode(image_data).decode("utf-8")

        message = {
            "type": "OUTPUT",
            "image_data": image_data_base64,
            "id_num": id_num,
            "hostname": hostname,
        }
        payload = json.dumps(message).encode("utf-8")
        sock.send(payload)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logging-level", dest="logging_level", default="INFO")
    parser.add_argument("--host-ip", dest="host_ip", type=str, required=True)
    parser.add_argument("--host-port", dest="host_port", type=str, default="5555")
    args = vars(parser.parse_args())
    # logger.setLevel(args.pop("logging_level"))
    _ = args.pop("logging_level")
    loop(**args)
