import sqlite3, os
from tarfile import RECORDSIZE

connection = sqlite3.connect("DB/DiscordDB.db")
connection2 = sqlite3.connect("DB/8chan.db")
connection3 = sqlite3.connect("DB/Gettr.db")
connection4 = sqlite3.connect("DB/doxbin.db")
connection5 = sqlite3.connect("DB/weleakinfo.db")
connection6 = sqlite3.connect("DB/usemails.db")
cursor = connection.cursor()
cursor2 = connection2.cursor()
cursor3 = connection3.cursor()
cursor4 = connection4.cursor()
cursor5 = connection5.cursor()
cursor6 = connection6.cursor()


def menu():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝    180,291 Records         t.me/cultfed
    ──────────────────────────────────────────────────────────┐
     [1] Discord    (60)         [2] 8chan   (15k)            │
     [3] Gettr      (90k)        [4] Doxbin  (4k)             │
     [5] Weleakinfo  (23k)       [6] USA Emails (48k)         │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option2 = input(">$: ")
    if option2 == "1":
        os.system("cls")
        discorddb()
    elif option2 == "2":
        os.system("cls")
        eightchandb()
    elif option2 == "3":
        os.system("cls")
        gettrdb()
    elif option2 == "4":
        os.system("cls")
        doxbindb()
    elif option2 == "5":
        os.system("cls")
        weleakinfodb()
    elif option2 == "6":
        os.system("cls")
        usadb()

def usadb():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝    USA Emails      t.me/cultfed
    ──────────────────────────────────────────────────────────┐
     [1] Email Search        [2] Password Search              │
                                                              │
                                                              │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option7 = input(">$: ")
    if option7 == "1":
        usaemailsearch()
    elif option7 == "2":
        usapwsearch()


def usaemailsearch():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor6.execute(f"SELECT * FROM usemails WHERE trim(field1) LIKE '{query}';")
    results = cursor6.fetchall()
    for r in results:
        print("              ")
        print("Email:", r[0])
        print("Password:", r[1])

        
        print("========================")
        print("                         ")
        
    cursor.close()
def usapwsearch():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor6.execute(f"SELECT * FROM usemails WHERE trim(field2) LIKE '{query}';")
    results = cursor6.fetchall()
    for r in results:
        print("              ")
        print("Email:", r[0])
        print("Password:", r[1])

        
        print("========================")
        print("                         ")
        
    cursor.close()

def weleakinfodb():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝    Weleakinfo      t.me/cultfed
    ──────────────────────────────────────────────────────────┐
     [1] Email Search        [2] Name Search                  │
                                                              │
                                                              │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option6 = input(">$: ")
    if option6 == "1":
        weleakemail()

def weleakemail():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor5.execute(f"SELECT * FROM customers WHERE trim(field3) LIKE '{query}';")
    results = cursor5.fetchall()
    for r in results:
        print("              ")
        print("ID:", r[0])
        print("Email:", r[2])
        print("Name: ", r[3])
        print("Date Created: ", r[4])
        print("Card Brand: ", r[8])
        print("Card Exp Month: ", r[10])
        print("Card Exp Year:", r[11])
        print("Card Name:", r[12])
        print("Card Last 4:", r[7])
        print("User ID:", r[31])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def weleakename():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor5.execute(f"SELECT * FROM customers WHERE trim(field4) LIKE '{query}';")
    results = cursor5.fetchall()
    for r in results:
        print("              ")
        print("ID:", r[0])
        print("Email:", r[2])
        print("Name: ", r[3])
        print("Date Created: ", r[4])
        print("Card Brand: ", r[8])
        print("Card Exp Month: ", r[10])
        print("Card Exp Year:", r[11])
        print("Card Name:", r[12])
        print("Card Last 4:", r[7])
        print("User ID:", r[31])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def doxbindb():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝    Doxbin      t.me/cultfed
    ──────────────────────────────────────────────────────────┐
    [1] Username Search              [2] Password Search      │
                                                              │
                                                              │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option5 = input(">$: ")
    if option5 == "1":
        doxbinuser()
    elif option5 == "2":
        doxbinpw()

