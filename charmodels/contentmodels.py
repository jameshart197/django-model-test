from django.db import models


class AttributeContentTable(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Attribute'


class SkillsContentTable(models.Model):
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="SkillsGoverningAttribute")
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Skill'


class RaceContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Race'


class SubRaceContentTable(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=models.CASCADE, default=0, related_name="SubraceParentRace")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name} {self.race}'

    class Meta:
        verbose_name = 'Subrace'


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
    spell_level = models.IntegerField(default=1)   # range limit 1-9
    full_description = models.CharField(max_length=1000)
    spell_reqs = models.IntegerField(choices=SPELL_REQUIREMENTS, default=0)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Spell'


class ClassContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Class'


class SubClassContentTable(models.Model):
    parent_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, related_name="SubclassParentClass")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Subclass'


class LanguageContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Language'


class BackgroundContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)
    feature = models.CharField(max_length=500)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Background'


class AlignmentContentTable(models.Model):
    name = models.CharField(max_length=100)
    full_description = models.CharField(max_length=400)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Alignment'


class ToolContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Tool'
