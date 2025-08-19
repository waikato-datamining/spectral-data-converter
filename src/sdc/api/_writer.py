import argparse
from typing import List

from wai.logging import LOGGING_WARNING
from seppl import Initializable
import kasperl.api
import seppl.io
from ._data import SampleData
from ._spectralio import SpectralIOBased


class SpectralIOWriter(SpectralIOBased):
    """
    Mixin for SpectralIO-based writers.
    """

    def _init_writer(self):
        """
        Initializes the writer.

        :return: the writer
        """
        raise NotImplementedError()


class DefaultExtensionWriter:
    """
    Mixin for writers that have a default file extension.
    """

    @property
    def default_extension(self) -> str:
        """
        Returns the default extension (incl dot) for this file type.

        :return: the default extension
        :rtype: str
        """
        raise NotImplementedError()


class SampleDataBatchWriter(kasperl.api.BatchWriter, Initializable):
    """
    Ancestor for batch sample data writers.
    """

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [SampleData]


class SplittableSampleDataBatchWriter(SampleDataBatchWriter):
    """
    Ancestor for batch sample data writers that .
    """

    def __init__(self, split_names: List[str] = None, split_ratios: List[int] = None, split_group: str = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the reader.

        :param split_names: the names of the splits, no splitting if None
        :type split_names: list
        :param split_ratios: the integer ratios of the splits (must sum up to 100)
        :type split_ratios: list
        :param split_group: the regular expression with a single group used for keeping items in the same split, e.g., for identifying the base name of a file or the sample ID
        :type split_group: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.split_names = None
        self.split_ratios = None
        self.split_group = None
        self.splitter = None
        seppl.io.init_splitting_params(self, split_names=split_names, split_ratios=split_ratios, split_group=split_group)

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        seppl.io.add_splitting_params(parser)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        seppl.io.transfer_splitting_params(ns, self)

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        seppl.io.initialize_splitting(self)


class SampleDataStreamWriter(kasperl.api.StreamWriter):
    """
    Ancestor for stream sample data writers.
    """

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [SampleData]


class SplittableSampleDataStreamWriter(SampleDataStreamWriter):
    """
    Ancestor for sample data stream writers that support splits.
    """

    def __init__(self, split_names: List[str] = None, split_ratios: List[int] = None, split_group: str = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the reader.

        :param split_names: the names of the splits, no splitting if None
        :type split_names: list
        :param split_ratios: the integer ratios of the splits (must sum up to 100)
        :type split_ratios: list
        :param split_group: the regular expression with a single group used for keeping items in the same split, e.g., for identifying the base name of a file or the sample ID
        :type split_group: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.split_names = None
        self.split_ratios = None
        self.split_group = None
        self.splitter = None
        seppl.io.init_splitting_params(self, split_names=split_names, split_ratios=split_ratios, split_group=split_group)

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        seppl.io.add_splitting_params(parser)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        seppl.io.transfer_splitting_params(ns, self)

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        seppl.io.initialize_splitting(self)
