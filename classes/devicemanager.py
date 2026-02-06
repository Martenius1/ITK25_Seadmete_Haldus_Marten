from classes.device import Device
from classes.saveloading import SaveLoading


class DeviceManager:

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def display_devices(self):
        if not self.devices:
            print("Seadmeid ei ole leitud.")
            return
        for device in self.devices:
            print(device)

    def update_status(self, device_name, new_status):
        for device in self.devices:
            if device.name == device_name:
                if new_status not in ['available', 'in_use', 'broken']:
                    print("Vigane seisund!")
                    return
                device.status = new_status
                print(f"Seisund seadmele '{device_name}' on muudetud.")
                return
        print(f"Seadet nimega '{device_name}' ei leitud.")

    def delete_device(self, device_name):
        self.devices = [device for device in self.devices if device.name != device_name]
        print(f"Seade '{device_name}' on kustutatud.")

    def save_devices(self, filename, file_type):
        if file_type == 'csv':
            SaveLoading.save_to_csv(self.devices, filename)
        elif file_type == 'json':
            SaveLoading.save_to_json(self.devices, filename)
        else:
            print("Vale failitüüp. Kasutage 'csv' või 'json'.")

    def load_devices(self, filename, file_type):
        if file_type == 'csv':
            self.devices = SaveLoading.load_from_csv(filename)
        elif file_type == 'json':
            self.devices = SaveLoading.load_from_json(filename)
        else:
            print("Vale failitüüp. Kasutage 'csv' või 'json'.")
