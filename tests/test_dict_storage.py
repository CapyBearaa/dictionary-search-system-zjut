# tests/test_dict_storage.py
import pytest
from src.storages.dict_storage import DictStorage, Item

@pytest.fixture
def storage():
    """Provides a fresh DictStorage instance with sample data for each test."""
    s = DictStorage()
    s.add(Item("3120100001", "John Doe", "A1"))
    s.add(Item("3120100002", "Jane Smith", "B2"))
    s.add(Item("3120100003", "Bob Wilson", "A1"))
    return s

def test_add_and_get_all_success(storage):
    """Verifies that items are added and the total count is correct."""
    all_items = storage.get_all()
    assert len(all_items) == 3

def test_search_by_id_success(storage):
    """
    Tests searching by ID (the primary O(1) operation).
    """
    item = storage.search_by_id("3120100002")
    assert item is not None
    assert item.name == "Jane Smith"
    assert item.group == "B2"

def test_search_by_id_not_found(storage):
    """Verifies that searching for a non-existent ID returns None."""
    item = storage.search_by_id("9999999999")
    assert item is None

def test_add_update_existing_id(storage):
    """
    Verifies that adding an item with an existing ID updates the record.
    """
    updated_item = Item("3120100001", "John Updated", "C3")
    storage.add(updated_item)
    
    # Total count should remain 3
    assert len(storage.get_all()) == 3 
    
    # Data should reflect the update
    retrieved = storage.search_by_id("3120100001")
    assert retrieved.name == "John Updated"
    assert retrieved.group == "C3"

def test_search_by_group(storage):
    """
    Tests searching by group (an O(N) operation).
    """
    results = storage.search_by_group("A1")
    assert len(results) == 2
    
    # Verify both IDs are present in the results
    ids = {item.student_id for item in results}
    assert "3120100001" in ids
    assert "3120100003" in ids
