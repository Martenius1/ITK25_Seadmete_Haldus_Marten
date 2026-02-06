class Device:
    def __init__(self, name, device_type, status, location, number):
        self.name = name
        self.device_type = device_type
        self.status = status
        self.location = location
        self.number = number

    def __str__(self):
        return f"Nimi: {self.name} | Seadme tüüp: {self.device_type} | Seisund: {self.status} | Asukoht: {self.location} |Number: {self.number}"
