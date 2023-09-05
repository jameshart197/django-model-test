from django.db import models
from django.contrib.auth.models import User

# top level models


class CharacterDetails(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=SET_NULL, related_name="race")
    alignment = models.ForeignKey(AlignmentContentTable, on_delete=SET_NULL, related_name="alignment")
    background = models.ForeignKey(BackgroundContentTable, on_delete=SET_NULL, related_name="background")
    languages = models.ForeignKey(LanguageContentTable, on_delete=SET_NULL, related_name="languages")  # can be multiple entries?
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
    spell = models.ForeignKey(SpellID, on_delete=SET_NULL, related_name="spell name")


class CharacterLevels(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=CASCADE, related_name="character")
    subclass = models.ForeignKey(SubClassContentTable, on_delete=SET_NULL, related_name="subclass")
    level = models.IntegerField(max_length=2)


class CharacterSavingThrows(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=CASCADE, related_name="character")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=SET_NULL, related_name="governing attribute")


class CharacterSkillProficiencies(models.Model):
    PROFIENCY_LEVEL = (
        (0, "Proficient"), 
        (1, "Expertise"), 
        (2, "Half-Proficiency (Bard)")
        )
    character = models.ForeignKey(CharacterDetails, on_delete=CASCADE, related_name="character")
    skill = models.ForeignKey(SkillContentTable, on_delete=SET_NULL, related_name="skill")
    proficiency_level = models.IntegerField(choices=PROFICIENCY_LEVEL)


class CharacterAttributes(models.Model):
    character = models.ForeignKey(CharacterDetails, on_delete=CASCADE, related_name="character")
    attribute = models.ForeignKey(AttributeContentTable, on_delete=SET_NULL, related_name="attribute")
    score = models.IntegerField(max_length=2)


# Content Models

class SkillsContentTable(models.Model):
    attribute = models.ForeignKey(AttributeContentTable, on_delete=SET_NULL, related_name="governing attribute")
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)


class AttributeContentTable(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=5)
    full_description = models.CharField(max_length=400)


class RaceContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class SubRaceContentTable(models.Model):
    race = models.ForeignKey(RaceContentTable, on_delete=CASCADE, related_name="race")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class SpellsContentTable(models.Model):
    SPELL_REQUIREMENTS = (
        (0, ""), 
        (1, "Verbal"), 
        (2, "Somatic"), 
        (3, "Material"), 
        (4, "Verbal and Material"), 
        (5, "Somatic and Material"), 
        (6, "Verbal and Somatic"), 
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
    parent_class = models.ForeignKey(ClassContentTable, on_delete=CASCADE, related_name="class")
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class LanguageContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)


class BackgroundContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)
    feature = models.CharField(500)


class AlignmentContentTable(models.Model):
    name = models.CharField(max_length=100)
    full_description = models.CharField(max_length=400)


class ToolContentTable(models.Model):
    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=1000)

# Link Models

#SUBRACE

class SubraceToSkillProficiencies(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="subrace")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=SET_NULL, related_name="skill granted")


class SubraceLanguages(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="subrace")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=SET_NULL, related_name="language granted")


class SubraceSpells(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="subrace")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=SET_NULL, related_name="spells granted")


class SubraceTools(models.Model):
    subrace = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="subrace")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=SET_NULL, related_name="tool proficiency granted")


# CLASS


class ClassSkillProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="class")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=SET_NULL, related_name="skill granted")


class ClassLanguageProficiencies(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="class")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=SET_NULL, related_name="language granted")


class ClassSpellsGranted(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="class")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=SET_NULL, related_name="spells granted")


class ClassSavingThrows(models.Model):
    character_class = models.ForeignKey(SubRaceContentTable, on_delete=CASCADE, related_name="class")
    saving_throws_granted = models.ForeignKey(CharacterSavingThrows, on_delete=SET_NULL, related_name="saving throws granted")


# SUBCLASSES

class SubclassSkillProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=CASCADE, related_name="subclass")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=SET_NULL, related_name="skill granted")


class SubclassLanguageProficiencies(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=CASCADE, related_name="subclass")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=SET_NULL, related_name="language granted")


class SubclassSpellsGranted(models.Model):
    subclass = models.ForeignKey(SubClassContentTable, on_delete=CASCADE, related_name="subclass")
    spells_granted = models.ForeignKey(SpellsContentTable, on_delete=SET_NULL, related_name="spells granted")


# BACKGROUND

class BackgroundClassSkillProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=CASCADE, related_name="background")
    skill_proficiency_granted = models.ForeignKey(SkillsContentTable, on_delete=SET_NULL, related_name="skill granted")


class SubclassLanguageProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=CASCADE, related_name="background")
    tool_proficiency_granted = models.ForeignKey(ToolContentTable, on_delete=SET_NULL, related_name="tool proficiency granted")


class BackgroundToolProficiencies(models.Model):
    background = models.ForeignKey(BackgroundContentTable, on_delete=CASCADE, related_name="background")
    language_granted = models.ForeignKey(LanguageContentTable, on_delete=SET_NULL, related_name="language granted")
