
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "b66ef67b37817fff3ab83645022438af6b076103830a15d97d344168840f0361dcb1a4407cad0c1aa8621"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def msg_001(user_id):
    msg_send(user_id, 'text\ntext')

def send_message(user_id, message):
    from random import randint
    vk.method('messages.send',
        {'user_id': user_id,
        "random_id":randint(1,1000) ,
        'message': message,}
    )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            
            get_msg = event.text.lower() # get_msg
            msg_send = send_message # msg_send

            if text == '=help': # 
                send_message(user_id, 'Мои команды:')
                
            elif 'привет' in text: # привет > И тебе привет
                msg_send(user_id, 'И тебе привет')
                
            elif 'чо' in get_msg or 'что' in get_msg:
                msg_send(user_id, 'ЧТО')
                
            else: msg_send(user_id, 'Я не есть тебя понимать')
            
            print(event.user_id, ':', text)
            
