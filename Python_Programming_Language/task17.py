# Create a class called Human

# Initialize the class

class Human:
    name = "Samuel"
    group = "Male"
    colour = "Black"
    age = "20"

    def get_name_group_colour_age(self):
        return self.name + ":" + self.group + ":" + self.colour + ":" + self.age


Samuel = Human()
print(Samuel.name, Samuel.group, Samuel.colour, Samuel.age, Samuel.get_name_group_colour_age())
