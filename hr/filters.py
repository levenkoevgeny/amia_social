import django_filters
from institution.models import Institution, Vacancy
from social_profile.models import SocialProfile, Language, Skill


LEVELS = (
    (1, 'Beginner'),
    (2, 'Pre-Intermediate'),
    (3, 'Intermediate'),
    (4, 'Upper-Intermediate'),
    (5, 'Advanced'),
    (6, 'Proficiency'),
)


class VacancyFilter(django_filters.FilterSet):

    institution = django_filters.ModelMultipleChoiceFilter(queryset=Institution.objects.all())
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all())
    language = django_filters.ModelChoiceFilter(field_name='languages__languagewithlevelvacancy__language',
                                                queryset=Language.objects.all())
    language_level = django_filters.ChoiceFilter(field_name='languages__languagewithlevelvacancy__level',
                                                 choices=LEVELS)

    class Meta:
        model = Vacancy
        fields = [
            'skills',
            'languages',
            'institution',
        ]


class ProfileFilter(django_filters.FilterSet):

    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all())
    language = django_filters.ModelChoiceFilter(field_name='languages__languagewithlevel__language',
                                                queryset=Language.objects.all())
    language_level = django_filters.ChoiceFilter(field_name='languages__languagewithlevel__level',
                                                 choices=LEVELS)

    class Meta:
        model = SocialProfile
        fields = [
            'skills',
        ]