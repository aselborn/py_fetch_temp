"""Program options v0.1"""
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class MenuOption:

    def __init__(self, title, options):
        self.title = title
        self.options = options

    
    def show(self):
         while True:
            print(f"\n--- {self.title} ---")
            for i, (text, _) in enumerate(self.options, 1):
                print(f"{i}. {text}")
            
            val = input("Välj ett alternativ: ")
            
            # Kontrollera om valet är ett giltigt alternativ
            if val.isdigit() and 1 <= int(val) <= len(self.options):
                index = int(val) - 1
                self.options[index][1]()  # Kör den valda funktionen
            else:
                print("Ogiltigt val, försök igen.")


    