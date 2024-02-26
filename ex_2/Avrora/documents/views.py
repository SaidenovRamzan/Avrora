from django.shortcuts import redirect
from django.views import generic
from documents.models import Document
from django.urls import reverse_lazy

from documents.forms import DocumentForm


class DocumentListView(generic.ListView):
    model = Document
    template_name = "document_list.html"
    context_object_name = "documents"


class DocumentDetailView(generic.DetailView):
    model = Document
    template_name = "document_detail.html"
    context_object_name = "document"


class DocumentCreateView(generic.CreateView):
    model = Document
    template_name = "document_form.html"
    form_class = DocumentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.model.objects.create(user=request.user, file=form.cleaned_data["file"])
            return redirect("document_list")
        return self.form_invalid(form)


class DocumentUpdateView(generic.UpdateView):
    model = Document
    template_name = "document_form.html"
    fields = ["file"]


class DocumentDeleteView(generic.DeleteView):
    model = Document
    template_name = "document_confirm_delete.html"
    success_url = reverse_lazy("document_list")
