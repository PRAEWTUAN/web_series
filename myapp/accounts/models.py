# series/models.py
from django.db import models
from django.contrib.auth.models import User
class Series(models.Model):
    title = models.CharField(max_length=200)
    cover_image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    country = models.CharField(max_length=100)
    average_rating = models.FloatField(default=0)  # เพิ่มฟิลด์สำหรับคะแนนเฉลี่ย

    def __str__(self):
        return self.title

class Comment(models.Model):
    series = models.ForeignKey(Series, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.series.title}'

class Rating(models.Model):
    series = models.ForeignKey(Series, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # ค่าคะแนน 1 ถึง 5

    def __str__(self):
        return f'Rating {self.score} for {self.series.title}'

class WatchList(models.Model):
    user = models.ForeignKey(User, related_name='watchlist', on_delete=models.CASCADE)
    series = models.ManyToManyField(Series)  # เชื่อมกับซีรีส์ที่ต้องการดู

    def __str__(self):
        return f'Watchlist of {self.user.username}'

