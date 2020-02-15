import vk_api

def get_conversations(vk, vk_tools):
    conversation_list = vk_tools.get_all(method='messages.getConversations', max_count=100,
                                         values={'extended': 1, 'fields': 'first_name, last_name, name'})
    conversations = []
    for conversation in conversation_list['items']:
        messages = vk_tools.get_all(max_count=200, method='messages.getHistory',
                               values={'rev': 1, 'extended': 1, 'fields': 'first_name, last_name',
                                       'peer_id': conversation['conversation']['peer']['id']})
        conversations.append({'id': conversation['conversation']['peer']['id'], 'messages': messages})
    return conversations

if __name__ == '__main__':
    API_VERSION = '5.92'
    APP_ID =  # id приложения
    token = '' # токен
    vk_session = vk_api.VkApi(token=token, app_id=APP_ID, api_version=API_VERSION)
    vk = vk_session.get_api()
    vk_tools = vk_api.VkTools(vk)
    print(get_conversations(vk, vk_tools))
