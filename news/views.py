from django.shortcuts import get_object_or_404, render
from .serializers import NewsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from rest_framework import status  



@api_view(["GET"])
def list_news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_news(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_news(request, slug):
    news = get_object_or_404(News, slug=slug)
    serializer = NewsSerializer(news, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def retreive_news(request, slug):
    news = get_object_or_404(News, slug=slug)
    serializer = NewsSerializer(news)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete_news(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.delete()
    return Response("news has succesfully been deleted", status=status.HTTP_204_NO_CONTENT)




















# @api_view(["GET", "PUT", "DELETE"])
# def news_details(request, slug):
    # news = get_object_or_404(News, slug)
    # if request.method == "GET":
    #    serializer = NewsSerializer(news)
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PUT":
        # serializer = NewsSerializer(news, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "DELETE":
        # news.delete()
        # return Response(status=status.HTTP_204)
# 




