

docker exec -it mock_courtlistener_disclosures python3 -m unittest disclosures.tests.DisclosureTest.test_disclosures


docker-compose -f docker-compose.dev.yml up --build -d