from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    date_of_entry = models.DateField(verbose_name='Дата ввода в эксплуатацию')
    base_fuel_consumption = models.FloatField(verbose_name='Базовый расход топлива')
    trailer_fuel_consumption = models.FloatField(verbose_name='Расход топлива на прицеп')
    transport_fuel_consumption = models.FloatField(verbose_name='Расход топлива - транспортная работа')
    initial_mileage = models.IntegerField(verbose_name='Начальный пробег')
    is_used = models.BooleanField(verbose_name='Используется?')
    fuel_type = models.CharField(max_length=50, verbose_name='Тип топлива')
    registration_number = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    depreciation = models.FloatField(verbose_name='Амортизационные отчисления')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Trip(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата завершения')
    comment = models.TextField(verbose_name='Комментарий')
    status = models.CharField(max_length=50, verbose_name='Статус')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    driver1 = models.CharField(max_length=100, verbose_name='Водитель 1')
    driver2 = models.CharField(max_length=100, verbose_name='Водитель 2')
    climate_control = models.BooleanField(verbose_name='Климат-контроль')

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Request(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    creation_date = models.DateField(verbose_name='Дата создания')
    insurance_costs = models.FloatField(verbose_name='Затраты на страхование')
    expected_revenue = models.FloatField(verbose_name='Ожидаемая выручка')
    other_costs = models.FloatField(verbose_name='Прочие затраты')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class RequestCost(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name='Заявка')
    value_choice = models.CharField(max_length=10, verbose_name='Выбор значения')  # План/Факт
    fuel_consumption = models.FloatField(verbose_name='Расход топлива')
    driver1_payment = models.FloatField(verbose_name='Оплата водителю 1')
    driver2_payment = models.FloatField(verbose_name='Оплата водителю 2')
    depreciation = models.FloatField(verbose_name='Амортизация')
    insurance = models.FloatField(verbose_name='Страхование')
    other_costs = models.FloatField(verbose_name='Прочие затраты')
    total = models.FloatField(verbose_name='Итого')

    class Meta:
        verbose_name = 'Себестоимость заявки'
        verbose_name_plural = 'Себестоимости заявок'

class RouteDetail(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name='Заявка')
    point = models.CharField(max_length=100, verbose_name='Пункт')
    loading_unloading = models.CharField(max_length=50, verbose_name='Погрузка/Выгрузка')
    arrival_date_time = models.DateTimeField(verbose_name='Дата и время прибытия')
    cargo_weight = models.FloatField(verbose_name='Масса груза')

    class Meta:
        verbose_name = 'Детали маршрута заявки'
        verbose_name_plural = 'Детали маршрутов заявок'




