from disclosure_extractor import (
    extract_vector_pdf,
    process_jef_document,
    extract_financial_document,
    process_judicial_watch,
)
import pdfplumber

from django.http import HttpResponse, JsonResponse

from disclosures.forms import DocumentForm
from disclosures.utils import cleanup_form



def heartbeat(request):
    """Heartbeat endpoint

    :param request:
    :return:
    """
    return HttpResponse(f"Heartbeat detected.")


def simple_disclosure(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_vector_pdf(form.cleaned_data["fp"])
    cleanup_form(form)
    return JsonResponse(output)


def JEF_disclosure(request):
    """Extract content from a JEF generated financial disclosure.

    Extract content from a financial record that was generated using the new
    JEF system being rolled out by the AO.

    :return: Disclosure information
    """
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    financial_record_data = process_jef_document(file_path=form.cleaned_data["fp"])
    cleanup_form(form)
    return JsonResponse(financial_record_data)


def JW_disclosure(request):
    """Extract content from a JEF generated financial disclosure.

    Extract content from a financial record that was generated using the new
    JEF system being rolled out by the AO.

    :return: Disclosure information
    """
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    financial_record_data = process_judicial_watch(file_path=form.cleaned_data["fp"])
    cleanup_form(form)
    return JsonResponse(financial_record_data)


def scan_disclosure(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})

    financial_record_data = extract_financial_document(
        file_path=form.cleaned_data["fp"],
        show_logs=True,
        resize=True,
    )
    cleanup_form(form)
    return JsonResponse(financial_record_data)


def identify_disclosure(request):
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})

    with pdfplumber.open(form.cleaned_data["fp"]) as pdf:
        if pdf.pages[0].width > pdf.pages[0].height:
            if "JEFS" in pdf.pages[0].extract_text():
                response = process_jef_document(file_path=form.cleaned_data["fp"])
            else:
                response = {"success": False, "message": "Unknown document type"}
        else:
            response = extract_vector_pdf(form.cleaned_data["fp"])
            if not response['success']:
                response = extract_financial_document(
                    file_path=form.cleaned_data["fp"],
                    show_logs=False,
                    resize=True,
                )
    cleanup_form(form)
    return JsonResponse(response)