from sprite import sprite
from bug import bug

class page(sprite):
    def __init__(self, page_bug:bug):
        # super().__init__("page.jpg")

        if page_bug.found == True:
            # self.bug_image = page_bug.get_path()
            self.status = "Found"
            self.name = page_bug.type
            self.flower = page_bug.flower
            self.description = page_bug.description
        else:
            # self.bug_image =
            self.status = "Not Found"
            self.name = "???"
            self.flower = "???"
            self.description = "???"

    def get_name(self):
        return self.name
    
    def get_status(self):
        return self.status
    
    def get_description(self):
        return self.description
    
    def get_image(self):
        return self.image
    
    def get_flower(self):
        return self.flower


    
