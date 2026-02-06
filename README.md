# ITK25_Seadmete_Haldus_Marten

# Features 
1. Lisa seade
2. Kuva kõik seadmed
3. Muuda seadme seisundit
4. Kustuta seade
5. Salvesta seadmed
6. Laadi seadmed

Antud programmiga saaab hallata erinevaid seadmeid, näiteks printereid ja monitore. 
Seadmeid saab lisada läbi CLI ja salvestada need CSV või JSON faili. 
Seadme olekut saab muuta läbi CLI interaktiivse menüü

# Dünaamilisus 
Lisavälja lisamine ei ole raske.
Välja saab lisada antud näite põhjal (kasutame selleks näiteks responsible_person):
### 1. Navigeeri kausta classes ja ava fail devices 
### 2. Lisa vajalik väli device file:
```
_init__(self, name, device_type, status, location, number, **responsible_person**)
    self.name = name,
    ...
    ...
    self.responsible_person = responsible_person

    def __str__(self):
        return f"Nimi: {self.name} | Seadme tüüp: {self.device_type} | Seisund: {self.status} | Asukoht: {self.location} |Number: {self.number} **| Vastutaja: {self.responsible_person}**"
```
### 3. Muuda *main.py* sisu
```
if choice == '1':
            name = input("Sisesta seadme nimi: ")
            device_type = input("Sisesta seadme tüüp: ")
            status = input("Sisesta seadme seisund (available, in_use, broken): ")
            location = input("Sisesta seadme asukoht: ")
            number = input("Sisesta seadme number: ")
            **responsible_person = input("Kes on vastutav?")** 

            device = Device(name, device_type, status, location, number, **responsible_person**)
            device_manager.add_device(device)
```
### 4. Ja ongi valmis!
<img width="212" height="197" alt="image" src="https://github.com/user-attachments/assets/97919643-7af3-465b-ad12-5e3a14533185" />






    
