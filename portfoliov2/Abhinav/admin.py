from django.contrib import admin
from .models import (
    UserAboutPage, 
    PersonalWorkPage, 
    ContributionWorkPage,
    PhotographyWorkPage,
    HomePageModel)

admin.site.register(UserAboutPage)
admin.site.register(PersonalWorkPage)
admin.site.register(ContributionWorkPage)
admin.site.register(PhotographyWorkPage)
admin.site.register(HomePageModel)

admin.site.site_header = 'PORTFOLIO ADMIN'