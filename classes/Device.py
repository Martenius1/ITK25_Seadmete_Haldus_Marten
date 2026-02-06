class Device:
    def __init__(self, name, device_type, status, location):
        self.name = name
        self.type = device_type
        self.status = status
        self.location = location

    def __str__(self):
        return f"{self.name} ({self.type}) - Seisund: {self.status} Asukoht: {self.location}"
