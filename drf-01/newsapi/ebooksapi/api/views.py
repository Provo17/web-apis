from rest_framework import generics
from rest_framework import mixins
# from rest_framework import permissions
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404

from ebooksapi.models import Ebook
# from ebooksapi.api.pagination import SmallSetPagination
# from ebooksapi.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooksapi.api.serializers import EbookSerializer

class EbookListCreateAPIView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
