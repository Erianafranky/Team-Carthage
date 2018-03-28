import cmd
class User(object):
    def __init__(self):
        self.users = [{'admin':'admin12','is_admin':True},{'moderator':'mod1','is_moderator':True}]
        self.isadmin = False
        self.is_moderator = False  
        self.comments = list() 
    def register(self, username, password,confirm):
        id = len(self.users)
        if username.strip() == '':
            print ("username should not be empty")
        if password != confirm:
            print ('password mistmatch')
        user = {
             'user_id': id,
             'username':username,
             'password':password,
             'conf_pwd':confirm,
              self.isadmin : False,
              self.is_moderator : False

        }
        self.users.append(user) 

    def login(self,username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                print('logged in') 
            continue
        print ('user does not exist')


    def Comment(self,id, body, username, user_id):
           comment = {
           'comment_id': id,
           'user_id': user_id,
           'username':username,
           'body':body}
           self.comments.append(comment)
           
    def view_all(self):
        for comment in self.comments:
            print(comment)

class Moderator(User):
    def __init__(self, id,body):
       pass

class Admin(Moderator):
    def __init__(self, id,body):
        User.__init__(self)
        Moderator.__init__(self)


class Post(object):
    def __init__(self, id,body,author):
        self.posts = list()

    def make_post (self,id ,body,author):
        pass
class Comment(object):

    def __init__(self, id,body):
        self.comments = []
        self.to_be_moderated = []

def main():
    user1 = User()

    print (
        """
          welcome to the commentor app
          You can:
          1 register
          2 login as user
          3 add comment
          4 edit comment
          5 view comments
        """
    )
    choice = input('what do you want to do >>>')
    if choice == 1:
        print ('you have chosen to register, enter your details.')
        username = str(input('Enter name'))
        pwd = str(input('Enter pwd'))
        cnf_pwd = str(input('Enter confirm password'))
        user1.register(username,pwd,cnf_pwd)

    elif choice == 2:
        print ('you have chosen to login, enter your details.')
        username = input('Enter name')
        pwd = input('Enter pwd')
        user1.login(username,pwd)

    elif choice == 3:
        print ('you have chosen to add a comment.')
        username = input('Enter username')    
        body = input('Enter comment body')
        user1.login(username,pwd)
        user1.Comment(3,body,username,2)

    elif choice == 5:
        print ('you have chosen to view comments.')
        user1.view_all()
  
 
if __name__ == '__main__':
    main()


