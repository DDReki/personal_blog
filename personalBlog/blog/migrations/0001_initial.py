# Generated by Django 2.2.6 on 2021-01-12 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=68, verbose_name='文章标题')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_related', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('slug', models.SlugField()),
                ('desc', models.TextField(verbose_name='分类描述')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='文章标签', max_length=20, verbose_name='文章标签')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': '标签管理',
                'verbose_name_plural': '标签管理',
                'ordering': ['-tag'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='评论日期')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='所属文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '评论管理',
                'verbose_name_plural': '评论管理',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tags', verbose_name='文章标签'),
        ),
    ]
