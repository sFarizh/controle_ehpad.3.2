# -*- coding: utf-8 -*-
"""
Created on Mon Fev 20 14:38:45 2023

@author: mathieu.olivier
"""
import os
import pandas as pd
from unidecode import unidecode
import re 
import json
import logging
from os import listdir

#Regle à respecter fichier excel seulement
#La feuille d'interet doit etre placée en premier
#Les noms de colonne doivent être ne première ligne et aucune colonne ne doit être vide sur la gauche

# à déplacer dans utils/utils.py 
def checkIfPathExists(file):
    if os.path.exists(file):
        os.remove(file)
        print('Ancien fichier écrasé')
        
        
def _convertXlsxToCsv(inputExcelFilePath, outputCsvFilePath):
    try:
    # Reading an excel file
    #   sheetname = getSheetName()
        excelFile = pd.read_excel(inputExcelFilePath, header=0)
        checkIfPathExists(outputCsvFilePath)
    # Converting excel file into CSV file
        excelFile.to_csv(outputCsvFilePath, index = None, header=True, sep=';', encoding='UTF-8')
        return outputCsvFilePath
    except ValueError as err:
        print(err)
        return str(err) 

        
def _convertCsvToXlsx(inputCsvFilePath, outputExcelFilePath):
    try:
    # Reading a csv file
    #   sheetname = getSheetName()
        csvFile = pd.read_csv(inputCsvFilePath)
        checkIfPathExists(outputExcelFilePath)
    # Converting CSV file into Excel file
        csvFile.to_excel(outputExcelFilePath, index = None, header=True, sep=';', encoding='UTF-8')
        return outputExcelFilePath
    except ValueError as err:
        print(err)
        return str(err)   
    
#_convertXlsxToCsv("C:/Users/mathieu.olivier/Documents/Helios/Script_V2/input/Calcul du nombre de signalements.xlsx")
# à déplacer dans utils/utils.py et à appeler dans modules/init_db/init_db.py
def _csvReader(csvFilePath):
    df = pd.read_csv(csvFilePath, sep= ';', encoding='UTF-8',low_memory=False)
    return df

# à déplacer dans utils/utils.py et à appeler dans modules/init_db/init_db.py
#Pousser le csv sans mettre en dataframe

# à déplacer dans utils/utils.py et à appeler dans modules/init_db/init_db.py
### Partie nettoyage des données


def _cleanTxt(text):
    try:
        text = unicode(text.lower(), 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unidecode(text.lower())
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")

    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text) 
    return str(text)

def _cleanSrcData(df):
# Enlever caractères spéciaux, accents, espace ( _ ) ,
    df.columns = [ _cleanTxt(i) for i in df.columns.values.tolist()]
    return df

def read_settings(path_in, dict, elem):
    """
    Permet de lire le document settings et retourne les informations souhaitées au format dictionnaire.
    Paramètres :
        - path_in : Chemin du dossier settings où sont stockées les informations.
        - dict : Dictionnaire contenant les informations que l'on recherche.
        - elem : Elément au sein du dictionnaire dont on souhaite retourner les informations.
    """
    with open(path_in) as f:
        dict_ret = json.load(f)
    L_ret = dict_ret[dict]
    param_config = {}
    for param in L_ret:
        param_config = param[elem]
    logging.info("Lecture param config" + path_in + ".")
    return param_config

# Fonction pour concaténer les différentes régions de SIVSS
def _concatSignalement():
    #créer une liste avec les noms de table de signalement
    folderPath = 'data/input/sivss'
    allSignalFiles =  listdir(folderPath)
    #allSignalFiles.remove('demo.xlsx')
    checkIfPathExists('data/to_csv/all_sivss.csv')
    # create an Empty DataFrame object
    df = pd.DataFrame()
    for fileName in allSignalFiles:
        df = pd.concat([df, pd.read_excel('data/input/sivss/'+fileName)])
    print('signalement concaténés')
    df.to_csv('data/to_csv/all_sivss.csv', index = None, header=True, sep=';', encoding='UTF-8')
    print('all_sivss.csv créé')
    return
 