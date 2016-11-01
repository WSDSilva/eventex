from django.db import models
# trecho abaixo comentado 1º
# class EmailContactManager(models.Manager):
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.EMAIL)
#         return  qs
#
# class PhoneContactManager(models.Manager):
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.PHONE)
#         return  qs

class KindContactQuerySet(models.QuerySet):

    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)

# trecho abaixo comentado 2º
# class KindContactManager(models.Manager):
#
#     def get_queryset(self):
#         return KindContactQuerySet(self.model, using=self._db)
#
#     def emails(self):
#         return self.filter(kind=self.model.EMAIL)
#
#     def phones(self):
#         return self.filter(kind=self.model.PHONE)


class PeriodManager(models.Manager):

    MIDDAY = '12:00'
    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)