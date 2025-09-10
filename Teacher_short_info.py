from Teacher import Teacher

class Teacher_short_info:
    def __init__(self, teacher:Teacher, inn:str, ogrn: str):
        self.last_name=teacher.get__last_name()
        self.initial = f"{teacher.get__first_name()[0]}"
        self.inn=inn
        self.ogrn=ogrn

    def __str__(self):
        return (f"Teacher short info: {self.last_name} {self.initial}, inn:{self.inn}, ogrn:{self.ogrn}")