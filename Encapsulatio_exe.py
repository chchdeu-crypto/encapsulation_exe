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

#mission 4
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

#mission 5
class UserProfile:
    def __init__(self,username,bio):
        self.username=username
        self.__bio=bio
    @property
    def bio(self):
        return self.__bio
class VerifiedUser(UserProfile):
    def __init__(self, username, bio,badge):
        super().__init__(username, bio)
        self.badge=badge
    def full_dicreption(self):
        print(f"{self.username} [{self.badge}]: {self.bio}")
chaim=VerifiedUser("caleb","singer and song writer","V")
chaim.full_dicreption()

#mission 6
class UserProfile:
    def __init__(self,username,age):
        self.username=username
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if 120>=age>=13:
            self.__age=age
        else:
            print("invalid age")
p=UserProfile("dan",18)
p.age=10  
p.age=200  
p.age=25
print(p.age) 

#mission 7
class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def check_passowrd(self,attempt):
        return True if attempt==self.__password else False
    def change_password(self,old,new):
        if old==self.__password:
            self.__password=new
        else:
            print("incorrect old password ")
admin=UserAccount("admin","secret")
print(admin.check_passowrd("wrong"))
admin.change_password("secret","new123")





        