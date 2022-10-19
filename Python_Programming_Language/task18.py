class Human:
    name = "Samuel"
    leg_count = "4"
    can_walk = "True"

    def get_name_leg_count_can_walk(self):
        return self.name + ":" + self.leg_count + ":" + self.can_walk


Samuel = Human()
print(Samuel.name, Samuel.leg_count, Samuel.can_walk, Samuel.get_name_leg_count_can_walk()