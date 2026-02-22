from sprite import sprite
from bug import bug

class page(sprite):
    def __init__(self, page_bug:bug):
        # super().__init__("page.jpg")

        if page_bug.found == True:
            # self.bug_image = page_bug.get_path()
            self.status = "Found"
            self.name = page_bug.type
            self.plant = page_bug.plant
            self.description = page_bug.description
        else:
            # self.bug_image =
            self.status = "Not Found"
            self.name = "???"
            self.plant = "???"
            self.description = "???"
    
    def __str__(self):
        return f"Name: {self.name}\nStatus: {self.status}\nFavorite Plant: {self.plant}\n{self.description}"


    
