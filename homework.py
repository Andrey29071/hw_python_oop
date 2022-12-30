class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 traning_type,
                 duration,
                 distance,
                 speed,
                 calories) -> None:
        pass


    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                'Длительность: {self.duration: .3f} ч.; '
                'Дистанция: {self.distance: .3f} км; '
                'Ср. скорость: {self.speed: .3f} км/ч; '
                'Потрачено ккал: {self.calories: .3f}. ')

class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_H: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    def __init__(self, action: int, 
                 duration: float, 
                 weight: float) -> None:
        super().__init__(action, duration, weight)


    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_spent_calories() 
                + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight 
                / self.M_IN_KM * (self.duration * self.MIN_IN_H))
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    KMH_IN_MSEC: float = 0.278
    CM_IN_M: int = 100
    
    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    
    def get_spent_calories(self) -> float:
        return ((self.CALORIES_WEIGHT_MULTIPLIER 
                * self.weight 
               + ((self.get_mean_speed() * self.KMH_IN_MSEC)**2 
                / (self.height / self.CM_IN_M)
                * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight))
               * self.duration * self.MIN_IN_H)
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
