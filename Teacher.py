class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str, academic_degree: str, administrative_position: str, experience_years: int):

        self.set_teacher_id(teacher_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_academic_degree(academic_degree)
        self.set_administrative_position(administrative_position)
        self.set_experience_years(experience_years)

    @staticmethod
    def validate_teacher_id(teacher_id: int) -> bool:
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            raise ValueError("teacher id is invalid")
        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ValueError("email is invalid")
        return True

    @staticmethod
    def validate_string(value: str, field_name: str) -> bool:
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError(f"{field_name} is invalid")
        return True

    @staticmethod
    def validate_experience_years(experience_years: int) -> bool:
        if not isinstance(experience_years, int) or experience_years < 0:
            raise ValueError("experience years is invalid")
        return True

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

    # setters (изменение значений) с валидацией
    def set_teacher_id(self, teacher_id: int):
        self.validate_teacher_id(teacher_id)
        self.__teacher_id = teacher_id

    def set_first_name(self, first_name: str):
        self.validate_string(first_name, "First name")
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        self.validate_string(last_name, "Last name")
        self.__last_name = last_name

    def set_email(self, email: str):
        self.validate_email(email)
        self.__email = email

    def set_academic_degree(self, academic_degree: str):
        self.validate_string(academic_degree, "Academic degree")
        self.__academic_degree = academic_degree

    def set_administrative_position(self, administrative_position: str):
        self.validate_string(administrative_position, "Administrative position")
        self.__administrative_position = administrative_position

    def set_experience_years(self, experience_years: int):
        self.validate_experience_years(experience_years)
        self.__experience_years = experience_years

    def __str__(self):
        return (f"Teacher_ID: {self.__teacher_id}"
                f"Fullname: {self.__first_name} {self.__last_name}, Email: {self.__email}, Degree: {self.__academic_degree}, Position: {self.__administrative_position}"
                f"Experience: {self.__experience_years} years")