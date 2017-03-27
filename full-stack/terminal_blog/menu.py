from models.blog import Blog


class Menu(object):
    def __init__(self):
        # allow user to enter name
        # check in they already have an account
        # if not, prompt to creae
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self.user._user_has_account():
            print ("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            se.

    def _prompt_user_for_account
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog



    def run_menu(self):
        # user read or write blog
        read_or_write = input("Do you want to read (R) or write (W) a blog? ")
        # if read:
        if read_or_write == 'R':
        # list blogs in database
        #  allow user to pick on
        #  display post
        elif read_write == 'W'