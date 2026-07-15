#mission 1
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
chaim=UserProfile("chaim")
print(chaim.username)
#print(chaim.__username)

#mission 2
class UserProfile:
    def __init__(self,username, email):
        self.__username=username
        self.__email=email
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
bob=UserProfile("bob","bob@mail.com")
print(bob.username,bob.email)
    
        


        