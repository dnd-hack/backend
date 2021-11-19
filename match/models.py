from django.db import models

# Create your models here.
from accounts.models import User


class Group(models.Model):
    GRADE = (
        (1, '아이언'),
        (2, '브론즈'),
        (3, '실버'),
        (4, '골드'),
        (5, '플래티넘'),
        (6, '다이아'),
        (7, '마스터'),
        (8, '그랜드마스터'),
        (9, '챌린저'),
    )
    TEAM = (
            (1, 'DWF_KIA'),
            (2, 'T1'),
            (3, 'Gen_G'),
            (4, 'NongShim_REDFORCE'),
            (5, 'Liiv_SANDBOX'),
            (6, 'Afreeca Freecs'),
            (7, 'kt Rolster'),
            (8, 'Hanwha_Life_Esports'),
            (9, 'Fredit_BRION'),
            (10, 'DRX')
    )
    AGE_RANGE = (
        (1, '10대'),
        (2, '20대'),
        (3, '30대'),
        (4, '40대'),
        (5, '50대'),
    )
    title = models.CharField(help_text="모임 제목", max_length=30)
    content = models.CharField(help_text="모임 내용", max_length=200)
    url = models.URLField(max_length=200)
    grade = models.IntegerField(choices=GRADE, blank=True, null=True)
    age_range = models.IntegerField(choices=AGE_RANGE, blank=True, null=True)
    cheer = models.IntegerField(choices=TEAM, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    organizer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='matches')

    def __str__(self):
        return self.title


class JoinedMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()

