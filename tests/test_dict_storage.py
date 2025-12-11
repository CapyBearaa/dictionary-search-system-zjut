# tests/test_dict_storage.py
import pytest

# Импортируем вашу реализацию и Mock-классы для тестов
from src.storages.dict_storage import DictionaryStorage, MockItem, MockCollection


@pytest.fixture
def storage():
    """Returns a fresh instance of DictionaryStorage for each test."""
    return DictionaryStorage()


def test_add_and_retrieve_item_success(storage):
    """Tests O(1) retrieval for a single Item (Leaf)."""
    key = "ISBN9780321765723"
    book = MockItem(key, "The C++ Programming Language", "Bjarne Stroustrup")
    
    assert storage.add(key, book) is True
    
    retrieved_book = storage.retrieve(key)
    assert retrieved_book == book
    assert storage.size() == 1


def test_retrieve_not_found(storage):
    """Tests retrieval of a key that does not exist."""
    assert storage.retrieve(999) is None
    assert storage.contains(999) is False


def test_update_item(storage):
    """Tests O(1) update operation."""
    key = "T_001"
    original = MockItem(key, "Old Title", "Author X")
    updated = MockItem(key, "New Title", "Author Y")
    
    storage.add(key, original)
    storage.add(key, updated) # This should overwrite
    
    assert storage.size() == 1
    assert storage.retrieve(key) == updated
    assert storage.retrieve(key) != original


def test_remove_success(storage):
    """Tests O(1) removal operation."""
    key = 404
    book = MockItem(key, "Non-existent Book", "Error")
    
    storage.add(key, book)
    
    assert storage.remove(key) is True
    assert storage.contains(key) is False
    assert storage.size() == 0


def test_add_and_retrieve_collection_composite(storage):
    """
    Tests adding and retrieving a Collection (Composite) object.
    """
    # Create Composite object
    shelf_key = "SF_SHELF"
    sci_fi_shelf = MockCollection(shelf_key, "Science Fiction Shelf")
    sci_fi_shelf.add_component(MockItem("DUNE", "Dune", "Herbert"))
    sci_fi_shelf.add_component(MockItem("RING", "Ringworld", "Niven"))
    
    # Add the entire Composite object to storage (O(1))
    storage.add(shelf_key, sci_fi_shelf)
    
    retrieved_shelf = storage.retrieve(shelf_key)
    assert retrieved_shelf is not None
    assert retrieved_shelf.title == "Science Fiction Shelf"
    # Check the recursive size of the retrieved component
    assert retrieved_shelf.get_size() == 2 # 2 items inside the shelf
    assert storage.size() == 1 # Only one component (the shelf) at the top level


def test_deep_search_for_item_in_collection(storage):
    """
    Tests deep_search_all, ensuring it finds an item nested within a Collection.
    """
    # Setup Collection
    sci_fi_shelf = MockCollection("SFC", "SciFi")
    target_book = MockItem("TARGET_KEY", "The Martian", "Andy Weir")
    sci_fi_shelf.add_component(target_book)
    
    # Add Collection to Storage
    storage.add("COL_1", sci_fi_shelf)
    
    # Search for the key of the nested item
    results = storage.deep_search_all("TARGET_KEY")
    
    # Check that the item was found
    assert len(results) == 1
    assert results[0].title == "The Martian"
