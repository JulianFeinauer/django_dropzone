import uuid

from django.core.files.uploadedfile import TemporaryUploadedFile
from django.http.response import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from django_dropzone.models import UploadedFile


class DropzoneIndex(TemplateView):
    template_name = "django_dropzone/index.html"


class UploadView(View):
    def post(self, request):
        print(f"Hallo: {request.FILES}")
        file: TemporaryUploadedFile = request.FILES["file"]

        filename = file.name
        file.name = str(uuid.uuid4()) + "." + file.name.split(".")[-1]

        instance = UploadedFile(filename=filename, file=file)
        instance.save()

        return JsonResponse({"filename": instance.filename, "url": instance.file.url})
