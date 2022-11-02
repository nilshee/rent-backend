from locale import DAY_1
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date
from django.utils import timezone


class Priority(models.Model):
    prio = models.PositiveSmallIntegerField(
        verbose_name='priority in renting queue')
    name = models.CharField(
        max_length=100, verbose_name='name of the priority class')
    description = models.CharField(
        max_length=255, verbose_name='description of the priority class', null=True)


class Profile(models.Model):
    """
    extension of User model for addtitional information
    """
    class Meta:
        permissions=[
            ("inventory_editing", "able to edit and create the inventory and got nearly full access"),
            ("general_access","got general Access to everything, but no editing rights"),
            ("lending_access", "is able to lend stuff")
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prio = models.ForeignKey(Priority, on_delete=models.CASCADE)
    authorized = models.BooleanField(
        verbose_name='authorized to rent objects', default=False)
    newsletter = models.BooleanField(
        verbose_name='newsletter signup', default=False)


class Category(models.Model):
    """
    To categorize each RentalObjectType
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RentalObjectType(models.Model):
    """
    Parenttype for objects
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_id_prefix',
                fields=['prefix_identifier']
            )
        ]
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rentalobjecttypes')
    description = models.TextField(default='')
    # hide objects from rentalpage
    visible = models.BooleanField(default=False)
    image = models.ImageField()
    prefix_identifier = models.CharField(max_length=20, default="LZ")

    def __str__(self) -> str:
        return self.name


class PublicInfoObjectType(models.Model):
    """
    to show public information about an objectType
    """
    object_type = models.ForeignKey(RentalObjectType, on_delete=models.CASCADE)
    # infotype e.g. Warning danger (everything that works with material)
    type = models.CharField(max_length=20, verbose_name='material type')
    content = models.TextField()


class RentalObject(models.Model):
    type = models.ForeignKey(RentalObjectType, on_delete=models.CASCADE, related_name='rentalobjects')
    # if the object also got a external identifier e.g. a department uses its own identifiers but the objects also got a inventory number of the company
    inventory_number = models.CharField(max_length=100, null=True, blank=True)
    # maybe broken so it shouldnt be rentable
    rentable = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.type.name + " " + str(self.type.prefix_identifier) + str(self.pk)


class InternalInfoObjectType(models.Model):
    object_type = models.ForeignKey(RentalObjectType, on_delete=models.CASCADE)
    # infotype e.g. Warning danger (everything that works with bootstrap)
    type = models.CharField(max_length=20, verbose_name='Information type')
    content = models.TextField()


class RentalOperation(models.Model):
    object = models.ForeignKey(RentalObject, on_delete=models.CASCADE)
    renter = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='renter')
    lender = models.ForeignKey(User, blank=True, null=True,
                               default=None, on_delete=models.CASCADE, related_name='lender')
    return_processor = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                         related_name='return_processor', verbose_name='person who processes the return')
    rejected = models.BooleanField()
    operation_number = models.BigIntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    reserved_from = models.DateTimeField()
    reserved_until = models.DateTimeField()
    picked_up_at = models.DateTimeField(null=True, default=None)
    handed_out_at = models.DateTimeField(null=True, default=None)
    received_back_at = models.DateTimeField(null=True, default=None)

# TODO add reservation model with RentalObjecttype and count


class OnPremiseTimeSlot(models.Model):
    day = models.SmallIntegerField()
    start_time = models.TimeField()
    duration = models.DurationField()


class OnPremiseBlockedTimes(models.Model):
    """
    To block specific days e.g. someone is ill
    """
    starttime = models.DateTimeField(default=None, null=False)
    endtime = models.DateTimeField(default=None, null=False)


class OnPremiseBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showed_up = models.BooleanField()
    start_datetime = models.DateTimeField()
    duration = models.DurationField()


class Notification(models.Model):
    type = models.CharField(max_length=100, default='email')
    receiver = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True)
    send_at = models.DateTimeField(default=timezone.now)


class Settings(models.Model):
    """
    for general dynamic Settings like general lenting day and rocketchat url and email setup
    """
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Suggestion(models.Model):
    """
    for suggestions which obejcts should be rented together
    """
    suggestion = models.ForeignKey(
        RentalObjectType, on_delete=models.CASCADE, related_name='suggestion')
    suggestion_for = models.ForeignKey(
        RentalObjectType, on_delete=models.CASCADE, related_name='suggestion_for')
