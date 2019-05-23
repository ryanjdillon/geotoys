
def test_sentineldl_geojson_bb():
    from geotoys.sentinel import SentinelDL
    from shapely.geometry import Polygon

    bb_json = SentinelDL.geojson_bb(170.0, 45.0, 175.0, 46.0)

    # TODO validate geojson produced here

    # Make sure we've made a Polygon here
    assert bb_json['features'][0]['geometry']['type'] is 'Polygon'
