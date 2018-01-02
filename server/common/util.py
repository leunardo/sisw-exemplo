"""Módulo utilitário"""

from datetime import datetime

def hora_atual():
    """"Retorna a hora atual"""
    hora = str(datetime.now())
    return hora

def send_response(data, status=200, error=None):
    """Wrapper que é responsável por padronizar as respostas feitas pelo servidor"""
    return { 'data': data, 
             'status': status, 
             'error': error  }
             