# hw6

Принцип единственной ответственности (Single Responsibility Principle): Каждый класс выполняет только одну задачу:

TeacherService отвечает за управление данными учителей.
TeacherView отвечает за отображение информации об учителях.
TeacherController управляет взаимодействием между сервисом и представлением.


Принцип открытости/закрытости (Open/Closed Principle):

Создан новый класс LoggingTeacherService, расширяющий функциональность TeacherService, не изменяя его.
Теперь, если требуется логирование действий, можно использовать LoggingTeacherService вместо изменения существующего TeacherService.


Принцип подстановки Барбары Лисков (Liskov Substitution Principle):

Класс LoggingTeacherService может использоваться везде, где используется TeacherService, не нарушая работу программы.


Принцип инверсии зависимостей (Dependency Inversion Principle):

TeacherController не создает зависимости напрямую, а получает их через конструктор, что позволяет легко менять реализации зависимостей (например, подменить TeacherService на LoggingTeacherService).
