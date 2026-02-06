from classes.device import Device
from classes.devicemanager import DeviceManager

def main():
    device_manager = DeviceManager()

    while True:
        print("Vali tegevus:")
        print("1. Lisa seade")
        print("2. Kuva kõik seadmed")
        print("3. Muuda seadme seisundit")
        print("4. Kustuta seade")
        print("5. Salvesta seadmed")
        print("6. Laadi seadmed")
        print("7. Välju")

        choice = input("Sisesta oma valik (1-7): ")

        if choice == '1':
            name = input("Sisesta seadme nimi: ")
            device_type = input("Sisesta seadme tüüp: ")
            status = input("Sisesta seadme seisund (available, in_use, broken): ")
            location = input("Sisesta seadme asukoht: ")
            number = input("Sisesta seadme number: ")

            device = Device(name, device_type, status, location, number)
            device_manager.add_device(device)

        elif choice == '2':
            device_manager.display_devices()

        elif choice == '3':
            device_name = input("Sisesta seadme nimi, mille seisundit soovid muuta: ")
            new_status = input("Sisesta uus seisund (available, in_use, broken): ")
            device_manager.update_status(device_name, new_status)

        elif choice == '4':
            device_name = input("Sisesta seadme nimi, mille soovid kustutada: ")
            device_manager.delete_device(device_name)

        elif choice == '5':
            filename = input("Sisesta faili nimi (nt seadmed): ")

            file_type = input("Sisesta failitüüp (csv või json): ").lower()

            if file_type not in ['csv', 'json']:
                print("Vigane failitüüp! Kasutatakse ainult 'csv' või 'json'.")
                continue

            filename = f"{filename}.{file_type}"

            device_manager.save_devices(filename, file_type)

        elif choice == '6':
            filename = input("Sisesta faili nimi, mille soovid laadida (nt seadmed): ")
            file_type = input("Sisesta failitüüp (csv või json): ").lower()

            if file_type not in ['csv', 'json']:
                print("Vigane failitüüp! Kasutatakse ainult 'csv' või 'json'.")
                continue

            filename = f"{filename}.{file_type}"

            device_manager.load_devices(filename, file_type)

        elif choice == '7':
            print("Programm on lõpetatud.")
            break

        else:
            print("Vigane valik! Palun sisesta number 1 kuni 7.")

if __name__ == "__main__":
    main()

