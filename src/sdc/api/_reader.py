import argparse
from typing import List

from kasperl.api import Reader as KReader
from wai.logging import LOGGING_WARNING

from ._data import SampleData
from ._spectralio import SpectralIOBased


class Reader(KReader):
    """
    Ancestor for dataset readers.
    """

    def __init__(self, instrument: str = None, format: str = None, keep_format: bool = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the reader.

        :param instrument: the instrument name to use
        :type instrument: str
        :param format: the spectral format
        :type format: str
        :param keep_format: whether to keep the format determined by the reader
        :type keep_format: bool
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.instrument = instrument
        self.format = format
        self.keep_format = keep_format

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        parser.add_argument("--instrument", type=str, help="The instrument this data is from", required=False, default="unknown")
        parser.add_argument("--format", type=str, help="The spectral data format to set", required=False, default="NIR")
        parser.add_argument("--keep_format", action="store_true", help="Will keep the format that the reader determines rather than the supplied one.", required=False)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.instrument = ns.instrument
        self.format = ns.format
        self.keep_format = ns.keep_format

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        if self.instrument is None:
            self.instrument = "unknown"
        if self.format is None:
            self.format = "NIR"
        if self.keep_format is None:
            self.keep_format = False


def add_locale_option(parser: argparse.ArgumentParser):
    """
    Adds the locale option to the parser.

    :param parser: the parser to update
    :type parser: argparse.ArgumentParser
    """
    parser.add_argument("--locale", type=str, help="The locale to use for parsing/formatting numbers", required=False, default="en_US")


class SpectralIOReader(Reader, SpectralIOBased):
    """
    Ancestor for readers that use a wai.spectralio-based reader under the hood.
    """

    def _compile_options(self) -> List[str]:
        """
        Compiles the options for initializing the underlying reader.

        :return: the list of options to use
        :rtype: list
        """
        result = ["--instrument", self.instrument, "--format", self.format]
        if self.keep_format:
            result.append("--keep-format")
        return result

    def _init_reader(self):
        """
        Initializes the reader.

        :return: the reader
        """
        raise NotImplementedError()


class SpectralIOReaderWithLocaleSupport(SpectralIOReader):
    """
    Ancestor for dataset readers that support locales.
    """

    def __init__(self, instrument: str = None, format: str = None, keep_format: bool = None, locale: str = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the reader.

        :param instrument: the instrument name to use
        :type instrument: str
        :param format: the spectral format
        :type format: str
        :param keep_format: whether to keep the format determined by the reader
        :type keep_format: bool
        :param locale: the locale to use for parsing numbers
        :type locale: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(instrument=instrument, format=format, keep_format=keep_format, logger_name=logger_name, logging_level=logging_level)
        self.locale = locale

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        add_locale_option(parser)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.locale = ns.locale

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        if self.locale is None:
            self.locale = "en_US"

    def _compile_options(self) -> List[str]:
        """
        Compiles the options for initializing the underlying reader.

        :return: the list of options to use
        :rtype: list
        """
        result = super()._compile_options()
        result.extend(["--locale", self.locale])
        return result


class SampleDataReader(KReader):
    """
    Ancestor for sample data readers.
    """

    def generates(self) -> List:
        """
        Returns the list of classes that get produced.

        :return: the list of classes
        :rtype: list
        """
        return [SampleData]
