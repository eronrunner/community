from object_management.UserManager import UserManager

if __name__ == '__main__':
    linked_id = "nphatdat@gmail.com"
    user_m = UserManager()
    print(user_m.delete(linked_id))
    n_user = user_m.create(linked_id)
    print(n_user.to_json())