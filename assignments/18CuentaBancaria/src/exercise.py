def main():
    #escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior:"))
    ingresos = float(input("Dame los ingresos:"))
    egresos = float(input("Dame los egresos:"))
    nce = int(input("Dame el número de cheques:"))

    total = ((saldo + ingresos - egresos - (total * 13)) * .925) 

    print("El saldo final de la cuenta es:", res) 
    pass

if __name__ == '__main__':
    main()
