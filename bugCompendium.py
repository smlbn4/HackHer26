from button import button
from bug import bug
from page import page

class bugCompendium(button):
    def __init__(self):
        self.current_index = 0
        self.page = page(bug.bug_types[self.current_index])

    def turn_page_forward(self):
        if self.current_index < len(bug.bug_types) - 1:
            self.current_index += 1
            self.page = page(bug.bug_types[self.current_index])
    
    def turn_page_backwards(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.page = page(bug.bug_types[self.current_index])


if __name__ == "__main__":
    bumblebee = bug("bumblebee", 0.3, "The bumblebee is a bug.")
    bumblebee.is_found()
    grasshopper = bug("grasshopper", 0.3, "The grasshopper is a bug.")

    compendium = bugCompendium()
    print(compendium.page.get_description())
    print(compendium.page.get_name())

    compendium.turn_page_forward()
    print(compendium.page.get_description())
    print(compendium.page.get_name())
