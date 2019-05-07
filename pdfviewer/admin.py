from django.contrib import admin

# Register your models here.

from .models import Score, Score_Comments



class CommentInline(admin.StackedInline):
    model = Score_Comments
    extra = 3

class ScoreAdmin(admin.ModelAdmin):
    fields = ['title', 'pdf_url', 'mei_url']
    inlines = [CommentInline]


admin.site.register(Score, ScoreAdmin)
