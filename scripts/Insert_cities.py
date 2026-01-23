from Supabase_operatoins import SupbaseConnection

capitals_data = {
    "Warszawa": (52.2297, 21.0122, "mazowieckie"),
    "Kraków": (50.0647, 19.9450, "małopolskie"),
    "Wrocław": (51.1079, 17.0385, "dolnośląskie"),
    "Łódź": (51.7592, 19.4560, "łódzkie"),
    "Poznań": (52.4064, 16.9252, "wielkopolskie"),
    "Gdańsk": (54.3520, 18.6466, "pomorskie"),
    "Szczecin": (53.4285, 14.5528, "zachodniopomorskie"),
    "Bydgoszcz": (53.1235, 18.0084, "kujawsko-pomorskie"),
    "Toruń": (53.0138, 18.5984, "kujawsko-pomorskie"),
    "Lublin": (51.2465, 22.5666, "lubelskie"),
    "Katowice": (50.2649, 19.0238, "śląskie"),
    "Białystok": (53.1325, 23.1688, "podlaskie"),
    "Rzeszów": (50.0415, 21.9991, "podkarpackie"),
    "Olsztyn": (53.7784, 20.4801, "warmińsko-mazurskie"),
    "Kielce": (50.8703, 20.6275, "świętokrzyskie"),
    "Opole": (50.6664, 17.9231, "opolskie"),
    "Gorzów Wielkopolski": (52.7311, 15.2369, "lubuskie"),
    "Zielona Góra": (51.9355, 15.5062, "lubuskie")
}
data_to_insert = [
    {"City_name": name, "Lon": coords[1], "Lat": coords[0], "Voivodship": coords[2]}
    for name, coords in capitals_data.items()]



def insert_cities(table_name, cities_dict):
    db = SupbaseConnection()
    try:
        response = db.insert_cities(table_name, cities_dict)
        print("✅ Wstawiono dane:", response)
    except Exception as e:
        print(f"❌ Błąd podczas wstawiania: {e}")

insert_cities("Cities", data_to_insert)