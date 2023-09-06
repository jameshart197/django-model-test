from django.db import models


class AttributeContentTable(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)


class SkillsContentTable(models.Model):
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.SET_NULL, related_name="governing attribute")
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)


class RaceContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class SubRaceContentTable(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=models.CASCADE, related_name="race")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class SpellsContentTable(models.Model):
    SPELL_REQUIREMENTS = (
        (0, ""), 
        (1, "Verbal"), 
        (2, "Somatic"), 
        (3, "Verbal and Somatic"), 
        (4, "Material"), 
        (5, "Verbal and Material"), 
        (6, "Somatic and Material"), 
        (7, "Verbal, Somatic and Material")
        )
    name = models.CharField(max_length=200)
    spell_level = models.IntegerField(max_length=1)
    full_description = models.CharField(max_length=1000)
    spell_reqs = models.IntegerField(choices=SPELL_REQUIREMENTS, default=0)


class ClassContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class SubClassContentTable(models.Model):
    parent_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, related_name="class")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class LanguageContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class BackgroundContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)
    feature = models.CharField(max_length=500)


class AlignmentContentTable(models.Model):
    name = models.CharField(max_length=100)
    full_description = models.CharField(max_length=400)


class ToolContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)