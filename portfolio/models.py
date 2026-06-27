from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    linkedin = models.URLField()
    github = models.URLField()

    profile_image = models.ImageField(
        upload_to='profile/'
    )

    resume = models.FileField(
        upload_to='cv/'
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=100)

    institution = models.CharField(
        max_length=200
    )

    grade = models.CharField(
        max_length=20
    )

    start_year = models.CharField(
        max_length=20
    )

    end_year = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.degree


class Skill(models.Model):
    category = models.CharField(
        max_length=100
    )

    skill_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.skill_name


class Language(models.Model):
    language = models.CharField(
        max_length=100
    )

    level = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.language


class Experience(models.Model):
    position = models.CharField(
        max_length=100
    )

    company = models.CharField(
        max_length=100
    )

    duration = models.CharField(
        max_length=100
    )

    description = models.TextField()

    def __str__(self):
        return self.position


class Project(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=300
    )

    github_link = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=100
    )

    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name