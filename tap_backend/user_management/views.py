from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .models import SubProfile
from .serializers import UserSerializer, SubProfileSerializer


# --- Utilisateurs ---
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur introuvable'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'message': 'Utilisateur supprimé'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur introuvable'}, status=status.HTTP_404_NOT_FOUND)


# --- Sous-profils ---
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_sub_profiles(request):
    sub_profiles = SubProfile.objects.filter(user=request.user)
    serializer = SubProfileSerializer(sub_profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sub_profile(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = SubProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_sub_profile(request, subprofile_id):
    try:
        sub_profile = SubProfile.objects.get(id=subprofile_id, user=request.user)
        serializer = SubProfileSerializer(sub_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except SubProfile.DoesNotExist:
        return Response({'error': 'Sous-profil introuvable'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_sub_profile(request, subprofile_id):
    try:
        sub_profile = SubProfile.objects.get(id=subprofile_id, user=request.user)
        sub_profile.delete()
        return Response({'message': 'Sous-profil supprimé'}, status=status.HTTP_204_NO_CONTENT)
    except SubProfile.DoesNotExist:
        return Response({'error': 'Sous-profil introuvable'}, status=status.HTTP_404_NOT_FOUND)
