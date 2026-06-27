from django.db import models


# ==========================
# PROFILE
# ==========================

class Profile(models.Model):

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=200)

    bio = models.TextField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(
        max_length=200,
        blank=True
    )

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


# ==========================
# EDUCATION
# ==========================

class Education(models.Model):

    degree = models.CharField(
        max_length=100
    )

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


# ==========================
# SKILLS
# ==========================

class Skill(models.Model):

    category = models.CharField(
        max_length=100
    )

    skill_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.skill_name


# ==========================
# LANGUAGES
# ==========================

class Language(models.Model):

    language = models.CharField(
        max_length=100
    )

    level = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.language


# ==========================
# EXPERIENCE
# ==========================

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


# ==========================
# PROJECTS
# ==========================

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


# ==========================
# TESTIMONIALS
# ==========================

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
    
    
    # ==========================
# CONTACT
# ==========================

class Contact(models.Model):

    heading = models.CharField(
        max_length=100,
        default="Contact Me"
    )

    description = models.TextField()

    location = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=50
    )

    email = models.EmailField()

    linkedin = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    available_for_work = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.heading