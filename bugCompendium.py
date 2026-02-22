from button import button
from bug import bug
from page import page

class bugCompendium(button):
    # Set the page index to 0 
    def __init__(self):
        self.page_index = 0
        self.page = page(bug.bug_types[self.page_index])

    def turn_page_forward(self):
        if self.page_index < len(bug.bug_types) - 1:
            self.page_index += 1
            self.page = page(bug.bug_types[self.page_index])
    
    def turn_page_backwards(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.page = page(bug.bug_types[self.page_index])


if __name__ == "__main__":
    bumblebee = bug("bumblebee", 0.5, "The bumblebee is a bug.", "beebalm")
    bumblebee.is_found()
    grasshopper = bug("grasshopper", 0.2, "The grasshopper is a bug.", "lettuce")

    compendium = bugCompendium()
    print()
    print(str(compendium.page))
    print()

    compendium.turn_page_forward()
    print(str(compendium.page))
    print()
