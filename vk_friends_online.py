import vk
import vk.exceptions

from getpass import getpass


def fetch_friends(login, password):
    session = vk.AuthSession(
        app_id=6173123,  # магическое число
        user_login=login,
        user_password=password,
    )
    vk_api = vk.API(session)
    friends_response = vk_api.friends.get(fields='id')
    if 'error' in friends_response:
        return friends_response
    return [friend for friend in friends_response if friend['online']]


if __name__ == '__main__':
    login = input('Login:')
    password = getpass('Password (would be invisible):')
    friends_response = fetch_friends(login, password)
    if 'error' in friends_response:
        print(friends_response['error']['error_msg'])
        raise SystemExit
    for friend in friends_response:
        print(friend['first_name'], friend['last_name'])