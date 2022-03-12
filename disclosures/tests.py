import json
import unittest
from typing import Any

import requests


def make_file(filename) -> Any:
    filepath = f"/opt/app/disclosures/test_assets/{filename}"
    with open(filepath, "rb") as f:
        return {"file": (filename, f.read())}


class DisclosureTest(unittest.TestCase):
    def test_heartbeat(self):
        """"""
        response = requests.post("http://disclosures:5050/")
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertEqual(response.text, "Heartbeat detected.", msg="Failed response.")

    def test_disclosures(self):
        """"""
        files = make_file(filename="simple-disclosure.pdf")
        response = requests.post("http://disclosures:5050/simple/", files=files)
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertTrue(response.json()["success"], msg="Extraction failed")
        self.assertEqual(
            response.json()["sections"]["Positions"]["rows"][0]["Position"]["text"],
            "Life Trustee",
            msg=f"{response.json()}",
        )
        self.assertEqual(
            response.json()["sections"]["Positions"]["rows"][0]["Name of Organization"][
                "text"
            ],
            "Bridgewater College",
            msg=f"{response.json()}",
        )

    def test_jef_disclosure(self):
        """"""
        files = make_file(filename="JEF-disclosure.pdf")
        response = requests.post("http://disclosures:5050/jef/", files=files)
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertTrue(response.json()["success"], msg="Extraction failed")

    def test_jw_disclosure(self):
        """"""
        files = make_file(filename="JW-disclosure.pdf")
        response = requests.post("http://disclosures:5050/jw/", files=files)
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertTrue(response.json()["success"], msg="Extraction failed")

    def test_scanned_disclosure(self):
        """"""
        files = make_file(filename="image-disclosure.pdf")
        response = requests.post("http://disclosures:5050/scan/", files=files)
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertTrue(response.json()["success"], msg="Extraction failed")


if __name__ == "__main__":
    unittest.main()
