from django.db import models

class HomePageModel(models.Model):
    UserVideo = models.FileField(upload_to='videos/%Y/%m/%d/', null=True)
    UserBitmoji = models.ImageField(upload_to='images-bitmoji',null = True)
    UserWork = models.ImageField(upload_to='images-bitmoji',null = True)
    UserReach = models.ImageField(upload_to='image-bitmoji',null= True)
    workIntroduction = models.TextField(default= 'enter work')
    Introduction = models.TextField()

    def __str__(self):
        return 'ABHINAV MISHRA'
    
    class Meta:
        verbose_name = 'HOME PAGE' 

class UserAboutPage(models.Model):
    name = models.CharField(max_length=50)
    Image = models.ImageField(default=' image_21.jpeg',upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ' ABOUT PAGE' 

class PersonalWorkPage(models.Model):
    personalName = models.CharField(max_length=50, null=True, blank=True)
    personalWorkImage = models.ImageField(default=' image_21.jpeg',upload_to='images-work/')
    personalWorkDescription = models.TextField(null=True, blank=True)
    personalLink = models.URLField(default= 'https://github.com/abhinav1590',max_length=200)

    def __str__(self):
        return self.personalName

    class Meta:
        verbose_name = 'PERSONAL WORK PAGE' 

class ContributionWorkPage(models.Model):
    contributedName = models.CharField(default='Null Name',max_length=100,null=True, blank=True)
    contributedWorkImage = models.ImageField(default='image_21.jpeg',upload_to='images-work-contrib/')
    contributedWorkDescription = models.TextField(default='enter description',null=True, blank=True)
    contributedLink = models.URLField(default= 'https://github.com/abhinav1590',max_length=200)

    def __str__(self):
        return self.contributedName

    class Meta:
        verbose_name = 'CONTRIBUTED WORK PAGE' 

class PhotographyWorkPage(models.Model):
    userPhotoName = models.CharField(max_length= 50, null= True, blank= True)
    userPhotoDescription = models.TextField(default='Add description / quote ',null= False, blank = False)
    userPhoto = models.ImageField(default='image_21.jpeg',upload_to = 'image-photography/')

    def __str__(self):
        return self.userPhotoName

    class Meta:
        verbose_name = 'PHOTOGRAPHY PAGE' 
    