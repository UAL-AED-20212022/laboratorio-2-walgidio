#Importar todas as funções presentes em LinkedList.py e em Node.py
from models.LinkedList import *
from models.Node import *

def registar_inicio(lista_ligada, pais_novo):
    #Adiciona um elemento no princípio da lista
    lista_ligada.insert_at_start(pais_novo)
    return lista_ligada

def registar_fim(lista_ligada, pais_novo):
    #Adiciona um elemento no final da lista
    lista_ligada.insert_at_end(pais_novo)
    return lista_ligada

def registar_depois_elemento(lista_ligada, pais_registado, pais_novo):
    #Adiciona um novo elemento depois do elemento indicado
    lista_ligada.insert_after_item(pais_registado, pais_novo)
    return lista_ligada

def registar_antes_elemento(lista_ligada, pais_registado, pais_novo):
    #Adiciona um novo elemento antes do elemento indicado
    lista_ligada.insert_before_item(pais_registado, pais_novo)
    return lista_ligada

def registar_posicao_especifica(lista_ligada, pais_novo, indice):
    #Adiciona um elemento na posição indicada
    lista_ligada.insert_at_index(indice, pais_novo)
    return lista_ligada

def verificar_num_elementos(lista_ligada):
    #Retorna o número de elementos da lista
    return lista_ligada.get_count()

def verificar_pais(lista_ligada, nome_pais):
    #Verifica se o país indicado está presente na lista
    return lista_ligada.search_item(nome_pais)

def eliminar_primeiro_elemento(lista_ligada):
    #Remove o primeiro elemento da lista
    lista_ligada.delete_at_start()
    return lista_ligada

def eliminar_ultimo_elemento(lista_ligada):
    #Remove o último elemento da lista
    lista_ligada.delete_at_end()
    return lista_ligada

def retornar_primeiro_elemento(lista_ligada):
    #Retorna o primeiro elemento da lista
    lista_ligada.reverse_linkedlist()
    eliminado = lista_ligada.get_last_node()
    lista_ligada.reverse_linkedlist()
    return eliminado

def retornar_ultimo_elemento(lista_ligada):
    #Retorna o último elemento da lista
    eliminado = lista_ligada.get_last_node()
    return eliminado

def eliminar_pais(lista_ligada, nome_pais):
    #Remove o país indicado da lista
    lista_ligada.delete_element_by_value(nome_pais)
    return lista_ligada
