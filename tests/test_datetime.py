
def test_timestamp_from_string():
    """
    Test that a pandas timestamp is produced from given strings
    """
    from geotoys.datetime import timestamp_from_string
    import pandas

    examples = [
        "some_file_name_201201050842_with_timestamp.tif",
        #"2012-01-05_08:42_with_timestamp.tif",
    ]

    for ex in examples:
        assert type(timestamp_from_string(ex)) is pandas.Timestamp


def test_utc_timestamp():
    """
    Test that the resulting timestamp's timezone attribute is pytz.UTC
    """
    from geotoys.datetime import utc_timestamp
    import pandas
    import pytz

    ts = pandas.Timestamp(2012,1,5,8,42)
    ts_utc = utc_timestamp(ts)

    assert ts_utc.tz is pytz.UTC
