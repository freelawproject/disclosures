from django.urls import path

from disclosures.views import (
    heartbeat,
    simple_disclosure,
    JEF_disclosure,
    JW_disclosure,
    scan_disclosure,
    identify_disclosure,
)

urlpatterns = [
    path(
        "",
        heartbeat,
        name="heartbeat-disclosure",
    ),
    path(
        "simple/",
        simple_disclosure,
        name="simple-disclosure",
    ),
    path(
        "jef/",
        JEF_disclosure,
        name="jef-disclosure",
    ),
    path(
        "extract/judical-watch/",
        JW_disclosure,
        name="jw-disclosure",
    ),
    path(
        "scan/",
        scan_disclosure,
        name="scan-disclosure",
    ),
    path(
        "extract/disclosure/",
        identify_disclosure,
        name="identify-disclosure",
    )
    # path(
    #     "disclosures/images-to-pdf/",
    #     images_to_pdf,
    #     name="images-to-pdf",
    # ),
]
