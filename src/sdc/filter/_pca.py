import argparse
from typing import List

from wai.ma.algorithm import PCA as WaiPCA
from wai.logging import LOGGING_WARNING
from sdc.api import flatten_list, TrainableBatchFilter, Spectrum2D, safe_deepcopy, spectra_to_matrix, matrix_to_spectra


class PCA(TrainableBatchFilter):
    """
    Subtracts mean and divides by standard deviation.
    """

    def __init__(self, variance: float = None, max_columns: int = None, center: bool = False,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the filter.

        :param variance: the variance to use
        :type variance: float
        :param max_columns: the maximum number of columns to produce, -1 for unlimited
        :type max_columns: int
        :param center: whether to center the data
        :type center: bool
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.variance = variance
        self.max_columns = max_columns
        self.center = center
        self._alg = None

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "pca"

    def description(self) -> str:
        """
        Returns a description of the filter.

        :return: the description
        :rtype: str
        """
        return "Applies principal components analysis to the data for dimensionality reduction."

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [Spectrum2D]

    def generates(self) -> List:
        """
        Returns the list of classes that get produced.

        :return: the list of classes
        :rtype: list
        """
        return [Spectrum2D]

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        parser.add_argument("-v", "--variance", type=float, help="The variance to use.", default=0.95, required=False)
        parser.add_argument("-m", "--max_columns", type=int, help="The maximum number of columns to generate, use -1 for unlimited.", default=-1, required=False)
        parser.add_argument("-c", "--center", action="store_true", help="Centers the data before applying PCA.")
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.variance = ns.variance
        self.max_columns = ns.max_columns
        self.center = ns.center

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()
        if self.variance is None:
            self.variance = 0.95
        if self.max_columns is None:
            self.max_columns = -1
        if self.center is None:
            self.center = False

    def _process_batches(self, batches: List):
        """
        Processes the batches.

        :param batches: the batches to process
        :return: the potentially updated batches
        """
        if not self._trained:
            self._trained = True
            self._alg = WaiPCA()
            self._alg.variance = self.variance
            self._alg.max_columns = self.max_columns
            self._alg.center = self.center

        result = []
        for batch_old in batches:
            mat_old = spectra_to_matrix([x.spectrum for x in batch_old])
            mat_new = self._alg.transform(mat_old)
            batch_new = matrix_to_spectra(mat_new, waveno=[x for x in range(mat_new.num_columns())])
            for sp_new, sp_old in zip(batch_new, batch_old):
                sp_new.sample_data = safe_deepcopy(sp_old.spectrum.sample_data)
                item_new = Spectrum2D(spectrum_name=sp_old.spectrum_name, spectrum=sp_new)
                result.append(item_new)

        return flatten_list(result)
