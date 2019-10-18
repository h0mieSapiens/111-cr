from menu import print_menu
from ITEM import Item
import pickle
import datetime
logs =[]
items=[]
id_count= 1
item_file="item.data"
logs_file="logs.data"

def print_log():
    print_header("LOGS")
    for log in logs:
        print(log)
def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time
def stock_v():
    stock=0
    for item in items:
        stock+=(item.stock * item.price)

        print(f"the total is: {stock}")
def register_purchase():
    print_header("PURCHASE")
    found = False
    item_list("Choose an Item")  # mostrar todos los items
    id = input("\n Select ID:")  # preguntar id

    for item in items:
        if (str(item.id) == id):
            stock = input("input how many:")  # pregunta si el ID es el mismo que el usuario ingreso
            item.stock -= int(stock)
            found = True
            log_line = get_time() + "|PURCHASE| " + id
            logs.append(log_line)
            save_log()
    if (not found):
        print("ERROR")
    print(f"you purchased {stock} items!")
def register_sell():
    print_header("SELL")
    found = False
    item_list("Choose an Item")  # mostrar todos los items
    id = input("\n Select ID:")  # preguntar id

    for item in items:
        if (str(item.id) == id):
            stock = input("input how many :")  # pregunta si el ID es el mismo que el usuario ingreso
            item.stock += int(stock)
            found = True
            log_line = get_time() + "|SELL| " + id
            logs.append(log_line)
            save_log()
    if (not found):
        print("ERROR")
    print(f"you selled {stock} items!")
def items_category():
    temp_list = []
    for item in items:
        if(item.category not in temp_list): #esto hace que si la categoria del item no esta en la lista temporal lo agrega
            temp_list.append(item.category)
    print(temp_list)
def read_items():
    try:
        global id_count
        reader = open(item_file, "rb")
        temp_list = pickle.load(reader) #lee el binario y lo convierte en el objeto original


        for item in temp_list:
            items.append(item)
        last = items[-1]    #te da el ultimo valor de la cadena
        id_count = last.id + 1
        print("loaded:" + str(len(temp_list)) + "items")
    except:
        print("error")
def read_log():
    try:

        reader = open(logs_file, "rb")
        temp_list = pickle.load(reader) #lee el binario y lo convierte en el objeto original


        for log in temp_list:
            logs.append(log)

        print("loaded:" + str(len(temp_list)) + "items")
    except:
        print("error")
def update_stock():
    found = False
    item_list("Choose an Item") #mostrar todos los items
    id= input("\n Select ID:") #preguntar id

    for item in items:
        if(str(item.id)==id):
            stock= input("input new value:")    #pregunta si el ID es el mismo que el usuario ingreso
            item.stock = int(stock)
            found= True
            log_line = get_time() + "|UPDATE| " + id
            logs.append(log_line)
            save_log()
    if(not found):
        print("ERROR")
def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)
def register_item():
    global id_count #importar la variable a toda la funcion

    print_header("register new Item")


    title= input("please input the Title:")
    category= input("please input Category:")
    price = float(input("please input price:"))
    stock = int(input("please input stock:"))

    new_item=Item()
    new_item.id= id_count

    new_item.title= title
    new_item.category=category
    new_item.price = price
    new_item.stock =stock
    #validando los valores
    id_count +=1
    items.append(new_item)
    log_line = get_time() + "|REGISTER| " + str(id_count)
    logs.append(log_line)
    save_log()


read_items()
read_log()

def item_list(header_text):
    print_header(header_text)
    print("ID  | Item Title                | Category        | Price     | Stock")
    print("_" * 70)

    for item in items:
        print(f"{str(item.id).ljust(3)} | {item.title.ljust(25)} | {item.category.ljust(15)} | {str(item.price).rjust(9)} | {str(item.stock).rjust(5)}"  ) #poniendo el item en sus caracteristicas
#rljust es para hacer padding
def no_stock():
    print_header("Items WIth no Stock:")
    for item in items:
        if(item.stock == 0):
            print(item.title)



def save_items():
    writer= open(item_file, "wb")  #wb= writw in binary(este metodo abre un archivo)
    pickle.dump(items, writer)
    writer.close()
    print("Data saved!")
def save_log():
    writer= open(logs_file, "wb")  #wb= writw in binary(este metodo abre un archivo)
    pickle.dump(logs, writer)
    writer.close()
    print("log saved!")



def delete_item():

    item_list("Choose an Item") #mostrar todos los items
    id= input("\n Select title:") #preguntar id

    for item in items:
        if(str(item.id)==id):
            items.remove(item)


#########################











opc=''
while(opc != 'x'):
    print_menu()

    opc= input("please select an option:")
    if (opc == "x"):
        break  # esto cierra el while
    elif(opc=='1'):
        register_item()
        save_items()

    elif(opc=="2"):
        item_list("list of items")
    elif(opc=="3"):
        update_stock()
        save_items()
    elif (opc == "5"):
        delete_item()
        save_items()

    elif (opc=="6"):
        items_category()
    elif (opc=="7"):
        stock_v()
    elif (opc=="8"):
        register_purchase()
    elif (opc=="9"):
        register_sell()
    elif (opc=="10"):
        print_log()
    input("\n\nPress Enter to continue...")


