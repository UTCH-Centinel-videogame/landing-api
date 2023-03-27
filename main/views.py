from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class VoteViewSet(ModelViewSet):
    queryset=Vote.objects.all()
    serializer_class=VoteSerializer
    
    @action(detail=False, methods=['get'])
    def average(self, request):
        votes = Vote.objects.all()
        num_votes = len(votes)
        avg_gameplay = sum([vote.gameplay for vote in votes]) / num_votes
        avg_music = sum([vote.music for vote in votes]) / num_votes
        avg_art = sum([vote.art for vote in votes]) / num_votes
        avg_story = sum([vote.story for vote in votes]) / num_votes
        avg_difficulty = sum([vote.difficulty for vote in votes]) / num_votes
        data = {
            'gameplay': avg_gameplay,
            'music': avg_music,
            'art': avg_art,
            'story': avg_story,
            'difficulty': avg_difficulty
        }
        return Response(data)