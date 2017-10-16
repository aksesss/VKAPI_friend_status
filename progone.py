from ClientVK import *
from gist import Gist


def main():
    username = input('Введите логин вк: ')
    # username = "fs44fs4fs"
    # username = "allling"
    # username = "tolaysha"

    client_get_id = ClientGetID(username)
    user_id = client_get_id.execute()

    if client_get_id.is_success():
        print("ID: ", user_id)
    else:
        print('Нету такого айди, мэн')
        return 0

    # find age list
    friends_ages_list = ClientGetFriendsAges(user_id).execute()
    if len(friends_ages_list) == 0:
        print('УУУУУ, нет друзей')
        return 0
    else:
        print("Ages: ", friends_ages_list)
        # write gist
        username_friend_gist = Gist(friends_ages_list)
        username_friend_gist.printGist()

    # show gist
    title = "Ages of Users "
    title_x = "Ages"
    title_y = "Users"
    username_friend_gist.showBar(title, title_x, title_y)


main()
