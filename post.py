import requests
class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    def get_data(self):
        response = requests.get(self.blog_url)
        return response.json()

    def get_blog_by_id(self, blog_id):
        blogs = self.get_data()
        for blog in blogs:
            if blog["id"] == blog_id:
                return blog
