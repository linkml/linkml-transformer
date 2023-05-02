from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from linkml_transformer.datamodel.transformer_model import TransformationSpecification


@dataclass
class Importer(ABC):
    """
    Base class for all importers.

    A compiler will translate an external mapping spec into the LinkML transformation model.

    An example importer would be sssom.
    """

    @abstractmethod
    def import_specification(self, input: Any) -> TransformationSpecification:
        """
        Import into a specification

        :param specification:
        :return:
        """
        raise NotImplementedError
