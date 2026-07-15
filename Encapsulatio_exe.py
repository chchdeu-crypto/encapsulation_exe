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

#mission 8
class Post:
    def __init__(self,author,conect):
        self.author=author
        self.conect=conect
        self.__likes=0
        self.__liked_by=[]
    @property
    def likes(self):
        return self.__likes
    def like(self,username):
        if username not in self.__liked_by:
            self.__liked_by.append(username)
            self.__likes+=1
    def unlike(self,username):
        if username in self.__liked_by:
            self.__liked_by.remove(username)
            self.__likes-=1
    def status(self):
        print(f"post by {self.author}: {self.likes} likes")
post=Post("cr7","hello")
post.like("alice")
post.like("yossi")
post.like("natan")
post.like("yossi")
post.unlike("natan")
post.status()

#mission 9
class UserProfile:
    def __init__(self,username):
        self.username=username
        self.__is_public=True
        self.__show_email=False
        self.__show_age=False
    @property
    def is_public(self):
        return self.__is_public
    @is_public.setter
    def is_public(self,field):
        if isinstance(field,bool):
            self.__is_public=field
        else:
            print(f"{field} must be True or False.")
    @property
    def show_email(self):
        return self.__show_email
    @show_email.setter
    def show_email(self,field):
        if isinstance(field,bool):
            self.__show_email=field
        else:
            print(f"{field} must be True or False.")
    @property
    def show_age(self):
        return self.__show_age
    @show_age.setter
    def show_age(self,field):
        if isinstance(field,bool):
            self.__show_age=field
        else:
            print(f"{field} must be True or False.")
    def privacy_summary(self):
        print(f"is public: {self.is_public} | show email: {self.show_email} | show age: {self.show_age}")
profile=UserProfile("chaim")
profile.is_public="yes"
profile.show_email=True
profile.privacy_summary()

#mission 10
class UserAccount:
    def __init__(self,username, email, password, age):
        self.__username=username
        self.__email=email
        self.__password=password
        self.__age=age
        self._logic_count=0
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        if len(username)>=3:
            self.__username=username
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        if "@" in email:
            self.__email=email
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if 120<age>13:
            self.__age=age
    def check_passowrd(self,attempt):
        return "welcome" if attempt==self.__password else False
    def change_password(self,old,new):
        if old==self.__password:
            self.__password=new
        else:
            print("incorrect old password ")
    def login(self,password):
        if password==self.__password:
            self._logic_count+=1
        else:
            print("Login failed")
    def account_summary(self):
        print(f"{self.username} | email: {self.email} | age: {self.age} | logins: {self._logic_count}")
account=UserAccount("user1","u@gmail.com","pass123",20)
account.login(123)
account.login("aaa")
account.login("pass123")
account.email="new@email.com"
account.age=22
account.account_summary()
