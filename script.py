import csv
import numpy as np

#Funzione che conta i punti di ogni giocatore dati i punteggi di squadra
def contaPunti(puntiSq):
    moneyBall = 1       #Iniziliazzo punti
    punteggi = {} #Salvo i punteggi dei giocatori in un dizionario

    
    #Scorro tutti i punti segnati in puntiSq,
    #Se è zero vuol dire che è vuoto, aggiungo punti alla "moneyball"
    #Se è diverso da zero aggiungo i punti della moneyball al giocatore riconosciuto

    for giocatore in puntiSq:
        #Se il numero è 0 aggiunge punti che vengono asseganti al primo numero diverso da zero che appare
        if(giocatore == '0'):
            moneyBall+=1
        else:
            if giocatore in punteggi:    #Se un giocatore è già presente nel dist non lo faccio
                punteggi[giocatore] += moneyBall
            else:
                punteggi[giocatore] = moneyBall
        
            moneyBall = 1
    
    print("Punteggi:", punteggi)

    return punteggi



#Immport del csv
results = []
with open("table-1.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

#Elimino le prime due righe che contengono le scritte della tabella
del results[0] 
del results[0]

#Ordino il dataset per tenerlo a colonne
s = [[str(e) for e in row] for row in results]

#Cambio la struttura della tabella in input
puntiA = []
punteggioA = [1, 5, 9, 13]
for e in punteggioA:
    for i in range(len(s)):
        puntiA.append(s[i][e])

puntiB = []
punteggioB = [4, 8, 12, 16]
for e in punteggioB:
    for i in range(len(s)):
        puntiB.append(s[i][e])

#print(puntiA)
print(contaPunti(puntiA))
print(contaPunti(puntiB))
