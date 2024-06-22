from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data["status"] = "error"
        response.data["response_code"] = "99"

    return response


@method_decorator(csrf_exempt, name="dispatch")
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        """Method to list all the items in the store"""
        try:
            items = self.get_queryset()
            serializer = self.get_serializer(items, many=True)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (ParseError, PermissionDenied, ValidationError) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, *args, **kwargs):
        """Method to retrieve a single item from the store"""
        try:
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (
            ObjectDoesNotExist,
            Http404,
            NotFound,
            ParseError,
            ValidationError,
            PermissionDenied,
        ) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

    def create(self, request, *args, **kwargs):
        """Method to add an item to the store"""
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except (ValidationError, ParseError, PermissionDenied) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        """Method to modify an existing item record in the store"""
        try:
            item = self.get_object()
            serializer = self.get_serializer(item, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (
            ObjectDoesNotExist,
            ValidationError,
            Http404,
            ParseError,
            NotFound,
            PermissionDenied,
        ) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, *args, **kwargs):
        """Method to remove a particular item from the store"""
        try:
            item = self.get_object()
            self.perform_destroy(item)
            return Response(
                {"status": "success", "response_code": "00"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except (ObjectDoesNotExist, Http404, NotFound, PermissionDenied) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )


@method_decorator(csrf_exempt, name="dispatch")
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        """Method to list all the suppliers in the store"""
        try:
            suppliers = self.get_queryset()
            serializer = self.get_serializer(suppliers, many=True)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, *args, **kwargs):
        """Method to retrieve a single supplier in the store"""
        try:
            supplier = self.get_object()
            serializer = self.get_serializer(supplier)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (
            ObjectDoesNotExist,
            Http404,
            NotFound,
            ParseError,
            ValidationError,
            PermissionDenied,
        ) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

    def create(self, request, *args, **kwargs):
        """Method to add a supplier to the store"""
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except (ValidationError, ParseError, PermissionDenied) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        """Method to update a particular supplier's record in the store"""
        try:
            supplier = self.get_object()
            serializer = self.get_serializer(supplier, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (
            ObjectDoesNotExist,
            ValidationError,
            Http404,
            ParseError,
            NotFound,
            PermissionDenied,
        ) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, *args, **kwargs):
        """Method to remove a particular supplier's record from the store"""
        try:
            supplier = self.get_object()
            self.perform_destroy(supplier)
            return Response(
                {"status": "success", "response_code": "00"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except (ObjectDoesNotExist, Http404, NotFound, PermissionDenied) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )


class SuppliersForItemApiView(generics.GenericAPIView):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        item = Item.objects.get(pk=pk)
        return item.suppliers.all()

    def get(self, request, *args, **kwargs):
        """Method to retrieve the suppliers of a particular item"""
        try:
            suppliers = self.get_queryset()
            serializer = self.get_serializer(suppliers, many=True)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except (ParseError, PermissionDenied, ValidationError) as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ItemForSupplierApiView(generics.GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = []

    def get_queryset(self):
        pk = self.kwargs["pk"]
        supplier = Supplier.objects.get(pk=pk)
        return supplier.items.all()

    def get(self, request, *args, **kwargs):
        """Method to retrieve items belonging to a particular supplier"""
        try:
            items = self.get_queryset()
            serializer = self.get_serializer(items, many=True)
            return Response(
                {
                    "status": "success",
                    "response_code": "00",
                    "response": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            return Response(
                {"status": "error", "response_code": "99", "response": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
