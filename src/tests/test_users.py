from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from user_management.models import SubProfile


class UserManagementTests(APITestCase):
    def setUp(self):
        """
        Configuration initiale avant chaque test.
        - Création d'un utilisateur principal.
        - Génération d'un token d'authentification.
        """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.user2 = User.objects.create_user(username="otheruser", password="password123")


    # --- Tests pour les utilisateurs ---
    def test_list_users(self):
        """
        Tester si la liste des utilisateurs est retournée correctement.
        """
        response = self.client.get('/api/user_management/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_create_user(self):
        """
        Tester la création d'un utilisateur via l'endpoint.
        """
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123"
        }
        response = self.client.post('/api/user_management/users/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(response.data['username'], "newuser")


    def test_update_user(self):
        """
        Tester la mise à jour d'un utilisateur existant.
        """
        data = {
            "email": "updatedemail@example.com"
        }
        response = self.client.put(f'/api/user_management/users/{self.user2.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.email, "updatedemail@example.com")


    def test_delete_user(self):
        """
        Tester la suppression d'un utilisateur.
        """
        response = self.client.delete(f'/api/user_management/users/{self.user2.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)


    # --- Tests pour les sous-profils ---
    def test_list_sub_profiles(self):
        """
        Tester si la liste des sous-profils liés à l'utilisateur connecté est retournée.
        """
        SubProfile.objects.create(user=self.user, username="SubProfile1")
        SubProfile.objects.create(user=self.user, username="SubProfile2")

        response = self.client.get('/api/user_management/subprofiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_create_sub_profile(self):
        """
        Tester la création d'un sous-profil.
        """
        data = {"username": "NewSubProfile"}
        response = self.client.post('/api/user_management/subprofiles/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubProfile.objects.count(), 1)
        self.assertEqual(response.data['username'], "NewSubProfile")


    def test_update_sub_profile(self):
        """
        Tester la mise à jour d'un sous-profil existant.
        """
        sub_profile = SubProfile.objects.create(user=self.user, username="OldSubProfile")
        data = {"username": "UpdatedSubProfile"}
        response = self.client.put(f'/api/user_management/subprofiles/{sub_profile.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sub_profile.refresh_from_db()
        self.assertEqual(sub_profile.username, "UpdatedSubProfile")


    def test_delete_sub_profile(self):
        """
        Tester la suppression d'un sous-profil.
        """
        sub_profile = SubProfile.objects.create(user=self.user, username="SubProfileToDelete")
        response = self.client.delete(f'/api/user_management/subprofiles/{sub_profile.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SubProfile.objects.count(), 0)
