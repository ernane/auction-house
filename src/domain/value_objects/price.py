from dataclasses import dataclass
from enum import StrEnum


class CurrencyOption(StrEnum):
    real = 'BRL'


@dataclass(frozen=True)
class Price:
    value: float
    currency: CurrencyOption
