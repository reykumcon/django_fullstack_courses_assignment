from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name should be at least 5 characters'
        if len(postData['content']) < 15:
            errors['content'] = 'Description should be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course, related_name='description', on_delete=models.CASCADE)

    objects = CourseManager()
