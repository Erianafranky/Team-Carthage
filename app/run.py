import cmd
class User(cmd.Cmd):
   def __init__(self):
       self.users = [{'admin':'admin12','is_admin':True},{'moderator':'mod1','is_moderator':True}]
       self.isadmin = False
       self.is_moderator = False   
   def register(self, username, password, conf_pwd):
       id = len(self.users)
       if username.strip() == '':
           print ("username should not be empty")
       if password != conf_pwd:
           print ('password mistmatch')
       user = {
            'user_id': id,
            'username':username,
            'password':password,
            'confirm':conf_pwd,
             self.isadmin : False,
             self.is_moderator : False

       }
       self.users.append(user)

   def do_login(self,username, password):
       for user in self.users:
           if user['username'] == username and user['password'] == password:
               print('logged in') 
           continue
       print ('user does not exist')

   def do_Comment(self,id, body, username, user_id):
       pass
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
   choice = input('what do you want to do >>>')
   if choice == 1:
       user1 = User.register('collo','12343','12343')
       print (user1)




if __name__ == '__main__':
   main()
