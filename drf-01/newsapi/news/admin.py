from django.contrib import admin
from news.models import Article, Journalist
from jobsapi.models import JobOffer
from ebooksapi.models import Ebook, Review

admin.site.register(Article)
admin.site.register(Journalist)
admin.site.register(JobOffer)
admin.site.register(Ebook)
admin.site.register(Review)
