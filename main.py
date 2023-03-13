import csv
import datetime 

pizza_size = {
    1: "Klasik",
    2: "Margarita",
    3: "Türk Pizza",
    4: "Sade Pizza"
}


size_cost = {
    "Klasik": 10,
    "Margarita": 12,
    "Türk Pizza": 14,
    "Sade Pizza": 16
}

class Pizza_system():

    def __init__(self, size):
        self.size = size

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size()
    
    def get_description(self):
        print("B Pizza'ya Hoşgeldiniz!")


    def get_cost(self):
        return size_cost[self.size]

class Menu(Pizza_system):
    
    order_menu = open("Menu.txt")

class Ek_siparis():

    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotal(self):
        toplam = 0
        for pizza in self.pizzas:
            toplam += pizza.get_cost()
        return toplam
    
ek_siparis = Ek_siparis()

order_menu = open("Menu.txt")
print(order_menu.read())
    
def main():
     

    while True:
        try:
            
            response = input("Seçiminizi Giriniz:")

            if response == 'e':
                break

            size_wanted = int(response)

            size_wanted = pizza_size[size_wanted]
            

            print(f"Pizza: {size_wanted}")
            ek_siparis.addPizza(Pizza_system(size_wanted))
        except:
            print("Geçersiz seçim yaptınız. Lütfen 1 ve 4 arasında bir sayı giriniz.")
main()

print("Şu anki toplam tutar: ", "$" + str(ek_siparis.getTotal()))


ekstra_secimi = {
                    1: 'Zeytin', 
                    2: 'Mantarlar', 
                    3: 'Keçi Peyniri', 
                    4: 'Et', 
                    5: 'Soğan', 
                    6: 'Mısır', 
                    7: 'Sucuk'
                    }

ekstra_cost = {
                        'Zeytin': 2, 
                        'Mantarlar': 3, 
                        'Keçi Peyniri': 5, 
                        'Et': 5, 
                        'Soğan': 1, 
                        'Mısır': 2, 
                        'Sucuk': 2
                        }

class ekstra_secenekler():
    """ Have customer pick toppings for pizza"""
    
    def __init__(self, ekstrasay):
        self.ekstrasay = ekstrasay

    def set_toppings(self, ekstrasay):
        self.ekstrasay = ekstrasay

    def get_toppings(self):
        return ekstra_cost[self.ekstrasay]


class ekstra_ucretler():

    def __init__(self):
        self.malzeme = []

    def addTopping(self, toppings): 
        self.malzeme.append(toppings)

    def toppingTotal(self):
        get_total = 0
        for toppings in self.malzeme:
            get_total += toppings.get_toppings()
        return get_total

# Strat processing the order
topping_order = ekstra_ucretler()

order_menuekstra = open("Menuekstra.txt")
print(order_menuekstra.read())

def runTopping():
   

    while True:
        try: 
            response = input('-')
            if response == 'f':
                break
            toppings_wanted = int(response)

            toppings_wanted = ekstra_secimi[toppings_wanted]

            print(f"Topping: {toppings_wanted}")
            topping_order.addTopping(ekstra_secenekler(toppings_wanted))
        except:
            print("Geçersiz seçim yaptınız. Lütfen 1 ve 7 arasında bir sayı giriniz.")

runTopping()

sub_size = int(ek_siparis.getTotal())
sub_toppings =  int(topping_order.toppingTotal())
final_total = sub_size + sub_toppings

print(f" \nÖdenecek Tutar ${final_total}\nÖdeme İşlemine Geçiliyor..")


 
def odeme_main():

    
    while True:
        
        ad = input("Adınızı Giriniz: ")
        soyad = input("Soyadınızı Giriniz: ")
        tc = input("T.C Kimlik Numaranızı Giriniz: ")
        kartno = input("Kredi Kartı Numaranızı Giriniz: ")
        sifre = input("Kredi Kart Şifrenizi Giriniz: ")
    
        with open("Ödeme.csv" , "a+") as dosya:
            dosya.write("{}-{}-{}-{}-{}\n".format(ad , soyad , tc , kartno , sifre ))
        
        if True:
            print("Ödeme İşleminiz Gerçekleştirilmiştir.")
        break
odeme_main()

