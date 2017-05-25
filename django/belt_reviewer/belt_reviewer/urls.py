
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from apps.login.models import User as U
from apps.book_reviews.models import Author, Book, Review

class UAdmin(admin.ModelAdmin):
   pass
admin.site.register(U, UAdmin)

@admin.register(Author, Book, Review)
class DefaultAdmin(admin.ModelAdmin):
    pass

# from apps.book_reviews.models import Author as Author
# from apps.book_reviews.models import Book as Book
# from apps.book_reviews.models import Review as Review


# class AuthorAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Author, AuthorAdmin)

# class BookAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Book, BookAdmin)

# class ReviewAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Review, ReviewAdmin)




urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^', include('apps.book_reviews.urls', namespace="book_reviews")),
    url(r'^login/', include('apps.login.urls', namespace="login")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
]