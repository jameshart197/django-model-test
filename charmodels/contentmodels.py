from django.db import models


class AttributeContentTable(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Attribute'


class SkillsContentTable(models.Model):
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="SkillsGoverningAttribute")
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Skill'


class RaceContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    features = models.TextField(default="I am blank")

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Race'


class SubRaceContentTable(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=models.CASCADE, default=0, related_name="SubraceParentRace")
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    features = models.TextField(default="I am currently blank")

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
    SPELL_LEVELS = (
        (0, "Cantrip"),
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (5, "5th"),
        (6, "6th"),
        (7, "7th"),
        (8, "8th"),
        (9, "9th")
        )
    name = models.CharField(max_length=200)
    spell_level = models.IntegerField(choices=SPELL_LEVELS, default=0)
    full_description = models.TextField()
    spell_reqs = models.IntegerField(choices=SPELL_REQUIREMENTS, default=0)

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Spell'


class ClassContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    features = models.TextField(default="I am blank")
    saving_throw_1 = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, default=0, related_name="SavingThrow1")
    saving_throw_2 = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, default=0, related_name="SavingThrow2")
    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Class Choice'


class SubClassContentTable(models.Model):
    parent_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, default=0, related_name="SubclassParentClass")
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    features = models.TextField(default="I am blank right now")

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Subclass Choice'


class LanguageContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Language'


class BackgroundContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    feature = models.TextField()
    skill_proficiency_1 = models.ForeignKey(SkillsContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="BackgroundSkillGranted1")
    skill_proficiency_2 = models.ForeignKey(SkillsContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="BackgroundSkillGranted2")

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Background'


class AlignmentContentTable(models.Model):
    name = models.CharField(max_length=100)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Alignment'


class ToolContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Tool'
        

class InstrumentContentTable(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()

    def __str__(self):
        return f'ID: {self.id} - {self.name}'

    class Meta:
        verbose_name = 'Musical Instrument'
