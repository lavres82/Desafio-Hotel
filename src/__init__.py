#lakewood: classificacao 3 - cliente normal 110, cliente fidelidade 80
#cliente normal final de semana 90, fidelidade 80

#bridgewood: Classificação 4 - Taxa durante a semana 160 pra clientes normais e 110 pra clientes fidelidades
#final de semana : 60 clientes normais e 50 clientes fidelidade

#ridgewood: Classificação 5 - Taxa durante a semana 220 para clientes normais e 100 para clientes fidelidade
#final de semana: 150 para clientes normais e 40 para clientes fidelidade

from dataclasses import replace


lakewood = {
    "nome": "lakewood",
    "total":0,
    "classificacao": 3,
    "tcn": 110,
    "tcf": 80,
    "tx_final_semana_normal": 90,
    "tx_final_semana_fidelidade": 80 
}

bridgewood = {
    "nome": "bridgewood",
    "total":0,
    "classificacao": 4,
    "tcn": 160,
    "tcf": 110,
    "tx_final_semana_normal": 60,
    "tx_final_semana_fidelidade": 50 
}


ridgewood = {
    "nome": "ridgewood",
    "total":0,
    "classificacao": 5,
    "tcn": 220,
    "tcf": 100,
    "tx_final_semana_normal": 150,
    "tx_final_semana_fidelidade": 40
}

entrada = input()
aux = list(map(str, entrada.split()))
print(aux)

#Dados de Entrada:
#Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
#Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)
#Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)
#['Regular:', '16Mar2009(mon),', '17Mar2009(tues),', '18Mar2009(wed)']

tipo_cliente = aux[0].replace(":", "")
#print(tipo_cliente)

dias = []

data1 = aux[1].replace("(", " ")
data1 = data1.split()
data1 = data1[1]
data1 = data1.replace(")", "")
data1 = data1.replace(",", "")
dias.append(data1)

data2 = aux[2].replace("(", " ")
data2 = data2.split()
data2 = data2[1]
data2 = data2.replace(")", "")
data2 = data2.replace(",", "")
dias.append(data2)

data3 = aux[3].replace("(", " ")
data3 = data3.split()
data3 = data3[1]
data3 = data3.replace(")", "")
data3 = data3.replace(",", "")
dias.append(data3)



#calculando os dias do hotel Lakewood
for i in dias:
    if tipo_cliente=="Regular":
        if (i=="sat" or i=="sun"):
            lakewood["total"] = lakewood["total"] + lakewood["tx_final_semana_normal"]
        else:
            lakewood["total"] = lakewood["total"] + lakewood["tcn"]
    else:
        if (i=="sat" or i=="sun"):
            lakewood["total"] = lakewood["total"] + lakewood["tx_final_semana_fidelidade"]

        else:
            lakewood["total"] = lakewood["total"] + lakewood["tcf"]



#calculando os dias do hotel bridgewood
for i in dias:
    if tipo_cliente=="Regular":
        if (i=="sat" or i=="sun"):
            bridgewood["total"] = bridgewood["total"] + bridgewood["tx_final_semana_normal"]
        else:
            bridgewood["total"] = bridgewood["total"] + bridgewood["tcn"]
    else:
        if (i=="sat" or i=="sun"):
            bridgewood["total"] = bridgewood["total"] + bridgewood["tx_final_semana_fidelidade"]

        else:
            bridgewood["total"] = bridgewood["total"] + bridgewood["tcf"]

            
#calculando os dias do hotel ridgewood
for i in dias:
    if tipo_cliente=="Regular":
        if (i=="sat" or i=="sun"):
            ridgewood["total"] = ridgewood["total"] + ridgewood["tx_final_semana_normal"]
        else:
            ridgewood["total"] = ridgewood["total"] + ridgewood["tcn"]
    else:
        if (i=="sat" or i=="sun"):
            ridgewood["total"] = ridgewood["total"] + ridgewood["tx_final_semana_fidelidade"]

        else:
            ridgewood["total"] = ridgewood["total"] + ridgewood["tcf"]

valores = {
    lakewood["total"]: lakewood["nome"], 
    bridgewood["total"]: bridgewood["nome"],
    ridgewood["total"]: ridgewood["nome"]

}



valores_keys = sorted(valores.keys())
print(valores.get(valores_keys[0]))



