from django.contrib import admin
from .models import *

# ======================
# PROFILE
# ======================

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'location'
    )


# ======================
# EDUCATION
# ======================

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'degree',
        'institution',
        'start_year',
        'end_year'
    )


# ======================
# SKILLS
# ======================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        'category',
        'skill_name'
    )

    list_filter = (
        'category',
    )


# ======================
# LANGUAGES
# ======================

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

    list_display = (
        'language',
        'level'
    )


# ======================
# EXPERIENCE
# ======================

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        'position',
        'company',
        'duration'
    )


# ======================
# PROJECTS
# ======================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'technologies'
    )


# ======================
# TESTIMONIALS
# ======================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'designation'
    )


# ======================
# CONTACT
# ======================


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'phone',
        'email',
        'available_for_work'
    )