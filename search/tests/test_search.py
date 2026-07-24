from search.api.search_engine import SearchEngine


def test_search_engine_creation():
    engine = SearchEngine()

    assert engine is not None


def test_search_returns_list():
    engine = SearchEngine()

    results = engine.search("employee")

    assert isinstance(results, list)