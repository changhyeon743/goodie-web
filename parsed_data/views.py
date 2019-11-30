from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core import serializers
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Video
from .serializers import VideoSerializer

from collections import Counter,OrderedDict
from django.views.generic import ListView

class BaseView(ListView):
    template_name = 'parsed_data/trending.html'
    context_object_name = 'video_list'
    queryset = {
        'published':Video.objects.order_by('-publishedDate'),
        'most_liked':Video.objects.order_by('-likeCount'),
        'well_community':Video.objects.order_by('-commentCount'),
        'random':Video.objects.order_by('?'),
        'trending':Video.objects.order_by('?')
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-createdDate')
    serializer_class = VideoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    @action(detail=False)
    def get_tags(self, request):
        tags = Video.objects.values_list('tags',flat=True)
        tags_list = list()
        for i in tags:
            for j in i.split(','):
                tags_list.append(j)
        res = sorted(Counter(tags_list).items(), key=(lambda x: x[1]), reverse = True)[:10]
        
        return Response(dict(res))

    @action(detail=False)
    def get_random(self,request):
        videos = Video.objects.order_by('?').values()[:10]
        return Response(videos)

    @action(detail=False)
    def sort_like(self,request):
        videos = Video.objects.order_by('-likeCount').values()[:10]
        return Response(videos)

    @action(detail=False)
    def sort_view(self,request):
        videos = Video.objects.order_by('-viewCount').values()[:10]
        return Response(videos)
    
    @action(detail=False)
    def sort_comment(self,request):
        videos = Video.objects.order_by('-commentCount').values()[:10]
        return Response(videos)
    
# def videos(request):
#     videos = Video.objects.all().order_by('-createdDate')[:5]
#     video_list = serializers.serialize('json', videos)
#     return HttpResponse(video_list, content_type="text/json-comment-filtered")

