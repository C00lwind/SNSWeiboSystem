# Generated by Django 2.0.3 on 2018-03-19 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '微博分类',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, verbose_name='评论日期')),
                ('comment_type', models.IntegerField(choices=[(0, '评论'), (1, '点赞')], default=0)),
                ('comment', models.CharField(blank=True, max_length=140, null=True, verbose_name='评论内容')),
                ('p_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='app01.Comment', verbose_name='父级评论')),
            ],
            options={
                'verbose_name_plural': '评论表',
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('code', models.CharField(max_length=4, verbose_name='验证码')),
                ('stime', models.DateTimeField(auto_now=True, verbose_name='生效时间')),
                ('status', models.IntegerField(choices=[(0, '未成功'), (1, '已成功')], default=0, verbose_name='注册状态')),
            ],
            options={
                'verbose_name_plural': '临时邮箱验证码',
                'db_table': 'EmailCode',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='话题名称')),
                ('readers', models.IntegerField(default=1, verbose_name='阅读数量')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': '话题',
                'db_table': 'Topic',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_created=True, verbose_name='创建时间')),
                ('user', models.IntegerField(choices=[(1, '管理员'), (2, '普通用户'), (3, 'VIP用户')], default=2, verbose_name='用户类型')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('brief', models.CharField(blank=True, max_length=140, null=True, verbose_name='个人简历')),
                ('sex', models.IntegerField(choices=[(0, '女'), (1, '男')], default=1, verbose_name='性别')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('head_img', models.ImageField(blank=True, null=True, upload_to='./static/img/user_pic', verbose_name='头像')),
                ('followed_list', models.ManyToManyField(blank=True, related_name='my_fans', to='app01.UserProfile', verbose_name='我的关注')),
            ],
            options={
                'verbose_name_plural': '用户表',
                'db_table': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wb_type', models.IntegerField(choices=[(0, '发布'), (1, '转发'), (2, '收藏')], default=0, verbose_name='微博类型')),
                ('text', models.CharField(max_length=140, verbose_name='微博内容')),
                ('permission', models.IntegerField(choices=[(0, '公开'), (1, '仅自己可见'), (2, '好友圈')], default=0, verbose_name='微博权限')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('forward_or_collect_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forward_or_collects', to='app01.Weibo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserProfile')),
            ],
            options={
                'verbose_name_plural': '微博表',
                'db_table': 'Weibo',
            },
        ),
        migrations.CreateModel(
            name='WeiboMore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_content', models.CharField(blank=True, max_length=128, null=True, verbose_name='图片内容')),
                ('picture_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weiboPhoto', to='app01.Weibo', verbose_name='微博相关图片')),
            ],
            options={
                'verbose_name_plural': '微博媒体仓库',
                'db_table': 'WeiboMore',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='to_weibo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Weibo', verbose_name='评论的微博'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserProfile', verbose_name='评论的人'),
        ),
    ]