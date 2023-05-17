from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import PostSerializer, ViewLogSerializer, SearchLogSerializer, EmployeeSerializer
from .models import Post, Employee, ViewLog, SearchLog

from .service.recommandImpl import RecommandImpl
# Create your views here.


class DetailEmployee(APIView):
    def get(self, request, emp_id):
        emp = Employee.objects.get(emp_id=emp_id)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)


class ListPost(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)


class DetailPost(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(post_id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class SearchPost(APIView):
    def get(self, request):
        #To Do : 여러 컬럼 탐색 필요
        post = Post.objects.filter(department="설비기술연구소")
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)


class RecommandByJob(APIView):
    def get(self, request):
        emp_id = "test_id"
        user = Employee.objects.get(emp_id=emp_id)
        posts = [{i.post_id: [i.tags, i.contents]} for i in Post.objects.all()]
        recommand_post_id = RecommandImpl().recommand(user.job, posts)
        serializer = PostSerializer(Post.objects.filter(post_id__in=recommand_post_id), many=True)
        return Response(serializer.data)


class RecommandByViewLog(APIView):
    def get(self, request):
        emp_id = "test_id"
        user = Employee.objects.filter(emp_id=emp_id)[0]
        # view_log = ViewLog.objects.values("")
        pass

    def post(self, request):
        """example
            request.data(json, immutable) : 
                {
                    "post_id":["1"],
                    "emp_id":["test_id"],
                    "cate_id": ["1"]
                }
        """
        serializer = ViewLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecommandBySearchLog(APIView):
    def get(self, request):
        emp_id = "test_id"
        user = Employee.objects.get(emp_id=emp_id)
        pass

    def post(self, request):
        """example
            request.data(json, immutable) : 
                {
                    "emp_id":["test_id"],
                    "keyword":"SW"
                }
        """
        serializer = SearchLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecommandByFollow(APIView):
    def get(self, request):
        emp_id = "test_id"
        user = Employee.objects.filter(emp_id=emp_id)[0]
        pass
