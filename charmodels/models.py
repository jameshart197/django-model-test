from django.db import models
from .contentmodels import *

# top level models


class CharacterDetails(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="race")
    alignment = models.ForeignKey(AlignmentContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="alignment")
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="background")
    languages = models.ForeignKey(LanguageContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="languages")  # can be multiple entries?
    character_name = models.CharField(max_length=200)
    inspiration = models.BooleanField
    faith = models.CharField(max_length=200)
    age = models.IntegerField(max_length=5)
    height = models.CharField(max_length=4)
    weight = models.IntegerField(max_length=4)
    notes = models.CharField(max_length=1000)
    backstory = models.CharField(max_length=10000)
    allies = models.CharField(max_length=200)
    enemies = models.CharField(max_length=200)
    factions_and_orgs = models.CharField(max_length=200)
    hit_points = models.IntegerField(max_length=3)
    armor_class = models.IntegerField(max_length=2)


class CharacterSpells(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="character")
    spell = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="spell name")


class CharacterLevels(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="character")
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="subclass")
    level = models.IntegerField(max_length=2)


class CharacterSavingThrows(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="character")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, related_name="governing attribute")


class CharacterSkillProficiencies(models.Model):
    PROFICIENCY_LEVEL = (
        (0, "Proficient"),
        (1, "Expertise"),
        (2, "Half-Proficiency (Bard)")
        )
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="character")
    skill = models.ForeignKey(SkillsContentTable, on_delete=models.SET_NULL, related_name="skill")
    proficiency_level = models.IntegerField(choices=PROFICIENCY_LEVEL)


class CharacterAttributes(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="character")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.SET_NULL, related_name="attribute")
    score = models.IntegerField(max_length=2)


# Content Models


# Link Models

#SUBRACE

class SubraceToSkillProficiencies(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="subrace")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="skill granted")


class SubraceLanguages(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="subrace")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="language granted")


class SubraceSpells(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="subrace")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="spells granted")


class SubraceTools(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="subrace")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="tool proficiency granted")


# CLASS


class ClassSkillProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="class")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="skill granted")


class ClassLanguageProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="class")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="language granted")


class ClassSpellsGranted(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="class")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="spells granted")


class ClassSavingThrows(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="class")
    saving_throws_granted = models.ForeignKey(CharacterSavingThrows, on_delete=models.CASCADE, related_name="saving throws granted")


# SUBCLASSES

class SubclassSkillProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="subclass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="skill granted")


class SubclassLanguageProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="subclass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="language granted")


class SubclassSpellsGranted(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="subclass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="spells granted")


# BACKGROUND

class BackgroundSkillProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="background")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="skill granted")


class BackgroundToolProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="background")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="tool proficiency granted")


class BackgroundLanguageProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="backgroundtolangaage")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="background language granted")
