def main():
    quantidade = eval(input("Quantos quilos de café quer? "))
    cafe = round(quantidade*2.5, 2)
    envio = round(quantidade*0.86 + 1.5 , 2)
    iva = round((cafe + envio)*0.23 , 2)

    print("Café:", cafe)
    print("Custos gerais:", envio)
    print("IVA:", iva)
    print("Total:", cafe + iva + envio)
main()
