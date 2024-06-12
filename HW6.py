# Класс, представляющий учителя
class Teacher:
    def __init__(self, id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher[ID: {self.id}, Name: {self.name}, Subject: {self.subject}]"

# Сервисный класс для управления учителями (Принцип единственной ответственности)
class TeacherService:
    def __init__(self):
        self.teachers = {}
        self.next_id = 1

    def add_teacher(self, name, subject):
        teacher = Teacher(self.next_id, name, subject)
        self.teachers[self.next_id] = teacher
        self.next_id += 1
        return teacher

    def edit_teacher(self, id, name=None, subject=None):
        if id in self.teachers:
            if name:
                self.teachers[id].name = name
            if subject:
                self.teachers[id].subject = subject
            return self.teachers[id]
        else:
            raise ValueError("Учитель с данным ID не найден")

    def get_all_teachers(self):
        return list(self.teachers.values())

# Класс представления для отображения учителей (Принцип единственной ответственности)
class TeacherView:
    @staticmethod
    def display_teacher(teacher):
        print(teacher)

    @staticmethod
    def display_all_teachers(teachers):
        for teacher in teachers:
            print(teacher)

# Контроллер для взаимодействия между сервисом и представлением (Принцип единственной ответственности)
class TeacherController:
    def __init__(self, service, view):
        self.service = service
        self.view = view

    def create_teacher(self, name, subject):
        teacher = self.service.add_teacher(name, subject)
        self.view.display_teacher(teacher)

    def edit_teacher(self, id, name=None, subject=None):
        try:
            teacher = self.service.edit_teacher(id, name, subject)
            self.view.display_teacher(teacher)
        except ValueError as e:
            print(e)

    def display_all_teachers(self):
        teachers = self.service.get_all_teachers()
        self.view.display_all_teachers(teachers)

# Добавляем LoggingTeacherService для демонстрации принципа открытости/закрытости
class LoggingTeacherService(TeacherService):
    def add_teacher(self, name, subject):
        teacher = super().add_teacher(name, subject)
        print(f"Учитель добавлен: {teacher}")
        return teacher

    def edit_teacher(self, id, name=None, subject=None):
        teacher = super().edit_teacher(id, name, subject)
        print(f"Учитель отредактирован: {teacher}")
        return teacher

# Пример использования
if __name__ == "__main__":
    # Создание сервиса и контроллера (Принцип инверсии зависимостей)
    service = LoggingTeacherService()
    view = TeacherView()
    controller = TeacherController(service, view)

    # Добавление учителей
    controller.create_teacher("Иван Иванович", "Математика")
    controller.create_teacher("Мария Петровна", "Русский язык")

    # Показ всех учителей
    controller.display_all_teachers()

    # Редактирование учителя
    controller.edit_teacher(1, name="Иван Иванович", subject="Физика")

    # Показ всех учителей после редактирования
    controller.display_all_teachers()
