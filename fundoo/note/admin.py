from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from note.documents import NotesDocument
from .models import Notes, Label #, UpdatedUser


# @admin.register(UpdatedUser)
# class User(UserAdmin):
#     class Meta:
#         model = UpdatedUser


class NoteAdmin(admin.ModelAdmin):
    list_display = ['user', "note", 'title', 'image', 'is_archive', 'is_trashed', 'reminder']
    list_filter = ['reminder']

    class Meta:
        model = Notes



admin.site.register(Notes, NoteAdmin)
admin.site.register(Label)
