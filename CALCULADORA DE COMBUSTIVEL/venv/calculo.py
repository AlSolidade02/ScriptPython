class Calculo:
    def __init__(self):
        self.__valor_gasolina = 5.072
        self.__valor_alcool = 3.205
        self.__valor_diesel = 4.821

        #distancia: é o valor referente à distância percorrida pelo automóvel.
        #consumo: é o valor referente ao consumo de combustível do automóvel em km/l.
    def calcular_gasto(self,distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception('o valor recebido não pode ser menor ou igual a zero') # Tratamento de erro "RAISE' não foi informada no curso

        gasto_gasolina = round(
            (distancia / consumo) * self.__valor_gasolina, 2)# qual a função do numeral dois?
        gasto_alcool = round(
            (distancia / consumo) * self.__valor_alcool,2)# qual a função do numeral dois?
        gasto_diesel = round(
            (distancia / consumo) * self.__valor_diesel,2)# qual a função do numeral dois?
        return """
                O valor total gasto será de:

                Gasolina: R$ {}
                Álcool:   R$ {}
                Diesel:   R$ {}
                """.format(
            gasto_gasolina, gasto_alcool, gasto_diesel)

#Dentro da string podemos declarar a abertura e fechamento de chaves {} para definir o espaço onde queremos inserir uma variável dentro do texto
#A função format de uma string aceita uma quantidade de parâmetros igual o número de vezes {} estão presentes na string, onde cada parâmetro é um valor que
#será convertido e inserindo dentro da string, respeitando a ordem em que se apresentam.