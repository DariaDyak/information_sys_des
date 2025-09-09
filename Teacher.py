class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str, academic_degree: str, administrative_position: str, experience_years: int):

        if not self.validate_teacher_id(teacher_id):
            raise ValueError("Teacher ID должен быть положительным целым числом")
        if not self.validate_non_empty_string(first_name):
            raise ValueError("Имя должно быть непустой строкой")
        if not self.validate_non_empty_string(last_name):
            raise ValueError("Фамилия должна быть непустой строкой")
        if not self.validate_email(email):
            raise ValueError("Email имеет некорректный формат")
        if not self.validate_non_empty_string(academic_degree):
            raise ValueError("Ученая степень должна быть непустой строкой")
        if not self.validate_non_empty_string(administrative_position):
            raise ValueError("Административная должность должна быть непустой строкой")
        if not self.validate_experience_years(experience_years):
            raise ValueError("Стаж должен быть целым числом >= 0")

        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__academic_degree = academic_degree
        self.__administrative_position = administrative_position
        self.__experience_years = experience_years

    # 4 основных статических методов валидации идентификатора, имени и тд.
    @staticmethod
    def validate_teacher_id(teacher_id: int) -> bool:
        return isinstance(teacher_id, int) and teacher_id > 0

    @staticmethod
    def validate_email(email: str) -> bool:
        return isinstance(email, str) and "@" in email and "." in email

    @staticmethod
    def validate_non_empty_string(value):
        return isinstance(value, str) and len(value.strip()) > 0

    @staticmethod
    def validate_experience_years(experience_years: int) -> bool:
        return isinstance(experience_years, int) and experience_years >= 0

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
        if self.validate_teacher_id(teacher_id):
            self.__teacher_id = teacher_id
        else:
            raise ValueError("Invalid teacher id")

    def set_first_name(self, first_name: str):
        if self.validate_non_empty_string(first_name):
            self.__first_name = first_name
        else:
            raise ValueError("Invalid first name")

    def set_last_name(self, last_name: str):
        if self.validate_non_empty_string(last_name):
            self.__last_name = last_name
        else:
            raise ValueError("Invalid last name")

    def set_email(self, email: str):
        if self.validate_email(email):
            self.__email = email
        else:
            raise ValueError("Invalid email")

    def set_academic_degree(self, academic_degree: str):
        if self.validate_non_empty_string(academic_degree):
            self.__academic_degree = academic_degree
        else:
            raise ValueError("Invalid academic degree")

    def set_administrative_position(self, administrative_position: str):
        if self.validate_non_empty_string(administrative_position):
            self.__administrative_position = administrative_position
        else:
            raise ValueError("Invalid administrative position")

    def set_experience_years(self, experience_years: int):
        if self.validate_experience_years(experience_years):
            self.__experience_years = experience_years
        else:
            raise ValueError("Invalid experience years")

    def __str__(self):
        return (f"Teacher_ID: {self.__teacher_id}"
                f"Fullname: {self.__first_name} {self.__last_name}, Email: {self.__email}, Degree: {self.__academic_degree}, Position: {self.__administrative_position}"
                f"Experience: {self.__experience_years} years")