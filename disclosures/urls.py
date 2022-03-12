from django.urls import path

from disclosures.views import (
    heartbeat,
    simple_disclosure,
    JEF_disclosure,
    JW_disclosure,
    scan_disclosure,
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
        "jw/",
        JW_disclosure,
        name="jw-disclosure",
    ),
    path(
        "scan/",
        scan_disclosure,
        name="scan-disclosure",
    )
    # path(
    #     "disclosures/images-to-pdf/",
    #     images_to_pdf,
    #     name="images-to-pdf",
    # ),
]
