class Reflection:
    def __init__(self,creation_date, reflection, user_id, title,tags,mood):
        self.creation_date = creation_date
        self.reflection = reflection
        self.user_id = user_id
        self.title = title
        self.tags = tags
        self.mood = mood

    def __repr__(self):
        return (f"Task(creation_date={self.creation_date!r}, reflection={self.reflection!r}, "
                f"user_id={self.user_id!r}, title={self.title!r}, tags={self.tags!r}, mood={self.mood!r})")

