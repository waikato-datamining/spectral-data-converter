import argparse
from typing import List

from seppl import AnyData
from seppl.io import Filter
from seppl.placeholders import add_placeholder, InputBasedPlaceholderSupporter, placeholder_list
from wai.logging import LOGGING_WARNING

from sdc.api import Spectrum2D


class SetPlaceholder(Filter, InputBasedPlaceholderSupporter):

    def __init__(self, placeholder: str = None, value: str = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the filter.

        :param placeholder: the name of the placeholder (without curly brackets)
        :type placeholder: str
        :param value: the value of the placeholder
        :type value: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.placeholder = placeholder
        self.value = value

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "set-placeholder"

    def description(self) -> str:
        """
        Returns a description of the handler.

        :return: the description
        :rtype: str
        """
        return "Sets the placeholder to the specified value when data passes through. The value can contain other placeholders, which get expanded each time data passes through."

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [AnyData]

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
        parser.add_argument("-p", "--placeholder", type=str, help="The name of the placeholder, without curly brackets.", default=None, required=True)
        parser.add_argument("-v", "--value", type=str, help="The value of the placeholder, may contain other placeholders. " + placeholder_list(obj=self), default=None, required=True)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.placeholder = ns.placeholder
        self.value = ns.value

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        if self.placeholder is None:
            raise Exception("No placeholder name provided!")
        if self.value is None:
            raise Exception("No placeholder value provided!")

    def _do_process(self, data: Spectrum2D):
        """
        Processes the data record(s).

        :param data: the record(s) to process
        :return: the potentially updated record(s)
        """
        value = self.session.expand_placeholders(self.value)
        self.logger().info("%s -> %s" % (self.placeholder, value))
        add_placeholder(self.placeholder, "no description", False, lambda i: value)
        return data
