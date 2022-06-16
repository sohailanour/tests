# Generated by Django 2.2.24 on 2021-06-14 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_sequences', '0012_add_user_partition_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionSequencePartitionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_section_sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_sequences.CourseSectionSequence')),
                ('user_partition_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_sequences.UserPartitionGroup')),
            ],
            options={
                'unique_together': {('user_partition_group', 'course_section_sequence')},
            },
        ),
        migrations.CreateModel(
            name='SectionPartitionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_sequences.CourseSection')),
                ('user_partition_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_sequences.UserPartitionGroup')),
            ],
            options={
                'unique_together': {('user_partition_group', 'course_section')},
            },
        ),
        migrations.AddField(
            model_name='coursesection',
            name='new_user_partition_groups',
            field=models.ManyToManyField(db_index=True, related_name='sec_user_partition_groups', related_query_name='sec_user_partition_group', through='learning_sequences.SectionPartitionGroup', to='learning_sequences.UserPartitionGroup'),
        ),
        migrations.AddField(
            model_name='coursesectionsequence',
            name='new_user_partition_groups',
            field=models.ManyToManyField(db_index=True, related_name='secseq_user_partition_groups', related_query_name='secseq_user_partition_group', through='learning_sequences.SectionSequencePartitionGroup', to='learning_sequences.UserPartitionGroup'),
        ),
    ]
