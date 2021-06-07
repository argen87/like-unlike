from audioop import reverse

from rest_framework import generics, permissions
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from knox.models import AuthToken
from django.http import HttpResponseRedirect

from .models import User, Post
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


@api_view(['GET'])
def api_overview_links(request):
    print(request.build_absolute_uri())
    urls = {
        'lists_social': 'list/',
        'create_social': 'create/',
        'register_social': 'api/register/',
        'login_social': 'api/login/',
        'logout_social': 'api/logout/',
    }
    for key in urls:
        urls[key] = request.build_absolute_uri() + urls[key]
    return Response(urls)


@api_view(['GET'])
def get_task_list(request):
    # '''retrieve all  task objects'''
    tasks = User.objects.all()
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)




@api_view(['PUT'])
def task_edit(request, pk):
    try:
        task = User.objects.get(id=pk)
        serializer = UserSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except User.DoesNotExist as error:
        print(error)
        raise Http404
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)





