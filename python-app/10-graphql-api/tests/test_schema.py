import sys
sys.path.insert(0, '../src')

def test_schema_import():
    from schema import schema
    assert schema is not None
