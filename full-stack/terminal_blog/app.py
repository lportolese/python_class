from database import Database
from models.blog import Blog


Database.initialize()

blog = Blog(author="Lisa Portolese",
            title="Sample Title",
            description="Sample description"
            )
blog.new_post()

blog.save_to_mongo()

blog_database = Blog.from_mongo(blog.id)

print(blog.get_post())
