import json
from unittest import mock

import pytest


@pytest.mark.asyncio
async def test_create_observation_ok(api_client, observations_endpoint, species):
    resp = await api_client.post(path=observations_endpoint, data={
        'species_id': species.id,
        'timestamp': '2022-10-17 05:51',
        'latitude': 55.0,
        'longitude': 85.0,
    })

    assert resp.status == 200
    assert json.loads(await resp.text()) == {
        'id': mock.ANY,
        'species': species.id,
        'timestamp': '2022-10-17T05:51:00',
        'latitude': 55.0,
        'longitude': 85.0,
    }


@pytest.mark.asyncio
async def test_create_observation_bad_request(api_client, observations_endpoint, species):
    resp = await api_client.post(path=observations_endpoint, data={
        'species_id': species.id,
        'timestamp': 'text',
        'latitude': 58.0,
        'longitude': 85.0,
    })

    assert resp.status == 400
    assert 'invalid datetime format' in await resp.text()
