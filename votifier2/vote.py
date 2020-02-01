from datetime import datetime


class Vote:
    def __init__(self, service_name, username, address, timestamp=None):
        self.service_name = service_name
        self.username = username
        self.address = address
        self.timestamp = timestamp or round(datetime.utcnow().timestamp() * 1000)
