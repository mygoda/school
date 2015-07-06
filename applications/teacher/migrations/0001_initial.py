# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubjectsTemplate'
        db.create_table(u'teacher_subjects_tpl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['SubjectsTemplate'])

        # Adding model 'SchoolClass'
        db.create_table(u'teacher_school_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['SchoolClass'])

        # Adding model 'Teacher'
        db.create_table(u'teacher_teachers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.SubjectsTemplate'], null=True, blank=True)),
            ('is_master', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['Teacher'])

        # Adding model 'Term'
        db.create_table(u'teacher_term_tpl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0, max_length=128)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.SubjectsTemplate'], null=True, blank=True)),
            ('school_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.SchoolClass'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['Term'])

        # Adding model 'SchoolClassTeacherShip'
        db.create_table(u'teacher_teacher_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], null=True, blank=True)),
            ('school_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.SchoolClass'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['SchoolClassTeacherShip'])

        # Adding model 'SchoolClassMasterShip'
        db.create_table(u'teacher_master_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], null=True, blank=True)),
            ('school_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.SchoolClass'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['SchoolClassMasterShip'])

        # Adding model 'TeacherTermShip'
        db.create_table(u'teacher_term_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], null=True, blank=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Term'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['TeacherTermShip'])

        # Adding model 'TeacherMessage'
        db.create_table(u'teacher_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=2578, null=True, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['TeacherMessage'])

        # Adding model 'TeacherSchedule'
        db.create_table(u'teacher_teacher_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], null=True, blank=True)),
            ('week', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=2528, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 6, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'teacher', ['TeacherSchedule'])


    def backwards(self, orm):
        # Deleting model 'SubjectsTemplate'
        db.delete_table(u'teacher_subjects_tpl')

        # Deleting model 'SchoolClass'
        db.delete_table(u'teacher_school_class')

        # Deleting model 'Teacher'
        db.delete_table(u'teacher_teachers')

        # Deleting model 'Term'
        db.delete_table(u'teacher_term_tpl')

        # Deleting model 'SchoolClassTeacherShip'
        db.delete_table(u'teacher_teacher_ship')

        # Deleting model 'SchoolClassMasterShip'
        db.delete_table(u'teacher_master_ship')

        # Deleting model 'TeacherTermShip'
        db.delete_table(u'teacher_term_ship')

        # Deleting model 'TeacherMessage'
        db.delete_table(u'teacher_message')

        # Deleting model 'TeacherSchedule'
        db.delete_table(u'teacher_teacher_schedule')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'teacher.schoolclass': {
            'Meta': {'object_name': 'SchoolClass', 'db_table': "u'teacher_school_class'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'teacher.schoolclassmastership': {
            'Meta': {'object_name': 'SchoolClassMasterShip', 'db_table': "u'teacher_master_ship'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'null': 'True', 'blank': 'True'}),
            'school_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.SchoolClass']", 'null': 'True', 'blank': 'True'})
        },
        u'teacher.schoolclassteachership': {
            'Meta': {'object_name': 'SchoolClassTeacherShip', 'db_table': "u'teacher_teacher_ship'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.SchoolClass']", 'null': 'True', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'null': 'True', 'blank': 'True'})
        },
        u'teacher.subjectstemplate': {
            'Meta': {'object_name': 'SubjectsTemplate', 'db_table': "u'teacher_subjects_tpl'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'teacher.teacher': {
            'Meta': {'object_name': 'Teacher', 'db_table': "u'teacher_teachers'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.SubjectsTemplate']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        u'teacher.teachermessage': {
            'Meta': {'object_name': 'TeacherMessage', 'db_table': "u'teacher_message'"},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '2578', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'teacher.teacherschedule': {
            'Meta': {'object_name': 'TeacherSchedule', 'db_table': "u'teacher_teacher_schedule'"},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '2528', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'null': 'True', 'blank': 'True'}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'teacher.teachertermship': {
            'Meta': {'object_name': 'TeacherTermShip', 'db_table': "u'teacher_term_ship'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Term']", 'null': 'True', 'blank': 'True'})
        },
        u'teacher.term': {
            'Meta': {'object_name': 'Term', 'db_table': "u'teacher_term_tpl'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'school_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.SchoolClass']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.SubjectsTemplate']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '128'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'user'"},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'student_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['teacher']