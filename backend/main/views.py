from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ProductSerializer
from .models import Product


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return JsonResponse({
                "message": "ok",
                "user": user.username
            })

        return JsonResponse({"error": "invalid credentials"}, status=400)


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session.save()

            return JsonResponse({
                "message": "register success",
                "username": user.username,
            }, status=201)

        return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "only POST method allowed"}, status=405)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "logout success"}, status=200)



class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer