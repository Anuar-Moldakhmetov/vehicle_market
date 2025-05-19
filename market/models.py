from django.db import models

class Aviation(models.Model):
    class AviationTypes(models.TextChoices):
        JET = 'jet', 'Истребитель'
        SHTORM_AVIATION = 'shtorm_aviation', 'Штурмовая авиация'
        HELICOPTER = 'helicopter', 'Ветролёты'
    
    class WeaponTypes(models.TextChoices):
        GUN = 'gun', 'Скорострельная пушка'
        ROCKET_AIR_EARTH = 'rocket_air_earth', 'Воздух-земля'
        ROCKET_AIR_AIR = 'rocket_air_air', 'Воздух-воздух'
        
    class FuelTypes(models.TextChoices):
        KEROSINE = 'kerosene', 'Керосин'
        GAZOLIE = 'gazoline', 'Бензин'

    photo = models.ImageField(upload_to='aviation_photos/', blank=True, null=True)

    def __str__(self):
        return self.name    
 
    name = models.CharField(max_length=50)
    type = models.CharField(choices = AviationTypes.choices, max_length=50)
    country = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    max_speed = models.IntegerField()
    weapon_type = models.CharField(choices = WeaponTypes.choices, max_length=50)
    fuel = models.CharField(choices = FuelTypes.choices, max_length=50)
    crew = models.IntegerField()


class ArmoredVehicles(models.Model):
    class ArmoredVehicleTypes(models.TextChoices):
        HEAVY_ARMORED_VEHICLE = 'heavy_armored_vehicle', 'Тяжёлая бронетехника',
        LEGHT_ARMORED_VEHICLE = 'light_armored_vehicle', 'Лёгкая бронетехника',

    class WeaponTypes(models.TextChoices):
        LARGE_CALIBER_GUN = 'large_caliber_gun', 'Крупнокалиберная пушка'
        SMALL_CALIBER_GUN = 'small_caliber_gun', 'Малокалиберная пушка'
        LARGE_CALIBER_GUN_MACHINE_GUN = 'large_caliber_machine_gun', 'Крупнокалиберный пулемёт'
        SMALL_CALIBER_GUN_MACHINE_GUN = 'small_caliber_machine_gun', 'Малокалиберный пулемёт'


    class FuelTypes(models.TextChoices):
        DIESEL_FUEL = 'diesel fuel', 'Солярка'
        GAZOLINE = 'gazoline', 'Бензин'

    class TowerTypes(models.TextChoices):
        INHABITED = 'inhabited', 'Обитаемая'
        UNINHABITED = 'uninhabited', 'Необитаемая'

    class NutritionTypes(models.TextChoices):
        MACHINE = 'machine', 'Автомат'
        LOADER = 'loader', 'Заряжающий'
    
    photo = models.ImageField(upload_to='ArmoredVehicles_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    type = models.CharField(choices = ArmoredVehicleTypes.choices, max_length=50)
    country = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    max_speed = models.IntegerField()
    weapon_type = models.CharField(choices = WeaponTypes.choices, max_length=50)
    fuel = models.CharField(choices = FuelTypes.choices, max_length=50)
    tower = models.CharField(choices = TowerTypes.choices, max_length=50)
    crew = models.IntegerField()
    is_amphibian = models.BooleanField()
    armor_thickness_cm = models.IntegerField()
    nutrition_type = models.CharField(choices = NutritionTypes.choices, max_length=50)


