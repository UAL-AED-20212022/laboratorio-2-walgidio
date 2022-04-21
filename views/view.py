#Importar todas as funções presentes em LinkedList.py e em controller.py
from models.LinkedList import *
import controllers.controller as clr

def main():

    lista_ligada = LinkedList()

    while True:

        comandos = input().upper().split()

        if comandos[0] == 'RPI':
            pais_novo = comandos[1].capitalize()
            registar_inicio(lista_ligada, pais_novo)
        
        elif comandos[0] == 'RPF':
            pais_novo = comandos[1].capitalize()
            registar_fim(lista_ligada, pais_novo)

        elif comandos[0] == 'RPDE':
            pais_novo = comandos[1].capitalize()
            pais_registado = comandos[2].capitalize()
            registar_depois_elemento(lista_ligada, pais_registado, pais_novo)

        elif comandos[0] == 'RPAE':
            pais_novo = comandos[1].capitalize()
            pais_registado = comandos[2].capitalize()
            registar_antes_elemento(lista_ligada, pais_registado, pais_novo)

        elif comandos[0] == 'RPII':
            pais_novo = comandos[1].capitalize()
            indice = int(comandos[2])
            registar_posicao_especifica(lista_ligada, pais_novo, indice)

        elif comandos[0] == 'VNE':
            verificar_num_elementos(lista_ligada)

        elif comandos[0] == 'VP':
            nome_pais = comandos[1].capitalize()
            verificar_pais(lista_ligada, nome_pais)

        elif comandos[0] == 'EPE':
            eliminar_primeiro_elemento(lista_ligada)

        elif comandos[0] == 'EUE':
            eliminar_ultimo_elemento(lista_ligada)

        elif comandos[0] == 'EP':
            nome_pais = comandos[1].capitalize()
            eliminar_pais(lista_ligada, nome_pais)



def registar_inicio(lista_ligada, pais_novo):
    clr.registar_inicio(lista_ligada, pais_novo)
    lista_ligada.traverse_list()

def registar_fim(lista_ligada, pais_novo):
    clr.registar_fim(lista_ligada, pais_novo)
    lista_ligada.traverse_list()

def registar_depois_elemento(lista_ligada, pais_registado, pais_novo):
    clr.registar_depois_elemento(lista_ligada, pais_registado, pais_novo)
    lista_ligada.traverse_list()

def registar_antes_elemento(lista_ligada, pais_registado, pais_novo):
    clr.registar_antes_elemento(lista_ligada, pais_registado, pais_novo)
    lista_ligada.traverse_list()

def registar_posicao_especifica(lista_ligada, pais_novo, indice):
    clr.registar_posicao_especifica(lista_ligada, pais_novo, indice)
    lista_ligada.traverse_list()

def verificar_num_elementos(lista_ligada):
    count = clr.verificar_num_elementos(lista_ligada)
    print(f'O número de elementos são {count}.')

def verificar_pais(lista_ligada, nome_pais):
    resultado = clr.verificar_pais(lista_ligada, nome_pais)
    if resultado == False:
        print(f'O país {nome_pais} não se encontra na lista.')
    else:
        print(f'O país {nome_pais} encontra-se na lista.')

def eliminar_primeiro_elemento(lista_ligada):
    eliminado = clr.retornar_primeiro_elemento(lista_ligada)
    clr.eliminar_primeiro_elemento(lista_ligada)
    print(f'O país {eliminado} foi eliminado da lista.')

def eliminar_ultimo_elemento(lista_ligada):
    eliminado = clr.retornar_ultimo_elemento(lista_ligada)
    clr.eliminar_ultimo_elemento(lista_ligada)
    print(f'O país {eliminado} foi eliminado da lista.')

def eliminar_pais(lista_ligada, nome_pais):
    resultado = clr.verificar_pais(lista_ligada, nome_pais)
    if resultado == False:
        print(f'O país {nome_pais} não se encontra na lista.')
    else:
        clr.eliminar_pais(lista_ligada, nome_pais)
        print(f'O país {nome_pais} foi eliminado da lista')
