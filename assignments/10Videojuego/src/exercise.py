def main():
    #escribe tu código abajo de esta línea
    x = int(1000)
    y = int(350)

    jn = int(input("Dame la cantidad de juegos nuevos:"))
    ju = int(input("Dame la cantidad de juegos usados:"))

    comp = jn * x + ju * y

    print("El total de la compra es:", comp)

    pass
   



if __name__ == '__main__':
    main()
