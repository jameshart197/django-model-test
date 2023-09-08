from django.db import models
from .contentmodels import *
from django.contrib.auth.models import User

# top level models


class CharacterDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterSubrace")
    alignment = models.ForeignKey(AlignmentContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterAlignment")
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterBackground")
    character_name = models.CharField(max_length=200)
    inspiration = models.BooleanField(default=False)
    faith = models.TextField(blank=True)
    age = models.CharField(max_length=24, blank=True) 
    height = models.CharField(max_length=24, blank=True)
    weight = models.CharField(max_length=24, blank=True)  
    notes = models.TextField(blank=True)
    backstory = models.TextField(blank=True)
    allies = models.TextField(blank=True)
    enemies = models.TextField(blank=True)
    factions_and_orgs = models.TextField(blank=True)
    hit_points = models.IntegerField(default=12)
    armor_class = models.IntegerField(default=10)

    def __str__(self):
        return f'ID: {self.id} - {self.character_name}'

    class Meta:
        verbose_name = 'Character'


class CharacterSpells(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SpellsCharacter")
    spell = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="CharacterSpells")

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} {self.spell}'
    
    class Meta:
        verbose_name = 'Character Spell'


class CharacterLevels(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="LevelsCharacter")
    char_class = models.ForeignKey(ClassContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="LevelsClass")
    level = models.IntegerField(default=1)  # range limit 1-20

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} - {self.subclass.name} - {self.level}'
    
    class Meta:
        verbose_name = 'Character Level'


class CharacterSavingThrows(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SavingThrowsCharacter")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, related_name="SavingThrowsGoverningAttribute")

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} - {self.attribute.name}'
    
    class Meta:
        verbose_name = 'Character Saving Throw'

class CharacterSkillProficiencies(models.Model):
    PROFICIENCY_LEVEL = (
        (0, "Proficient"),
        (1, "Expertise"),
        (2, "Half-Proficiency (Bard)")
        )
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SkillsCharacter")
    skill = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SkillsSkill")
    proficiency_level = models.IntegerField(choices=PROFICIENCY_LEVEL)

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} - {self.skill.name} - {self.proficiency_level}'

    class Meta:
        verbose_name = 'Character Skill'


class CharacterAttributes(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="AttributesCharacter")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, related_name="AttributesAttribute")
    score = models.IntegerField(default=10)  # range limit 1-30

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} - {self.attribute.name} - {self.score}'

    class Meta:
        verbose_name = 'Character Attribute'


# Link Models

#SUBRACE

class SubraceToSkillProficiencies(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SkillprofsSubrace")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SubraceSkillGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subrace.name} - {self.skill_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Subrace Granted Skill'


class SubraceLanguages(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="LanguagesSubrace")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="SubraceLanguageGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subrace.name} - {self.language_granted.name}'
    
    class Meta:
        verbose_name = 'Subrace Granted Language'


class SubraceSpells(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SpellsSubrace")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="SubraceSpellsGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subrace.name} - {self.spells_granted.name}'
    
    class Meta:
        verbose_name = 'Subrace Granted Spell'

class SubraceTools(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="ToolsSubrace")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="SubraceToolProficiencyGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subrace.name} - {self.tool_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Subrace Granted Tool'


# CLASS


class ClassSkillProficiencies(models.Model):
    character_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, related_name="SkillProfsClass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="ClassSkillGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.character_class.name} - {self.skill_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Class Granted Skill'


class ClassLanguageProficiencies(models.Model):
    character_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, related_name="LanguagesClass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="ClassLanguageGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.character_class.name} - {self.language_granted.name}'

    class Meta:
        verbose_name = 'Class Granted Language'


class ClassSpellsGranted(models.Model):
    character_class = models.ForeignKey(ClassContentTable, on_delete=models.CASCADE, related_name="SpellsClass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="ClassSpellsGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.character_class.name} - {self.spells_granted.name}'

    class Meta:
        verbose_name = 'Class Granted Spell'



# SUBCLASSES

class SubclassSkillProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="SkillprofsSubclass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SubclassSkillGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subclass.name} - {self.skill_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Subclass Granted Skill'


class SubclassLanguageProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="LanguagesSubclass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="SubclassLanguageGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subclass.name} - {self.language_granted.name}'

    class Meta:
        verbose_name = 'Subclass Granted Language'


class SubclassSpellsGranted(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="SpellsSubclass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="SubclassSpellsGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.subclass.name} - {self.spells_granted.name}'

    class Meta:
        verbose_name = 'Subclass Granted Spell'


# BACKGROUND

class BackgroundSkillProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="SkillprofsBackground")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="backgroundSkillGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.background.name} - {self.skill_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Background Granted Skill'



class BackgroundToolProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="ToolsBackground")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="BackgroundToolProficiencyGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.background.name} - {self.tool_proficiency_granted.name}'

    class Meta:
        verbose_name = 'Background Granted Tool'


class BackgroundLanguageProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="LanguagesBackground")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="BackgroundLanguageGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.background.name} - {self.language_granted.name}'

    class Meta:
        verbose_name = 'Background Granted Language'


# CHARACTER 

class CharacterLanguages(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="LanguagesCharacter")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="CharacterLanguageGranted")

    def __str__(self):
        return f'ID: {self.id} - {self.character.character_name} - {self.language_granted.name}'

    class Meta:
        verbose_name = 'Character Language'
