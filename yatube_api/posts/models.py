from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import CheckConstraint, F, UniqueConstraint, Q
from django.db.models.deletion import CASCADE, SET_NULL

User = get_user_model()


class Group(models.Model):
    """Модель Группы для добавления к постам."""
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Тема группы', unique=True)
    description = models.TextField('Описание группы')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        """Человекочитаемое отображение названия группы."""
        return self.title


class Post(models.Model):
    """Модель Поста."""
    text = models.TextField(
        'Текст поста', help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=CASCADE, related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Картинка поста', upload_to='posts/',
        null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=SET_NULL, blank=True,
        null=True, related_name='posts',
        help_text='Выберите группу'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    def __str__(self):
        """Человекочитаемый текст поста, урезанный до 15 символов."""
        return self.text[:15]


class Comment(models.Model):
    """Модель комметария к посту."""
    author = models.ForeignKey(
        User, on_delete=CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name='comments'
    )
    text = models.TextField(
        'Текст комментария к посту',
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления комментария',
        auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Человекочитаемый текст комментария урезанный до 15 символов."""
        return self.text[:15]


class Follow(models.Model):
    """
    Модель Подписки на авторов постов.
    user - ссылка на объект пользователя, который подписывается.
    author - ссылка на объект пользователя, на которого подписываются.
    """
    user = models.ForeignKey(
        User, on_delete=CASCADE, related_name='follower'
    )
    author = models.ForeignKey(
        User, on_delete=CASCADE, related_name='following'
    )
    
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            UniqueConstraint(
                fields=['user', 'author'], name='unique_follower'
            ),
            CheckConstraint(check=~Q(user=F('author')),
                            name='user_cant_follow_himself'),
        ]

    def __str__(self):
        """Чиловекочитаемое обозначение подписок на авторов постов."""
        return f'{self.user.username} подписался на {self.author.username}'
