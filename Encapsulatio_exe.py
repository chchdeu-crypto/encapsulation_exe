#mission 1
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
chaim=UserProfile("chaim")
print(chaim.username)
print(chaim.__username)

        