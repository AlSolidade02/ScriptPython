from calculo import Calculo
import PySimpleGUI as sg

def main():
    calcular = Calculo()# objeto calculo
    layout = [[sg.Text('''Esta aplicação tem como finalidade demonstrar os valores que serão gastos
        com combustível durante uma viagem, com base no consumo do seu veículo, e
        com a distância determinada por você!''')],
                  [sg.Text('''Os combustíveis disponíveis para este cálculo são: 
                •	Álcool
                •	Diesel
                •	Gasolina''')],
                  [sg.Text('Distância a ser percorrida (KM):'), sg.Input(key='distancia')],# Entrada de distancia do usuario
                  [sg.Text('Consumo por litro: '), sg.Input(key='litro')],# Entrada de litros do usuario
                  [sg.Button('Calcular consumo')],# botão de calculo
                  [sg.Output(size= (50, 20))]# Saida
                ]


    window = sg.Window('Calculadora de combustivel ', layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        distancia = float(values['distancia'])
        litro = float(values['litro'])

        print(calcular.calcular_gasto(distancia, litro))

if __name__ == "__main__":
    main()