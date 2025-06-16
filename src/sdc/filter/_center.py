from typing import List

from wai.logging import LOGGING_WARNING
from wai.ma.transformation import Center as WaiCenter

from sdc.api import flatten_list, TrainableBatchFilter, Spectrum2D, safe_deepcopy, spectra_to_matrix, matrix_to_spectra


class Center(TrainableBatchFilter):
    """
    Subtracts the column mean from the columns. Requires multiple spectra as input.
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
        self._trans = None

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "center"

    def description(self) -> str:
        """
        Returns a description of the filter.

        :return: the description
        :rtype: str
        """
        return "Subtracts the column mean from the columns. Requires multiple spectra as input."

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

    def _process_batches(self, batches: List):
        """
        Processes the batches.

        :param batches: the batches to process
        :return: the potentially updated batches
        """
        if not self._trained:
            self._trained = True
            self._trans = WaiCenter()

        result = []
        for data in batches:
            mat = spectra_to_matrix(data)
            mat_new = self._trans.transform(mat)
            sp_new = matrix_to_spectra(mat_new, safe_deepcopy(data[0].spectrum.waves))

            for old, new in zip(data, sp_new):
                new.id = old.spectrum.id
                new.sample_data = safe_deepcopy(old.spectrum.sample_data)
                item_new = Spectrum2D(spectrum_name=old.spectrum_name, spectrum=new)
                result.append(item_new)

        return flatten_list(result)
