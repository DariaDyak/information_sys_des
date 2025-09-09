class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str, academic_degree: str, administrative_position: str, experience_years: int):
        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__academic_degree = academic_degree
        self.__administrative_position = administrative_position
        self.__experience_years = experience_years

    # getters (чтение значений)
    def get_teacher_id(self):
        return self.__teacher_id

    def get__first_name(self):
        return self.__first_name

    def get__last_name(self):
        return self.__last_name

    def get__email(self):
        return self.__email

    def get__academic_degree(self):
        return self.__academic_degree

    def get__administrative_position(self):
        return self.__administrative_position

    def get__experience_years(self):
        return self.__experience_years

    # setters (изменение значений)
    def set_teacher_id(self, teacher_id:int):
        self.__teacher_id = teacher_id

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name:str):
        self.__last_name = last_name

    def set_email(self, email: str):
        self.__email = email

    def set_academic_degree(self, academic_degree:str):
        self.__academic_degree = academic_degree

    def set_administrative_position(self, administrative_position: str):
        self.__administrative_position = administrative_position

    def set_experience_years(self, experience_years: int):
        if experience_years >= 0:
            self.__experience_years = experience_years
        else:
            raise ValueError("Стаж должен быть больше или равен 0")

    def __str__(self):
        return (f"Teacher_ID: {self.__teacher_id}"
                f"Fullname: {self.__first_name} {self.__last_name}, Email: {self.__email}, Degree: {self.__academic_degree}, Position: {self.__administrative_position}"
                f"Experience: {self.__experience_years} years")