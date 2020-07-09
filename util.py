def analisar_sentimento(classificador, texto):
    message = "<!> Esse texto é considerado"
    predicted = classificador.preditor_texto(texto)
    message += (" positivo pelo classificador %s."%classificador.nome) if int(predicted[0]) > 0 else (" negativo pelo classificador %s."%classificador.nome)
    print(message)