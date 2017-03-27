from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # allow user to enter name
        # check in they already have an account
        # if not, prompt to creae
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
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
            self._list_blogs()
            self._view_blogs()
            pass

        elif read_or_write == 'W':
            self._prompt_write_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter ID of the blog you would like to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("Date {}, title {}\n\n{}".format(post['created_date'], post['title'], post['content']))
