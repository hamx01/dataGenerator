from faker import Faker
import random
import csv
from datetime import datetime

fake = Faker('pl_PL')

def generate_gabinet_hurtownia_data():
    with open('gabinet_hurtownia.csv', mode='w', newline='') as file:
        nr_gabinetu = [1,2,3,4,5,6,7,8,9,10]
        specjalizacje = [
            "Alergologia",
            "Anestezjologia i intensywna terapia",
            "Angiologia",
            "Audiologia i foniatria",
            "Balneologia i medycyna fizykalna",
            "Chirurgia dziecieca",
            "Chirurgia klatki piersiowej"
        ]

        writer = csv.writer(file)
        writer.writerow(['gabinetid', 'numergabinetu', 'specjalizacja'])
        for i in range(10):
            writer.writerow([nr_gabinetu[i], 
            str(nr_gabinetu[i]), 
            str(random.choice(specjalizacje))])

def generate_pacjent_hurtownia_data():
    with open('pacjent_hurtownia.csv', mode='w', newline='') as file:
        pacjent_id = [x for x in range(1,200+1)]
        imiona = generate_random_name(200)
        nazwiska = generate_random_surname(200)
        start_date = datetime(1970, 1, 1)
        end_date = datetime(2006, 12, 31)
        daty = generate_random_dates(200, start_date, end_date)
        numery_telefonu = generate_random_phone_number(200)
        ulice = generate_random_street(200)
        miasta = generate_random_cities(200)

        writer = csv.writer(file)
        writer.writerow(['pacjentid', 'imie', 'nazwisko', 'dataurodzenia', 'plec', 'numertelefonu', 'ulica', 'miejscowosc', 'nr_mieszkania'])
        for i in range(200):
            writer.writerow([pacjent_id[i], str(imiona[i]), str(nazwiska[i]), daty[i], 
                             random.choice(['M', 'K']), str(numery_telefonu[i]), str(ulice[i]), str(miasta[i]), str(random.randint(1, 150))])

def generate_pracownik_hurtownia_data():
    with open('pracownik_hurtownia.csv', mode='w', newline='') as file:
        pracownik_id = [x for x in range(1,30+1)]
        imiona = generate_random_name(30)
        nazwiska = generate_random_surname(30)
        stanowiska = generate_stanowisko(30)
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2023, 12, 31)
        daty = generate_random_dates(30, start_date, end_date)
        numery_telefonu = generate_random_phone_number(30)
        ulice = generate_random_street(30)
        miasta = generate_random_cities(30)

        writer = csv.writer(file)
        writer.writerow(['pracownikid', 'imie', 'nazwisko', 'stanowisko', 'datazatrudnienia', 'numertelefonu', 'ulica', 'miejscowosc', 'nr_mieszkania'])
        for i in range(30):
            writer.writerow([pracownik_id[i], str(imiona[i]), str(nazwiska[i]), str(stanowiska[i]), daty[i], 
                             numery_telefonu[i], str(ulice[i]), str(miasta[i]), str(random.randint(1, 150))])

def generate_recepta_hurtownia_data():
    with open('recepta_hurtownia.csv', mode='w', newline='') as file:
        id_recepty = [x for x in range(1,751)]
        pacjent_id = [x for x in range(1,200+1)]
        pracownik_id = [x for x in range(1,30+1)]
        start_date = datetime(2021, 6, 1)
        end_date = datetime(2023, 12, 31)
        daty_recepty = generate_random_dates(750, start_date, end_date)
        opis_leku = generate_drug(750)
        dawkowanie = generate_dosage(750)
        okreswaznosci = daty_plus_rok(daty_recepty)

        writer = csv.writer(file)
        writer.writerow(['receptaid', 'pacjentid', 'pracownikid', 'datawystawienia', 'opisleku', 'dawkowanie', 'okreswaznosci'])
        for i in range(750):
            writer.writerow([id_recepty[i], random.choice(pacjent_id), random.choice(pracownik_id), daty_recepty[i], 
                            str(opis_leku[i]),
                            str(dawkowanie[i]),
                            okreswaznosci[i]])

def generate_wizyta_hurtownia_data():
    with open('wizyta_hurtownia.csv', mode='w', newline='') as file:
        wizyta_id = [x for x in range(1,1001)]
        pacjent_id = [x for x in range(1,200+1)]
        pracownik_id = [x for x in range(1,30+1)]
        nr_gabinetu = [1,2,3,4,5,6,7,8,9,10]
        start_date = datetime(2021, 6, 1)
        end_date = datetime(2023, 12, 31)
        daty_wizyty = generate_random_dates(1000, start_date, end_date)        
        godzina_wizyty = generate_random_visit_time(1000)
        writer = csv.writer(file)
        writer.writerow(['wizytaid', 'pacjentid', 'pracownikid', 'gabinetid', 'datawizyty', 'godzinawizyty'])
        for i in range(1000):
            writer.writerow([wizyta_id[i], 
            random.choice(pacjent_id), 
            random.choice(pracownik_id), 
            random.choice(nr_gabinetu), 
            daty_wizyty[i], 
            godzina_wizyty[i]])

