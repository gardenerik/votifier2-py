import hashlib
import hmac
import json
import socket
import struct
from base64 import b64encode

from .exceptions import VotifierError


class Server:
    def __init__(self, host, port, token):
        self.token = token
        self.address = (host, port)

    def send_vote(self, vote):
        with socket.create_connection(self.address, 3) as sock:
            sock.settimeout(3)

            header = sock.recv(64)
            if not header:
                raise VotifierError("Server did not send any header.")

            header = header.split()
            if len(header) != 3:
                raise VotifierError("Not a Votifier v2 server")

            payload = json.dumps(
                {
                    "username": vote.username,
                    "serviceName": vote.service_name,
                    "timestamp": vote.timestamp,
                    "address": vote.address,
                    "challenge": header[2].decode(),
                }
            )

            signature = b64encode(
                hmac.digest(self.token.encode(), payload.encode(), hashlib.sha256)
            ).decode()

            message = json.dumps({"signature": signature, "payload": payload})

            packet = struct.pack(">HH", 0x733A, len(message)) + message.encode()

            sock.send(packet)

            response = sock.recv(256)
            if not response:
                raise VotifierError("Unable to read server response")

            response = json.loads(response)
            if response["status"] != "ok":
                raise VotifierError(
                    "Server error: %s: %s" % (response["cause"], response["error"])
                )