def doxbinuser():

    query = input("Enter the Username query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor4.execute(f"SELECT * FROM doxbin WHERE trim(field1) LIKE '{query}';")
    results = cursor4.fetchall()
    for r in results:
        print("              ")
        print("Username:", r[0])
        print("Password: ", r[1])
        
        print("========================")
        print("                         ")
def doxbinpw():

    query = input("Enter the Password query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor4.execute(f"SELECT * FROM doxbin WHERE trim(field2) LIKE '{query}';")
    results = cursor4.fetchall()
    for r in results:
        print("              ")
        print("Username:", r[0])
        print("Password: ", r[1])
        
        print("========================")
        print("                         ")
    cursor.close()



#////////////////////////
def gettrdb():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝     Gettr                 t.me/cultfed
    ──────────────────────────────────────────────────────────┐
      [1] Username Search          [2] Email Search           │
      [3] Home                                                │
                                                              │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option4 = input(">$: ")
    if option4 == "1":
        usersearchgettr()
    elif option4 == "2":
        emailsearchgettr()
    elif option4 == "3":
        os.system("cls")
        menu()

    
def usersearchgettr():

    query = input("Enter the ID query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor3.execute(f"SELECT * FROM gettr WHERE trim(field4) LIKE '{query}';")
    results = cursor3.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[5])
        print("Birth Year: ", r[7])
        print("Location: ", r[15])
        print("Language: ", r[12])
        print("Email: ", r[4])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def emailsearchgettr():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor3.execute(f"SELECT * FROM gettr WHERE trim(field5) LIKE '{query}';")
    results = cursor3.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[5])
        print("Birth Year: ", r[7])
        print("Location: ", r[15])
        print("Language: ", r[12])
        print("Email: ", r[4])
        
        print("========================")
        print("                         ")

        
    cursor.close()


#/////////////////////
#####################################
def eightchandb():
    print(f'''
       
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝        8chan              t.me/cultfed
    ──────────────────────────────────────────────────────────┐
     [1] ID Search       [2] Username Search                  │
     [3] Hash Search     [4] Salt Search                      │
     [5] Email Search    [6] Home                             │
                                                              │
                                                              │
   ───────────────────────────────────────────────────────────┘
    
    
    ''')
    option3 = input(">$: ")
    if option3 == "1":
        
        idsearchtwo()
    elif option3 == "2":
        usersearchtwo()
    elif option3 == "3":
        hashsearch()
    elif option3 == "4":
        saltsearch()
    elif option3 == "5":
        emailsearchtwo()
    elif option3 == "6":
        os.system("cls")
        menu()

def idsearchtwo():

    query = input("Enter the ID query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field1) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[1])
        print("Hash: ", r[2])
        print("Salt: ", r[3])
        print("Type: ", r[4])
        print("Boards: ", r[5])
        print("Email: ", r[6])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def usersearchtwo():

    query = input("Enter the Username query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field2) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[1])
        print("Hash: ", r[2])
        print("Salt: ", r[3])
        print("Type: ", r[4])
        print("Boards: ", r[5])
        print("Email: ", r[6])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def hashsearch():

    query = input("Enter the Hash query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field3) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[1])
        print("Hash: ", r[2])
        print("Salt: ", r[3])
        print("Type: ", r[4])
        print("Boards: ", r[5])
        print("Email: ", r[6])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def saltsearch():

    query = input("Enter the Salt query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field4) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[1])
        print("Hash: ", r[2])
        print("Salt: ", r[3])
        print("Type: ", r[4])
        print("Boards: ", r[5])
        print("Email: ", r[6])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def emailsearchtwo():

    query = input("Enter the Email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field7) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Username: ", r[1])
        print("Hash: ", r[2])
        print("Salt: ", r[3])
        print("Type: ", r[4])
        print("Boards: ", r[5])
        print("Email: ", r[6])
        
        print("========================")
        print("                         ")
        
    cursor.close()
############################

#UI (User Interface) Function
def discorddb():
    print(f'''
    
        
    ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
    ║  ║ ║║  ║  ║║╠╩╗
    ╚═╝╚═╝╩═╝╩o═╩╝╚═╝          Discord           t.me/cultfed
   ──────────────────────────────────────────────────────────┐
    [1] UserID Search        [2] Email Search                │
    [3] Number Search        [4] IP Search                   │
    [5] Token Search         [6] User Search                 │
    [7] Show                 [8] Home                        │
                                                             │
   ──────────────────────────────────────────────────────────┘
    ''')                            
    option = input(">$: ")
    if option == "1":
        idsearch()
    elif option == "2":
        emailsearch()
    elif option == "3":
        numbersearch()
    elif option == "4":
        ipsearch()
    elif option == "5":
        tokensearch()
    elif option =="6":
        usersearch()
    elif option == "7":
        showdb()
    elif option == "8":
        os.system("cls")
        menu()

# Function for "ID Search" Query
def idsearch():

    query = input("Enter the ID query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(UserID) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        
    cursor.close()

# Function For "Email Search" Query
def emailsearch():
    query = input("Enter the email query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(Email) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        
    cursor.close()

# Function For "Number Search" Query
def numbersearch():
    query = input("Enter the number query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(Number) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        

# Function For "IP Search" Query
def ipsearch():
    query = input("Enter the IP query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(IP) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        
    cursor.close()
def tokensearch():
    query = input("Enter the Token query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(Token) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        
def usersearch():
    query = input("Enter the Username query: ")
    if query == "cancel":
        os.system("cls")
        menu()
    cursor.execute(f"SELECT * FROM info WHERE trim(Username) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
        print("              ")
        print("UserID:", r[0])
        print("Email: ", r[1])
        print("Number: ", r[2])
        print("IP: ", r[3])
        print("Token: ", r[4])
        print("Username: ", r[5])
        
        print("========================")
        print("                         ")
        
    cursor.close()

def showdb():
    cursor.execute("SELECT * FROM info;")
    results = cursor.fetchall()
    for r in results:
        print(r)
menu()
connection.close()