# src/storages/dict_storage.py
from typing import Any, Optional, Dict, List, Protocol, runtime_checkable
from abc import ABC, abstractmethod

# --- MOCK INTERFACES & CLASSES (Temporary until Kimal provides final files) ---

# --- 1. MOCK Component Interface (Root of Composite Pattern) ---
@runtime_checkable
class SearchableComponent(Protocol):
    """
    MOCK interface for all entities (Item or Collection).
    """
    def get_key(self) -> Any: ...
    def get_size(self) -> int: ...
    def deep_search(self, key: Any) -> List['SearchableComponent']: ...

# --- 2. MOCK Item (Leaf) ---
class MockItem:
    """MOCK Leaf component (e.g., a Book)."""
    def __init__(self, key: Any, title: str, author: str):
        self._key = key
        self.title = title
        self.author = author

    def get_key(self) -> Any:
        return self._key

    def get_size(self) -> int:
        return 1

    def deep_search(self, key: Any) -> List[SearchableComponent]:
        return [self] if self._key == key else []

    def __eq__(self, other):
        if not isinstance(other, MockItem):
            return NotImplemented
        return self._key == other._key and self.title == other.title and self.author == other.author

# --- 3. MOCK Collection (Composite) ---
class MockCollection:
    """MOCK Composite component (e.g., a Shelf/Genre)."""
    def __init__(self, key: Any, title: str):
        self._key = key
        self.title = title
        self._components: List[SearchableComponent] = []

    def add_component(self, component: SearchableComponent):
        self._components.append(component)

    def get_key(self) -> Any:
        return self._key

    def get_size(self) -> int:
        """Recursive call: sums the sizes of all nested components."""
        return sum(c.get_size() for c in self._components)

    def deep_search(self, key: Any) -> List[SearchableComponent]:
        results = []
        if self._key == key:
            results.append(self)
        
        for component in self._components:
            results.extend(component.deep_search(key))
        return results

# --- 4. MOCK Storage Interface (Strategy Pattern) ---
class MockStorage(ABC):
    """MOCK interface for storage strategies (Dict, List, BST)."""
    @abstractmethod
    def add(self, key: Any, component: SearchableComponent) -> bool: ...
    @abstractmethod
    def retrieve(self, key: Any) -> Optional[SearchableComponent]: ...
    @abstractmethod
    def remove(self, key: Any) -> bool: ...
    @abstractmethod
    def size(self) -> int: ...

# -------------------------------------------------------------


class DictionaryStorage(MockStorage):
    """
    The main implementation using a Hash Table (Python dict).
    Provides O(1) average time complexity for core operations (add, retrieve, remove).
    
    """
    
    def __init__(self):
        # Internal dictionary to store the data: {key: SearchableComponent}
        self._data: Dict[Any, SearchableComponent] = {}

    def add(self, key: Any, component: SearchableComponent) -> bool:
        """Complexity: O(1) average."""
        self._data[key] = component
        return True

    def retrieve(self, key: Any) -> Optional[SearchableComponent]:
        """Complexity: O(1) average."""
        return self._data.get(key)

    def remove(self, key: Any) -> bool:
        """Complexity: O(1) average."""
        if key in self._data:
            del self._data[key]
            return True
        return False

    def contains(self, key: Any) -> bool:
        """Complexity: O(1) average."""
        return key in self._data

    def size(self) -> int:
        """
        Returns the count of components on the first level of storage.
        Complexity: O(1).
        """
        return len(self._data)

    def deep_search_all(self, key: Any) -> List[SearchableComponent]:
        """
        Initiates a recursive search across all components in the storage.
        Complexity: O(Total_Items) in the worst case, as it traverses all elements.
        """
        results: List[SearchableComponent] = []
        for component in self._data.values():
            results.extend(component.deep_search(key))
        return results
