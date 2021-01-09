from django.contrib import admin
from news.models import Article, Journalist
from jobsapi.models import JobOffer

admin.site.register(Article)
admin.site.register(Journalist)
admin.site.register(JobOffer)
