from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from documents.forms import DocumentForm
from documents.models import Document
from documents.permissions import IsAuthorOrSuperuser


class DocumentListView(LoginRequiredMixin, generic.ListView):
    model = Document
    template_name = "document_list.html"
    context_object_name = "documents"

    def get_queryset(self) -> QuerySet[Document]:
        user = self.request.user
        return Document.objects.filter(user=user)


class DocumentDetailView(IsAuthorOrSuperuser, generic.DetailView):
    model = Document
    template_name = "document_detail.html"
    context_object_name = "document"


class DocumentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Document
    template_name = "document_form.html"
    form_class = DocumentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.model.objects.create(user=request.user, **form.cleaned_data)
            return redirect("document_list")
        return self.form_invalid(form)


class DocumentUpdateView(IsAuthorOrSuperuser, generic.UpdateView):
    model = Document
    template_name = "document_form.html"
    form_class = DocumentForm

    def get_success_url(self):
        return reverse_lazy("document_list")


class DocumentDeleteView(IsAuthorOrSuperuser, generic.DeleteView):
    model = Document
    success_url = reverse_lazy("document_list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("document_list")
