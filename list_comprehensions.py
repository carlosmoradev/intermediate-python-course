#Crear una lista con los cuadrados de los 100 primeros naturales no divisibles por 3
def run():
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)


if __name__ == '__main__':
    run()