import programoption

class Program:

    def __init__(self):

        self.main_menu = programoption.MenuOption("Huvudmeny", [
            ("Gå till undermeny 1", self.undermeny1),
            ("Gå till undermeny 2", self.undermeny2),
            ("Via information", self.show_info),
            ("Avsluta", self.exit_program)
            
        ])

    def start(self):
        """Startar programmet och visar huvudmenyn."""
        self.main_menu.show()
    
    def undermeny1(self):
        """Visar undermeny 1."""
        undermeny1 =  programoption.MenuOption("Undermeny 1", [
            ("Alternativ 1 i undermeny 1", lambda: print("Du valde alternativ 1 i undermeny 1")),
            ("Alternativ 2 i undermeny 1", lambda: print("Du valde alternativ 2 i undermeny 1")),
            ("Tillbaka till huvudmenyn", lambda: self.main_menu.show())
        ])
        undermeny1.show()

    def undermeny2(self):
        """Visar undermeny 2."""
        undermeny2 = programoption.MenuOption("Undermeny 2", [
            ("Alternativ 1 i undermeny 2", lambda: print("Du valde alternativ 1 i undermeny 2")),
            ("Alternativ 2 i undermeny 2", lambda: print("Du valde alternativ 2 i undermeny 2")),
            ("Tillbaka till huvudmenyn", lambda: self.main_menu.show())
        ])
        undermeny2.show()

    def show_info(self):
        """Visar information om programmet."""
        print("\nDetta är ett exempelprogram med huvudmeny och undermenyer.")
        print("Här kan du välja olika alternativ för att se hur menyer och val fungerar.")
        print("Programmet använder objektorientering för att organisera koden.")

    def exit_program(self):
        print("Avslutar programmet...")
        exit()
