# Николай Крупичко 8-поток — Финальный проект. Инженер по тестированию плюс
import configuration
import  data
import requests

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.create_order,
                         headers=data.headers)

def get_order(token):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t":token})
