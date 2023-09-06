from django.db import models
from .contentmodels import *

# top level models


class CharacterDetails(models.Model):
    race = models.ForeignKey(SubRaceContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterSubrace")
    alignment = models.ForeignKey(AlignmentContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterAlignment")
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterBackground")
    languages = models.ForeignKey(LanguageContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="CharacterLanguages")  # to be separate table?
    character_name = models.CharField(max_length=200)
    inspiration = models.BooleanField
    faith = models.CharField(max_length=200)
    age = models.IntegerField  # range limit 1-9999?
    height = models.CharField(max_length=4)
    weight = models.IntegerField  # range limit 1-999
    notes = models.CharField(max_length=1000)
    backstory = models.CharField(max_length=10000)
    allies = models.CharField(max_length=200)
    enemies = models.CharField(max_length=200)
    factions_and_orgs = models.CharField(max_length=200)
    hit_points = models.IntegerField  # range limit 1-999
    armor_class = models.IntegerField  # range limit 1-50

    def __str__(self):
        return f'{self.character_name}'


class CharacterSpells(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SpellsCharacter")
    spell = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="CharacterSpells")

    def __str__(self):
        return f'{self.character} {self.spell}'


class CharacterLevels(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="LevelsCharacter")
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.SET_DEFAULT, default=0, related_name="LevelsSubclass")
    level = models.IntegerField  # range limit 1-20


class CharacterSavingThrows(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SavingThrowsCharacter")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, related_name="SavingThrowsGoverningAttribute")


class CharacterSkillProficiencies(models.Model):
    PROFICIENCY_LEVEL = (
        (0, "Proficient"),
        (1, "Expertise"),
        (2, "Half-Proficiency (Bard)")
        )
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="SkillsCharacter")
    skill = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SkillsSkill")
    proficiency_level = models.IntegerField(choices=PROFICIENCY_LEVEL)


class CharacterAttributes(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=models.CASCADE, related_name="AttributesCharacter")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=models.CASCADE, related_name="AttributesAttribute")
    score = models.IntegerField  # range limit 1-30


# Link Models

#SUBRACE

class SubraceToSkillProficiencies(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SkillprofsSubrace")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SubraceSkillGranted")


class SubraceLanguages(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="LanguagesSubrace")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="SubraceLanguageGranted")


class SubraceSpells(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SpellsSubrace")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="SubraceSpellsGranted")


class SubraceTools(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="ToolsSubrace")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="SubraceToolProficiencyGranted")


# CLASS


class ClassSkillProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SkillProfsClass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="ClassSkillGranted")


class ClassLanguageProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="LanguagesClass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="ClassLanguageGranted")


class ClassSpellsGranted(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SpellsClass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="ClassSpellsGranted")


class ClassSavingThrows(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=models.CASCADE, related_name="SavingThrowsClass")
    saving_throws_granted = models.ForeignKey(CharacterSavingThrows, on_delete=models.CASCADE, related_name="ClassSavingThrowsGranted")


# SUBCLASSES

class SubclassSkillProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="SkillprofsSubclass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="SubclassSkillGranted")


class SubclassLanguageProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="LanguagesSubclass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="SubclassLanguageGranted")


class SubclassSpellsGranted(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=models.CASCADE, related_name="SpellsSubclass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=models.CASCADE, related_name="SubclassSpellsGranted")


# BACKGROUND

class BackgroundSkillProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="SkillprofsBackground")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=models.CASCADE, related_name="backgroundSkillGranted")


class BackgroundToolProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="ToolsBackground")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=models.CASCADE, related_name="BackgroundToolProficiencyGranted")


class BackgroundLanguageProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=models.CASCADE, related_name="LanguagesBackground")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=models.CASCADE, related_name="BackgroundLanguageGranted")
