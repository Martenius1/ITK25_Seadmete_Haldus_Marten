import csv
import json
import os
from classes.device import Device

class SaveLoading:
    @staticmethod
    def ensure_data_directory():
        if not os.path.exists('data'):
            os.makedirs('data')

    @staticmethod
    def save_to_csv(devices, filename):
        SaveLoading.ensure_data_directory()
        file_path = os.path.join('data', filename)

        # Open the file in append ('a') or write ('w') mode
        file_mode = 'a' if os.path.exists(file_path) else 'w'

        with open(file_path, file_mode, newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')

            # Fetch field names dynamically from the Device class attributes
            headers = list(vars(devices[0]).keys())  # Get the field names of the first device

            # Write headers only if file is new or empty
            if file_mode == 'w' and os.path.getsize(file_path) == 0:
                writer.writerow(headers)

            # Write device data, values corresponding to the headers
            for device in devices:
                writer.writerow([getattr(device, field) for field in headers])

        print(f"Seadmed on salvestatud failisse {file_path}.")

    @staticmethod
    def save_to_json(devices, filename):
        SaveLoading.ensure_data_directory()
        file_path = os.path.join('data', filename)

        # Check if file exists to load existing data
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Add all devices to the existing data list
        devices_data = existing_data + [vars(device) for device in devices]

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(devices_data, file, ensure_ascii=False, indent=4)

        print(f"Seadmed on salvestatud failisse {file_path}.")

    @staticmethod
    def load_from_csv(filename):
        devices = []
        file_path = os.path.join('data', filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                headers = next(reader)  # Read the header row
                for row in reader:
                    device_data = dict(zip(headers, row))  # Combine headers and row
                    devices.append(Device(**device_data))  # Create Device object with the data
            print(f"Seadmed on laaditud failist {file_path}.")
        except FileNotFoundError:
            print(f"Faili {file_path} ei leitud.")
        return devices

    @staticmethod
    def load_from_json(filename):
        devices = []
        file_path = os.path.join('data', filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                devices_data = json.load(file)
                for device_data in devices_data:
                    devices.append(Device(**device_data))  # Create Device object with the data
            print(f"Seadmed on laaditud failist {file_path}.")
        except FileNotFoundError:
            print(f"Faili {file_path} ei leitud.")
        return devices
