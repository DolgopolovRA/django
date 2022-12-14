from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    body = models.TextField(verbose_name="Содержимое")
    body_as_markdown = models.BooleanField(
        default=False, verbose_name="As markdown")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"{self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _('новость')
        verbose_name_plural = _('новости')


class Course(models.Model):
    name = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False)

    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Стоимость", default=0)
    cover = models.CharField(
        max_length=25, default="no_image.svg", verbose_name="Изображение")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _('курс')
        verbose_name_plural = _('курсы')


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Номер урока")
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"№{self.num} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ("course", "num")


class CourseTeacher(models.Model):
    course = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=128, verbose_name="Имя")
    last_name = models.CharField(max_length=128, verbose_name="Фамилия")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"№{self.first_name} {self.last_name}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = 'курс к учителю'
        verbose_name_plural = 'курсы к учителям'


class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"),
              (1, "⭐"))
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    feedback = models.TextField(
        default=_("No feedback"), verbose_name=_("Feedback"))
    rating = models.SmallIntegerField(
        choices=RATING, default=5, verbose_name=_("Rating"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} ({self.user})"
