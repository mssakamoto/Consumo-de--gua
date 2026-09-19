Tipo_de_imóvel = input("Digite o tipo de imóvel (comercial ou casa ou apartamento): ")
Consumo_de_água = float(input("Digite o consumo mensal de água em metros cúbicos m3 (Ex: 15.5): "))
if Tipo_de_imóvel == "comercial":
    print("Tarifa comercial apliacada - consulte o plano corporativo")
elif Tipo_de_imóvel == "apartamento" and Consumo_de_água < 10:
    print("Consumo econômico - excelente controle de água")
elif Tipo_de_imóvel == "casa" or Tipo_de_imóvel == "apartamento" and Consumo_de_água <= 25:
    print("Consumo moderado - dentro do padrão residencial")
else:
    print("Consumo excessivo - adote medidas de economia de água e verifique possíveis vazamentos")