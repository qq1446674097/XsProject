from django.db import models


# Create your models here.
class ArtTga(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='作品类别',
                             unique=True,
                             db_index=True,
                             )
    add_time = models.DateTimeField(verbose_name='添加的时间',
                                    auto_now_add=True,
                                    )
    modify_time = models.DateTimeField(verbose_name='最后修改时间',
                                       auto_now=True,
                                       )

    def __str__(self):
        return self