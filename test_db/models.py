from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=122)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IpCameraParameter(models.Model):
    RESOLUTION = [
        ('5MP', 5),
        ('2MP', 2)
    ]

    CASES = [
        ('box', 'bullet'),
        ('dome', 'dome')
    ]

    LENS = [
        ('2.8mm', 2.8),
        ('4mm', 4)
    ]

    camera = models.ForeignKey(Person, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=10, choices=RESOLUTION, default='N/A')
    case = models.CharField(max_length=10, choices=CASES, default='N/A')
    lens = models.CharField(max_length=10, choices=LENS, default='N/A')

    def __str__(self):
        return f'{self.camera}'


class NVRCameraParameter(models.Model):
    CHANNEL_NUM = [
        ('16ch', 16),
        ('32ch', 32)
    ]

    HDD_NUM = [
        ('2 HDD', 2),
        ('4 HDD', 4)
    ]

    POE = [
        ('8ch', 8),
        ('16ch', 16)
    ]

    nvr = models.ForeignKey(Person, on_delete=models.CASCADE)
    channel = models.CharField(max_length=10, choices=CHANNEL_NUM, default='N/A')
    hdd = models.CharField(max_length=10, choices=HDD_NUM, default='N/A')
    poe = models.CharField(max_length=10, choices=POE, default='N/A')

    def __str__(self):
        return f'{self.nvr}'
