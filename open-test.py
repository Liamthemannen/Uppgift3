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

def add_product(new_name, new_desc, new_price, new_quantity, products):
    find_max = max(products, key=lambda id: id['id'])
    max_id = find_max['id']
    new_id = max_id + 1
    
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

def change_product(changed_product, new_name,new_price,new_quantity, products):
    for i, product in enumerate(products):
        if product["id"] == changed_product - 1:
            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity
            return product
def save_products(filepath, products):
    print("Sparar...")
    try:
        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name","desc","price","quantity"])
            writer.writeheader()
            writer.writerows(products)
    except Exception as error_code:
        print("Fel")

        if isinstance(error_code, OSError) and error_code.errno == 13:
            return f"Orsak: filen är skrivskyddas"
        else:
            return f"Orsak: {error_code}"
    
    return f"Ok"
    
#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id




def show_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx} {product['name']} {product['price']}")
    



def meny(file_path):
    os.system('cls')
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
    products = load_data(file_path)

    while True:
        print("\n===== PRODUKTMENY =====")
        print("1. Visa alla produkter")
        print("2. Visa specifik produkt")
        print("3. Lägg till produkt")
        print("4. Ändra produkt")
        print("5. Ta bort produkt")
        print("6. Spara ändringar")
        print("7. Avsluta")
        
        val = int(input("Välj ett alternativ 1-7"))
        if val == 1:
            show_products(products)
        elif val == 2:
            asked_id = int(input("Vilket id vill du söka på?"))
            prod = load_specific_product(asked_id, products)
            print(prod)
        elif val == 3:
            new_name = input("Vad heter produkten: ")
            new_desc = input("Skriv en beskrivning: ")
            new_price = int(input("Skriv priset: "))
            new_quantity = int(input("Hur många av produkten: "))
            add_product(new_name, new_desc, new_price, new_quantity,products)
        elif val == 4:
            changed_id = int(input("Vilket ID vill du ändra?: "))
            new_name = input("Vad ska den heta?: ")
            new_quantity = int(input("Hur många är det nu?: "))
            new_price = int(input("Vad är det nya priset?: "))
            change_product(changed_id, new_name, new_price, new_quantity, products)
        elif val == 5:
            asked_id = int(input("Vilket id vill du ta bort?"))
            removed = remove_specific_product(asked_id, products)
            print(removed)
        elif val == 6:
            save_products(file_path, products)
        elif val == 7:
            print("Avslutar")
            break
file_path = 'C:\\Users\\liam.brundinjohanss\\Documents\\PRR2\\Uppgift3\\Uppgift3\\db_products.csv'
meny(file_path)




