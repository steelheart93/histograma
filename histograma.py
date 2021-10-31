import matplotlib.pyplot as plot


def sumdigit(num):
    sum, ext = 0, 0
    while num != 0:
        ext = num % 10
        num //= 10
        sum += ext
    return sum


if __name__ == "__main__":
    loteria = []
    frecuentes = []

    for i in range(10000):
        number = sumdigit(i)
        loteria.append(number)

        end3 = sumdigit(i // 10)
        init3 = sumdigit(i % 1000)

        # Aplicar resultados del histograma a tres números
        regla3 = (init3 == 13 or init3 == 14) and (end3 == 13 or end3 == 14)

        end2 = sumdigit(i // 100)
        mid2 = sumdigit((i//10) % 100)
        init2 = sumdigit(i % 100)

        # Aplicar resultados del histograma a 2 números
        regla2 = init2 == 9 and mid2 == 9 and end2 == 9

        if number == 18 and regla3 and regla2:
            frecuentes.append(i)

    # Cálculamos los extremos de los intervalos.
    intervalos = range(min(loteria), max(loteria) + 2)

    plot.hist(x=loteria, bins=intervalos, color='#F2AB6D', rwidth=0.85)
    plot.title('Histograma de Lotería - matplotlib - codigopiton.com')
    plot.xlabel('Lotería')
    plot.ylabel('Frecuencia')
    plot.xticks(intervalos)

    # En teoría los más probables.
    print(frecuentes)  # [4545, 5454]

    # Dibujamos el histograma.
    plot.show()
