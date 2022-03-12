from disclosure_extractor import (
    extract_vector_pdf,
    process_jef_document,
    extract_financial_document,
    process_judicial_watch,
)

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


#
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


# def images_to_pdf(request):
#     """
#
#     :param request:
#     :return:
#     """
#     form = ImagePdfForm(request.POST)
#     if not form.is_valid():
#         return JsonResponse({"success": False})
#     sorted_urls = form.cleaned_data["sorted_urls"]
#
#     if len(sorted_urls) > 1:
#         image_list = download_images(sorted_urls)
#         with NamedTemporaryFile(suffix=".pdf") as tmp:
#             with open(tmp.name, "wb") as f:
#                 f.write(img2pdf.convert(image_list))
#             cleaned_pdf_bytes = strip_metadata_from_path(tmp.name)
#     else:
#         tiff_image = Image.open(
#             requests.get(sorted_urls[0], stream=True, timeout=60 * 5).raw
#         )
#         pdf_bytes = convert_tiff_to_pdf_bytes(tiff_image)
#         cleaned_pdf_bytes = strip_metadata_from_bytes(pdf_bytes)
#     return HttpResponse(cleaned_pdf_bytes, content_type="application/pdf")
