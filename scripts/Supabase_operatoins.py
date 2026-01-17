import os
from dotenv import load_dotenv
from supabase import create_client


class SupbaseConnection:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client = create_client(self.url, self.key)
    

    def get_client(self):
        return self.client
    def insert_cities(self, table_name,cities_dict):
        """
        Wstawia dane do dowolnej tabeli w Supabase.
        data_list: lista słowników, np. [{"col1": "val1"}, {"col2": "val2"}]
        """
        
        try:
            response = self.client.table(table_name).insert(cities_dict).execute()
            return response
        except Exception as e:
            print(f"❌ Błąd podczas insertu do {table_name}: {e}")
            raise e


def main():
    """Główna funkcja uruchomieniowa skryptu."""
    try:
        # Tworzymy instancję klasy
        db = SupbaseConnection()
        
        # Pobieramy klienta
        client = db.get_client()
        
        print("✅ Sukces! Klasa zainicjalizowana, dane z .env wczytane.")
        print(f"Połączono z adresem: {db.url}")
        
        # Tutaj możesz dopisać logikę wpisywania miast:
        # client.table('cities').insert({"name": "Warszawa"}).execute()

    except Exception as e:
        print(f"❌ Coś poszło nie tak: {e}")
# To jest kluczowy blok – zwróć uwagę na dwa podkreślniki z każdej strony
if __name__ == "__main__":
    main()







