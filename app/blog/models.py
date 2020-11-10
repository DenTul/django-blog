from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    title = models.CharField(verbose_name="Категория:", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    topic = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name="Заголовок:", max_length=200)
    main_img = models.ImageField(
        verbose_name="Главное изображение:",
        upload_to="blog_img/%Y/%m/%d/"
    )
    text = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name="Опубликовать", default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
