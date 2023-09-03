# Николай Крупичко 8-поток — Финальный проект. Инженер по тестированию плюс
import sender_request

def test_get_order_success():
    track = sender_request.post_new_order().json()["track"]
    status_code = sender_request.get_order(track).status_code
    assert status_code == 200