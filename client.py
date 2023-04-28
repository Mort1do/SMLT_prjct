import requests

i = input("Введите номер страницы: ")
get = requests.get("http://127.0.0.1:3000/", i)
print(get.json())

#print(" 1)Get object from server", '\n', "2)Input object to the server: ")
#num = int(input("input the number:"))
#if num == 1:
#    i = input("Input the number(index) of object: ")
#    line = "http://127.0.0.1:3000/obj/" + i
#    get = requests.get(line)
#    print(get.json())
#elif num == 2:
#    adr = str(input("Input the adress of object: "))
#    st = str(input("Input the state of object: "))
#    adm = str(input("Input the name of admin of object: "))
#    test3 = requests.post("http://127.0.0.1:3000/obj/4", json = {"adress": adr, "state": st, "admin": adm})
#elif num == 3:
#    lg = str(input("Input the login: "))
#    ps = str(input("Input the password: "))
#    log = requests.post("http://127.0.0.1:3000/obj/log", json = {"login": lg, "password": ps})
#else:
#    print("Error")