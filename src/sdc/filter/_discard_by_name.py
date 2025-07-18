import argparse
import os
import re
from typing import List

from seppl import AnyData
from wai.logging import LOGGING_WARNING

from sdc.api import Spectrum, flatten_list, make_list, Filter


class DiscardByName(Filter):
    """
    Discards files based on list of spectrum names and/or regular expressions that spectrum names must match.
    """

    def __init__(self, names: List[str] = None, names_file: str = None, paths: List[str] = None,
                 regexps: List[str] = None, regexps_file: str = None,
                 remove_ext: bool = None, invert: bool = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the filter.

        :param names: the list of spectrum names to drop
        :type names: list
        :param names_file: the text file with the spectrum names to drop (one per line)
        :type names_file: str
        :param paths: the list of paths with files to ignore, ignored if None
        :type paths: list
        :param regexps: the regular expressions for dropping spectrum names
        :type regexps: list
        :param regexps_file: the text file with the regexps for dropping spectrum names (one per line)
        :type regexps_file: str
        :param remove_ext: whether to remove the extension before determining matches
        :type remove_ext: bool
        :param invert: whether to invert the matching sense
        :type invert: bool
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.names = names
        self.names_file = names_file
        self.paths = paths
        self.regexps = regexps
        self.regexps_file = regexps_file
        self.remove_ext = remove_ext
        self.invert = invert
        self._names = None
        self._regexps = None

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "discard-by-name"

    def description(self) -> str:
        """
        Returns a description of the filter.

        :return: the description
        :rtype: str
        """
        return "Discards files based on list of spectrum names, list of paths and/or regular expressions that spectrum names must match."

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [Spectrum]

    def generates(self) -> List:
        """
        Returns the list of classes that get produced.

        :return: the list of classes
        :rtype: list
        """
        return [AnyData]

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        parser.add_argument("-i", "--names", type=str, help="The spectrum name(s) to drop.", required=False, nargs="*")
        parser.add_argument("-I", "--names_file", type=str, help="The text file with the spectrum name(s) to drop.", required=False, default=None)
        parser.add_argument("-p", "--paths", type=str, help="The directories with spectra to ignore.", required=False, nargs="*")
        parser.add_argument("-r", "--regexps", type=str, help="The regular expressions for matching spectrum name(s) to drop.", required=False, nargs="*")
        parser.add_argument("-R", "--regexps_file", type=str, help="The text file with regular expressions for matching spectrum name(s) to drop.", required=False, default=None)
        parser.add_argument("-e", "--remove_ext", action="store_true", help="Whether to remove the extension (and dot) before matching.")
        parser.add_argument("-V", "--invert", action="store_true", help="Whether to invert the matching sense.")
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.names = ns.names
        self.names_file = ns.names_file
        self.paths = ns.paths
        self.regexps = ns.regexps
        self.regexps_file = ns.regexps_file
        self.remove_ext = ns.remove_ext
        self.invert = ns.invert

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()

        if self.remove_ext is None:
            self.remove_ext = False
        if self.invert is None:
            self.invert = False

        # names
        self._names = set()
        if self.names is not None:
            self._names.update(self.names)
        if self.names_file is not None:
            with open(self.names_file) as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.strip()
                    if len(line) > 0:
                        self._names.add(line)

        # paths
        if self.paths is not None:
            for path in self.paths:
                for f in os.listdir(path):
                    full = os.path.join(path, f)
                    if not os.path.isfile(full):
                        continue
                    if self.remove_ext:
                        f = os.path.splitext(f)[0]
                    self._names.add(f)

        self.logger().info("# names: %d" % len(self._names))

        # regexps
        self._regexps = list()
        if self.regexps is not None:
            for regexp in self.regexps:
                self._regexps.append(re.compile(regexp))
        if self.regexps_file is not None:
            with open(self.regexps_file) as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.strip()
                    if len(line) > 0:
                        self._regexps.append(re.compile(line))
        self.logger().info("# regexps: %d" % len(self._regexps))

    def _do_process(self, data):
        """
        Processes the data record(s).

        :param data: the record(s) to process
        :return: the potentially updated record(s)
        """
        # nothing to do?
        if (len(self._names) == 0) and (len(self._regexps) == 0):
            return data

        result = []
        for item in make_list(data):
            spectrum_name = item.spectrum_name
            if self.remove_ext:
                spectrum_name = os.path.splitext(spectrum_name)[0]

            add = True

            # check against names
            if len(self._names) > 0:
                if spectrum_name in self._names:
                    if not self.invert:
                        self.logger().info("Skipping based on name match: %s" % item.spectrum_name)
                        add = False
                else:
                    if self.invert:
                        self.logger().info("Skipping based on no name match (invert): %s" % item.spectrum_name)
                        add = False

            # check against regexps
            if add:
                for regexp in self._regexps:
                    if regexp.fullmatch(spectrum_name) is not None:
                        if not self.invert:
                            self.logger().info("Skipping based on regexp match: %s" % item.spectrum_name)
                            add = False
                            break
                    else:
                        if self.invert:
                            self.logger().info("Skipping based on no regexp match (invert): %s" % item.spectrum_name)
                            add = False
                            break

            if add:
                result.append(item)

        return flatten_list(result)
