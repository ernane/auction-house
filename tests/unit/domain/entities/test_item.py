from uuid import UUID

import pytest

from src.domain.entities.item import Item


@pytest.fixture
def item():
    return Item(name='Test Item', description='This is a test item')


def test_item_creation(item):
    # Arrange is feito no fixture

    # Act
    # Nenhuma ação necessária, pois estamos testando a criação

    # Assert
    assert item.name == 'Test Item'
    assert item.description == 'This is a test item'
    assert isinstance(item.id, UUID)
