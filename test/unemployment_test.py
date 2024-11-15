from app.unemployment import fetch_unemployment_json


def test_data_fetching():

    data = fetch_unemployment_json()
    assert isinstance(data, list)
    assert len(data) > 900

    latest = data[0]
    assert isinstance(latest, dict)
    assert list(latest.keys()) == ["date", "value"]

    earliest = data[-1]
    assert earliest["date"] == '1948-01-01'
    assert earliest["value"] == 3.4