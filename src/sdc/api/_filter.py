import abc
from seppl.io import Filter as SFilter
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

    def _requires_list_input(self) -> bool:
        """
        Returns whether lists are expected as input for the _process method.

        :return: True if list inputs are expected by the filter
        :rtype: bool
        """
        return True


class TrainableBatchFilter(BatchFilter, abc.ABC):
    """
    Batch filter that get trained with first batch.
    """

    def __init__(self, logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the handler.

        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
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
