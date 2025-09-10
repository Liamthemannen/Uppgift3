import csv
import os
import locale




def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []           #lista
    
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    
    return products
   
def load_specific_product(asked_id, products):
    for product in products:
        if product['id'] == asked_id - 1:
            return product
    else:
        print("Produkten hittades inte.")

def remove_specific_product(remove_id, products):
    for i, product in enumerate(products):
        if product["id"] == remove_id - 1:
            removed = products.pop(i)
            return removed

def add_product(new_id, new_name, new_desc, new_price, new_quantity, products):
    products.append(
        {
            "id": new_id,
            "name": new_name,
            "desc": new_desc,
            "price": new_price,
            "quantity": new_quantity
        }
    )
    return products
#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

os.system('cls')

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('C:\\Users\\liam.brundinjohanss\\Documents\\PRR2\\Uppgift3\\Uppgift3\\db_products.csv')
asked_id = int(input("Vilket id vill du söka på?"))
prod = load_specific_product(asked_id, products)
print(prod)

asked_id = int(input("Vilket id vill du ta bort?"))
removed = remove_specific_product(asked_id, products)
print(removed)

add_product(10, "Skrivare", "En skrivare", 1500.00, 4, products)

for idx, product in enumerate(products, 1):
    print(f"{idx} {product['name']} {product['price']}")




