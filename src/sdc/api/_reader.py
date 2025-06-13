import argparse
import seppl.io
from seppl import Initializable
from typing import List

from wai.logging import LOGGING_WARNING


class Reader(seppl.io.Reader, Initializable):
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


def parse_reader(reader: str) -> Reader:
    """
    Parses the command-line and instantiates the reader.

    :param reader: the command-line to parse
    :type reader: str
    :return: the reader
    :rtype: Reader
    """
    from seppl import split_args, split_cmdline, args_to_objects
    from sdc.registry import available_readers

    if reader is None:
        raise Exception("No reader command-line supplied!")
    valid = dict()
    valid.update(available_readers())
    args = split_args(split_cmdline(reader), list(valid.keys()))
    objs = args_to_objects(args, valid, allow_global_options=False)
    if len(objs) == 1:
        if isinstance(objs[0], Reader):
            result = objs[0]
        else:
            raise Exception("Expected instance of Reader but got: %s" % str(type(objs[0])))
    else:
        raise Exception("Expected to obtain one reader from '%s' but got %d instead!" % (reader, len(objs)))
    return result
