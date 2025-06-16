import abc
import argparse
from typing import List
from seppl.io import Filter as SFilter
from seppl import MetaDataHandler, get_metadata
from sdc.api import make_list
from wai.logging import LOGGING_WARNING


class Filter(SFilter, abc.ABC):
    """
    Ancestor for filters.
    """
    pass


class BatchFilter(Filter, abc.ABC):
    """
    Ancestor for filters that work on batches.
    """

    def __init__(self, metadata_key: str = None, logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the filter.

        :param metadata_key: the key in the metadata that identifies the batches
        :type metadata_key: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.metadata_key = metadata_key

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        parser.add_argument("-k", "--metadata_key", type=str, help="The key in the meta-data that identifies the batches. NB: sorts the batch names alphabetically.", default=None, required=False)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.metadata_key = ns.metadata_key

    def _requires_list_input(self) -> bool:
        """
        Returns whether lists are expected as input for the _process method.

        :return: True if list inputs are expected by the filter
        :rtype: bool
        """
        return True

    def _process_batches(self, batches: List):
        """
        Processes the batches.

        :param batches: the batches to process
        :return: the potentially updated batches
        """
        raise NotImplementedError()

    def _do_process(self, data):
        """
        Processes the data record(s).

        :param data: the record(s) to process
        :return: the potentially updated record(s)
        """
        if self.metadata_key is None:
            return self._process_batches([data])
        else:
            splits = dict()
            for item in make_list(data):
                # get meta data
                meta = get_metadata(item)
                if meta is None:
                    if not isinstance(item, MetaDataHandler):
                        raise Exception("Cannot access meta-data for type: %s" % str(type(item)))

                split = meta[self.metadata_key]
                if split not in splits:
                    splits[split] = []
                splits[split].append(item)

            batches = []
            split_names = sorted(splits.keys())
            self.logger().info("split names: %s" % str(split_names))
            for split in split_names:
                batches.append(splits[split])
            return self._process_batches(batches)


class TrainableBatchFilter(BatchFilter, abc.ABC):
    """
    Batch filter that get trained with first batch.
    """

    def __init__(self, metadata_key: str = None, logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the handler.

        :param metadata_key: the key in the metadata that identifies the batches
        :type metadata_key: str
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(metadata_key=metadata_key, logger_name=logger_name, logging_level=logging_level)
        self._trained = False

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        self._trained = False


def parse_filter(filter_: str) -> Filter:
    """
    Parses the command-line and instantiates the filter.

    :param filter_: the command-line to parse
    :type filter_: str
    :return: the filter
    :rtype: Filter
    """
    from seppl import split_args, split_cmdline, args_to_objects
    from sdc.registry import available_filters

    if filter_ is None:
        raise Exception("No filter command-line supplied!")
    valid = dict()
    valid.update(available_filters())
    args = split_args(split_cmdline(filter_), list(valid.keys()))
    objs = args_to_objects(args, valid, allow_global_options=False)
    if len(objs) == 1:
        if isinstance(objs[0], Filter):
            result = objs[0]
        else:
            raise Exception("Expected instance of Filter but got: %s" % str(type(objs[0])))
    else:
        raise Exception("Expected to obtain one filter from '%s' but got %d instead!" % (filter_, len(objs)))
    return result
