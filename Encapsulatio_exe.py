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
    
#mission 3
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        if len(username)>=3:
            self.__username=username
        else:
            print("Username too short")
p=UserProfile("alice")
p.username="ab"
p.username="alexis"
print(p.username)

#mission 
class UserProfile:
    def __init__(self,username):
        self.__username=username
        self.__followers=0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers+=1
    def unfollow(self):
        if self.__followers>0:
            self.__followers-=1
chaim=UserProfile("chaim")
chaim.follow()
chaim.follow()
chaim.follow()
chaim.unfollow()
print(chaim.followers)

        


        