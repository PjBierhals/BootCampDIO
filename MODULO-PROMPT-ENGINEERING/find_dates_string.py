"""Faça uma função que me retorne datas dentro de um texto. 
A função deve receber uma string e me retornar uma lista com as datas encontradas.
As datas podem estar no formato DD/MM/YYYY ou DD-MM-YYYY ou DD/MM/AA ou DD-MM-AA.

Caso não encontre nenhuma data, retorne uma lista vazia."""


import re
def find_dates_in_string(text):
    # Regex pattern to match dates in the specified formats
    date_pattern = r'\b(\d{1,2}[-/]\d{1,2}[-/](\d{4}|\d{2}))\b'
    
    # Find all matches in the text
    matches = re.findall(date_pattern, text)
    
    # Extract the full date strings from the matches
    dates = [match[0] for match in matches]
    
    return dates

"""Faça uma função que me retorne datas dentro de um texto. 
A função deve receber uma string e me retornar uma lista com as datas encontradas.
As datas podem estar no formato DD/MM/YYYY ou DD-MM-YYYY ou DD/MM/AA ou DD-MM-AA.
Se houver dastas repetidas, retorne apenas uma vez cada data.
Caso não encontre nenhuma data, retorne uma lista vazia, ME RETORNE APENAS 1 VEZ"""
def find_dates_in_string_once(text):
    # Regex pattern to match dates in the specified formats
    date_pattern = r'\b(\d{1,2}[-/]\d{1,2}[-/](\d{4}|\d{2}))\b'
    
    # Find all matches in the text
    matches = re.findall(date_pattern, text)
    
    # Extract the full date strings from the matches and remove duplicates
    dates = list(set(match[0] for match in matches))
    
    return dates