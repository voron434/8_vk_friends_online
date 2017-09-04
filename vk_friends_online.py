import vk
import os
import vk.exceptions

from getpass import getpass

APP_ID = os.environ.get('APP_ID')


def fetch_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
        )
        vk_api = vk.API(session)
    except vk.exceptions.VkAuthError:
        return {'error': {'error_msg': 'Incorrect login or password'}}
    friends_response = vk_api.friends.get(fields='id')
    return friends_response


if __name__ == '__main__':
    login = input('Login:')
    password = getpass('Password (would be invisible):')
    friends_response = fetch_friends(login, password)
    if 'error' in friends_response:
        print(friends_response['error']['error_msg'])
        raise SystemExit
    online_friends = [friend for friend in friends_response if friend['online']]
    for friend in online_friends:
        print(friend['first_name'], friend['last_name'])