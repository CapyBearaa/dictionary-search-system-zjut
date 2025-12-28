import pytest
from src.storages.list_storage import ListStorage


# простая заглушка Item под тесты
class Item:
    def __init__(self, id, name, group):
        self.id = id
        self.name = name
        self.group = group


@pytest.fixture
def storage():
    storage = ListStorage()
    storage.add(Item("31201001", "Jamil Kamal", "A1"))
    storage.add(Item("31201002", "Ali Rahman", "B1"))
    storage.add(Item("31201003", "Jamil Kamal", "A1"))
    return storage


def test_add_and_get_all(storage):
    items = storage.get_all()
    assert len(items) == 3


def test_add_duplicate_id():
    storage = ListStorage()
    storage.add(Item("31201001", "Test", "A1"))

    with pytest.raises(ValueError):
        storage.add(Item("31201001", "Duplicate", "B1"))


def test_search_by_id_found(storage):
    student = storage.search_by_id("31201002")
    assert student is not None
    assert student.name == "Ali Rahman"
    assert student.group == "B1"


def test_search_by_id_not_found(storage):
    student = storage.search_by_id("99999999")
    assert student is None


def test_search_by_name(storage):
    results = storage.search_by_name("Jamil Kamal")
    assert len(results) == 2
    for student in results:
        assert student.name == "Jamil Kamal"


def test_search_by_group(storage):
    results = storage.search_by_group("A1")
    assert len(results) == 2
    for student in results:
        assert student.group == "A1"
