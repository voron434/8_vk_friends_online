import vk
import os
import vk.exceptions

from getpass import getpass

APP_ID = os.environ.get('APP_ID')


def if_error_sys_exit(response):
    if 'error' in response:
        print(response['error']['error_msg'])
        raise SystemExit


if __name__ == '__main__':
    login = input('Login:')
    password = getpass('Password (would be invisible):')
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        vk_api = vk.API(session)
    except vk.exceptions.VkAuthError:
        print('Incorrect login or password')
        raise SystemExit
    online_friends_ids = vk_api.friends.getOnline(online_mobile=1)
    if_error_sys_exit(online_friends_ids)
    online_friends_pc_info = vk_api.users.get(user_ids=online_friends_ids['online'])
    online_friends_mobile_info = vk_api.users.get(user_ids=online_friends_ids['online_mobile'])
    if_error_sys_exit(online_friends_pc_info)
    if_error_sys_exit(online_friends_mobile_info)
    print('Your pc-online friends:')
    for friend in online_friends_pc_info:
        print(friend['first_name'], friend['last_name'])
    print('Your mobile-online friends:')
    for friend in online_friends_mobile_info:
        print(friend['first_name'], friend['last_name'])