from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from match.models import Group, JoinedMember
from match.serializers import GroupSerializer, JoinedMemberSerializer

def filterNone(request, data):
    try:
        return request[data]
    except:
        return None

class GroupViewSet (ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['post', 'get']

class JoinMember (APIView):
    def post(self, request):
        user = filterNone(request.data, 'user')
        if (user):
            user = User.objects.get(user_id=user)
        group = filterNone(request.data, 'group')
        if (group):
            group = Group.objects.get(id=group)
        JoinedMember.objects.create(user=user,
                                    group=group)
        return Response({"open_link":group.url})


class MatchList(APIView):
    def post(self, request):
        try:
            user_id = request.data['user_id']
        except:
            user_id = ""
        group_list = []
        group_queryset = Group.objects.all().order_by('-created_at')
        for group in group_queryset:
            group_list.append({
                "group_id" : group.id,
                "title": group.title,
                "content": group.content,
                "url": group.url,
                "grade": group.grade,
                "age_range": group.age_range,
                "cheer": group.cheer,
                "gender": group.gender,
                "created_at": group.created_at.strftime(("%Y년 %m월 %d일")),
                "organizer": group.organizer.user_id,
                "joined_member_num" : group.joined_member_num(),
                "status": group.is_joined(user_id)
            })

        return Response(group_list)

class FilterMatch(APIView):
    def get(self, request):
        # try:
        group_queryset = Group.objects.all()
        user_id=request.GET.get('user_id', '')
        grade=request.GET.get('grade', 0)
        age_range=request.GET.get('age_range', 0)
        cheer=request.GET.get('cheer', 0)
        gender=request.GET.get('gender', 0)
        if (grade):
            group_queryset = group_queryset.filter(grade=grade)
        if (age_range):
            group_queryset = group_queryset.filter(age_range=age_range)
        if (cheer):
            group_queryset = group_queryset.filter(cheer=cheer)
        if (gender):
            group_queryset = group_queryset.filter(gender=gender)

        group_list = []
        for group in group_queryset:
            group_list.append({
                "group_id" : group.id,
                "title": group.title,
                "content": group.content,
                "url": group.url,
                "grade": group.grade,
                "age_range": group.age_range,
                "cheer": group.cheer,
                "gender": group.gender,
                "created_at" :group.created_at.strftime(("%Y년 %m월 %d일")),
                "organizer": group.organizer.username,
                "joined_member_num" : group.joined_member_num(),
                "status": group.is_joined(user_id)
            })

        return Response(group_list)

