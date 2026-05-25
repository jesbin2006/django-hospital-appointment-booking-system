from django.db import models
from django.contrib.auth.models import User
from department.models import Department
from doctors.models import Doctors
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class Appointment(models.Model):

    PERSON_TYPE = [
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('aged', 'Aged'),
        ('baby', 'Newly baby'),
    ]

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('after attending', 'After attending')
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField()

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doctor = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE,
        related_name='appointments',
        null=True,
        blank=True
    )

    date = models.DateTimeField()

    person_type = models.CharField(max_length=20, choices=PERSON_TYPE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"patient:{self.name}| username: {self.user.username if self.user else 'No User'} |department: {self.department}"


    def save(self, *args, **kwargs):

        old_status = None

        if self.pk:
            old_status = Appointment.objects.get(pk=self.pk).status

        super().save(*args, **kwargs)

        if old_status != "confirmed" and self.status == "confirmed":

            if self.user and self.user.email:

                subject = "Appointment Confirmed"

                text_content = f"""
Hi {self.user.username},

Your appointment is CONFIRMED ✔

Doctor: {self.doctor}
Date: {self.date}

Thank you,
Hospital Team
"""

                html_content = f"""
                <h2>🏥 Appointment Confirmed</h2>
                <p>Hi <b>{self.user.username}</b>,</p>

                <p>Your appointment is <b style='color:green;'>CONFIRMED</b> ✔</p>

                <p><b>Doctor:</b> {self.doctor}</p>
                <p><b>Date:</b> {self.date}</p>

                <br>
                <p>Thank you,<br>Hospital Team</p>
                """

                email = EmailMultiAlternatives(
                    subject,
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [self.user.email]
                )

                email.attach_alternative(html_content, "text/html")
                email.send()