def generate_badania_hurtownia_data():
    with open('badania_hurtownia.csv', mode='w', newline='') as file:
        badania_id = [x for x in range(1,301)]
        pacjent_id = [x for x in range(1,200+1)]
        opisWyniku = generate_short_description(300)
        pracownik_id = [x for x in range(1,30+1)]
        start_date = datetime(2021, 6, 1)
        end_date = datetime(2023, 12, 31)
        daty_badania = generate_random_dates(300, start_date, end_date)
        rodzajBadania = generate_medical_examination_type(300)
        writer = csv.writer(file)
        writer.writerow(['badanieID', 'pacjentID', 'opisWyniku', 'pracownikID', 'dataWykonania', 'rodzajBadania'])
        for i in range(300):
            writer.writerow([badania_id[i], random.choice(pacjent_id), opisWyniku[i], random.choice(pracownik_id), daty_badania[i], rodzajBadania[i]])

def generate_siec_hurtowania_data():
    with open('siec_hurtownia.csv', mode='w', newline='') as file:
        wizyta_id = [x for x in range(1,1001)]
        pacjent_id = [x for x in range(1,200+1)]
        pracownik_id = [x for x in range(1,30+1)]
        id_recepty = [x for x in range(1,751)]
        nr_gabinetu = [1,2,3,4,5,6,7,8,9,10]
        badania_id = [x for x in range(1,301)]
        writer = csv.writer(file)
        writer.writerow(['pacjentid', 'pracownikid', 'gabinetid', 'receptaid', 'badaniaid', 'wizytaid'])
        for _ in range(1000):
            writer.writerow([random.choice(pacjent_id), random.choice(pracownik_id), random.choice(nr_gabinetu), random.choice(id_recepty), 
                             random.choice(badania_id), random.choice(wizyta_id)])




# Funkcje wspomagajace
def generate_random_dates(num_dates, start_date, end_date):
    random_dates = []
    
    for _ in range(num_dates):
        random_timestamp = random.randint(start_date.timestamp(), end_date.timestamp())
        random_date = datetime.fromtimestamp(random_timestamp).date()
        random_dates.append(random_date)
    
    return random_dates

def generate_random_phone_number(num_phone_numbers):
    phone_numbers = []
    
    phone_format = 'XXXXXXXXX'
    
    for _ in range(num_phone_numbers):
        phone_number = ''.join([random.choice('0123456789') for _ in phone_format])
        phone_numbers.append(phone_number)
    
    return phone_numbers

def generate_random_cities(num_records):
    cities = ["Warszawa", "Krakow", "Gdansk", "Poznan", "Wroclaw"]
    result = []
    for _ in range(num_records):
        result.append(random.choice(cities))

    return result

def generate_random_street(num_records):
    result = []
    for _ in range(num_records):
        result.append(replace_polish_characters(fake.street_name()))
    
    return result

def generate_random_name(num_records):
    imiona = [replace_polish_characters(fake.first_name()) for _ in range(num_records)]
    return imiona

def generate_random_surname(num_records):
    nazwiska = [replace_polish_characters(fake.last_name()) for _ in range(num_records)]
    return nazwiska

def generate_stanowisko(num_records):
    positions = [
        "Lekarz",
        "Pielegniarka",
        "Anestezjolog",
        "Chirurg",
        "Internista",
        "Ortopeda",
        "Pediatra",
        "Ginekolog",
        "Neurolog",
        "Onkolog",
        "Psychiatra",
        "Radiolog",
        "Reumatolog",
        "Farmaceuta",
        "Fizjoterapeuta",
        "Laborant",
        "Terapeuta zajeciowy",
        "Siostra oddzialowa",
        "Asystent lekarza",
        "Specjalista ds. zdrowia publicznego",
        "Kierownik kliniki",
        "Kierownik oddzialu",
        "Specjalista ds. medycyny ratunkowej"
    ]
    result = []
    for _ in range(num_records):
        item = random.choice(positions)
        result.append(item)
    return result

def generate_drug(num_records):
    prefixes = [
        "Lek jest stosowany w leczeniu ",
        "Preparat ma zastosowanie w terapii ",
        "Jest to lek wykorzystywany do zwalczania ",
        "Zastosowanie leku obejmuje leczenie ",
        "Preparat jest wskazany do terapii "
    ]
    
    middles = [
        "chorob serca",
        "problematyki ukladu pokarmowego",
        "zaburzen hormonalnych",
        "schorzen neurologicznych",
        "chorob ukladu oddechowego",
        "problematyki dermatologicznej",
        "zakazen bakteryjnych",
        "chorob nowotworowych",
        "objawow alergicznych"
    ]
    
    suffixes = [
        " oraz innych schorzen.",
        " wraz z towarzyszacymi dolegliwosciami.",
        " i powiazanych problemow zdrowotnych.",
        " oraz dolegliwosci o charakterze przewleklym.",
        " z towarzyszacymi objawami klinicznymi."
    ]
    
    result = []
    for _ in range(num_records):
        prefix = random.choice(prefixes)
        middle = random.choice(middles)
        suffix = random.choice(suffixes)
        drug_description = prefix + middle + suffix
        result.append(drug_description)
    
    return result

