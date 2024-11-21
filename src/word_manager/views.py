from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import WordList, Word
from .serializers import WordListSerializer, WordSerializer
from tap_backend.permissions import IsOwner


class WordListViewSet(viewsets.ModelViewSet):
    """
    Vue permettant de créer, lire, modifier et supprimer des listes de mots.
    Seuls les propriétaires peuvent modifier ou supprimer leurs propres listes.
    """
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer

    def get_permissions(self):
        """
        Définit les permissions
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        """
        Associe automatiquement l'utilisateur connecté comme propriétaire de la liste.
        """
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        """
        Vérifie que l'utilisateur est le propriétaire avant de supprimer une liste.
        """
        if instance.owner != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à supprimer cette liste de mots.")
        instance.delete()

    def perform_update(self, serializer):
        """
        Vérifie que l'utilisateur est le propriétaire avant de mettre à jour une liste.
        """
        if serializer.instance.owner != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à modifier cette liste de mots.")
        serializer.save()


class WordViewSet(viewsets.ModelViewSet):
    """
    Vue permettant de gérer les mots individuels (CRUD).
    Aucune restriction sur l'accès pour le moment.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer

