class Desktop:
    def __init__(self, name, device_type, status, operating_system):
        self.name = "DESKTOP-15567"
        self.device_type = "Desktop"
        self.status = "avai"
        self.operating_system = operating_system

    def __str__(self):
        return f'{self.name} {self.device_type} {self.status} {self.operating_system}'