def generate_dosage(num_records):

    dosages = [
    "Stosowac zgodnie z zaleceniami lekarza.",
    "Dawke dostosowac do wieku i wagi pacjenta.",
    "Dorosli powinni przyjmowac w ilosci 1 tabletka raz dziennie.",
    "Nalezy unikac przedawkowania i stosowac zgodnie z instrukcja.",
    "Dawke mozna dostosowac w zaleznosci od objawow i reakcji organizmu.",
    "Przed uzyciem dokladnie zapoznaj sie z ulotka.",
    "Dawkowanie nalezy ustalic z lekarzem lub farmaceuta.",
    "Zachowac regularnosc przyjmowania leku.",
    "Nie przekraczac zalecanej dawki.",
    "Stosowac doustnie z jedzeniem lub bez, wedlug wskazan.",
    "Dawke mozna podzielic na mniejsze porcje w ciagu dnia.",
    "Zalecana dawka nie zalezy od posilkow.",
    "Unikac picia alkoholu podczas stosowania leku.",
    "Nie stosowac leku po uplywie daty waznosci.",
    "Przechowywac lek w miejscu niedostepnym dla dzieci.",
    "Nie stosowac u dzieci ponizej X lat bez konsultacji z lekarzem.",
    "Przerwac stosowanie w przypadku wystapienia dzialan niepozadanych i skonsultowac sie z lekarzem.",
    "Regularnie sprawdzac cisnienie krwi podczas stosowania leku.",
    "Nalezy pamietac o regularnych badaniach kontrolnych.",
    "W razie watpliwosci co do stosowania leku, skonsultowac sie z lekarzem."
]
    
    result = []

    for _ in range(num_records):
        dosage_description = random.choice(dosages)
        result.append(dosage_description)
    
    return result

def daty_plus_rok(daty):
    result = []
    for x in daty:
        try:
            new_date = x.replace(year=x.year + 1)
        except ValueError:
            if x.month == 2 and x.day == 29:
                new_date = x.replace(year=x.year + 1, day=28)
        result.append(new_date)
    return result

def generate_random_visit_time(num_records):
    hour = random.randint(8, 17)
    minute = random.choice([0, 15, 30, 45])
    
    result = []
    for _ in range(num_records):
        visit_time = f"{hour:02}:{minute:02}"
        result.append(visit_time)
    
    return result

def generate_short_description(num_records):
    words = [
        "normalny", "abnormalny", "wysoki", "niski", "wykryto", "brak", "obecnosc",
        "zdrowy", "choroba", "stan", "badanie", "diagnoza", "poziom", "wynik", "czynniki"
    ]
    result = []
    for _ in range(num_records):
        num_words = random.randint(3, 8)
        description_words = random.sample(words, num_words)
        short_description = ' '.join(description_words).capitalize() + '.' 
        if len(short_description) > 50:
            short_description = short_description[:50]
        result.append(short_description)
    
    return result

def generate_medical_examination_type(num_records):
    
    examination_types = [
        "badanie krwi",
        "badanie moczu",
        "USG",
        "RTG",
        "badanie EKG",
        "morfologia",
        "badanie hormonalne",
        "kolonoskopia",
        "gastroskopia",
        "tomografia komputerowa",
        "rezonans magnetyczny",
        "biopsja",
        "badanie dermatologiczne",
        "badanie okulistyczne",
        "badanie neurologiczne",
        "badanie genetyczne",
        "badanie serologiczne",
        "badanie obrazowe",
        "badanie endoskopowe",
        "badanie cytologiczne",
        "badanie mikrobiologiczne"
    ]
    
    result = []
    for _ in range(num_records):
        examination_type = random.choice(examination_types)
        result.append(examination_type)
    
    return result

def replace_polish_characters(text):
    translation_map = {
        'ł': 'l', 'ń': 'n', 'ą': 'a', 'ę': 'e', 'ć': 'c', 'ź': 'z', 'ż': 'z', 'ó': 'o',
        'Ł': 'L', 'Ń': 'N', 'Ą': 'A', 'Ę': 'E', 'Ć': 'C', 'Ź': 'Z', 'Ż': 'Z', "Ó": "O"
    }
    translated_text = ''.join(translation_map.get(char, char) for char in text)
    return translated_text


#Odpalamy funkcje do generowania plikow
generate_gabinet_hurtownia_data()
generate_pacjent_hurtownia_data()
generate_pracownik_hurtownia_data()
generate_recepta_hurtownia_data()
generate_wizyta_hurtownia_data()
generate_badania_hurtownia_data()
generate_siec_hurtowania_data()
