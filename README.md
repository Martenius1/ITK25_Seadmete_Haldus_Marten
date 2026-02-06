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

<img width="212" height="197" alt="Screenshot 2026-02-06 131325" src="https://github.com/user-attachments/assets/c6fc144c-9aa2-432c-b219-5367311c3fca" />

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

# Kuidas kasutada?
Kloonige remo
```
git clone https://github.com/Martenius1/ITK25_Seadmete_Haldus_Marten.git
cd REPO
```
Avage repos terminal

![ezgif-181ee05f5e044a82](https://github.com/user-attachments/assets/24538071-fd75-4083-98b6-945506811b44)

### Järgmisena kirjutage terminali *py main.py* ja programm hakkab tööle

# Kuidas valida kas CSV või JSON salvestus? 
Selleks on vaja programm käivitada py main.py käsuga ja navigeerida valikule 5. ehk salvesta seadmed. Selle valimisel tuleb kirjutada faili nimi ja valida kas salvestada CSV või JSON formaadis.









    
