from  vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import methods

vk_session = vk_api.VkApi(token='d84987b114afdf4816a9358035f7b9a4e3ddfebf416f5ecaa4e449fbb5cf64f31b9519d6e34643a97d4ec')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в ' + str(datetime.strftime(datetime.now(), '%H:%M:%S')))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if (event.from_user) and (not (event.from_me)):
                if response in methods.hellowords:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message':methods.answer(), 'random_id':0})
                else:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': methods.messages(), 'random_id': 0})




