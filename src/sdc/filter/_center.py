from typing import List

from wai.ma.transformation import Center as WaiCenter

from sdc.api import flatten_list, Filter, Spectrum2D, safe_deepcopy, spectra_to_matrix, matrix_to_spectra


class Center(Filter):
    """
    Subtracts the column mean from the columns. Requires multiple spectra as input.
    """

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

    def _requires_list_input(self) -> bool:
        """
        Returns whether lists are expected as input for the _process method.

        :return: True if list inputs are expected by the filter
        :rtype: bool
        """
        return True

    def _do_process(self, data):
        """
        Processes the data record(s).

        :param data: the record(s) to process
        :return: the potentially updated record(s)
        """
        trans = WaiCenter()
        mat = spectra_to_matrix(data)
        mat_new = trans.transform(mat)
        sp_new = matrix_to_spectra(mat_new, safe_deepcopy(data[0].spectrum.waves))

        result = []
        for old, new in zip(data, sp_new):
            new.id = old.spectrum.id
            new.sample_data = safe_deepcopy(old.spectrum.sample_data)
            item_new = Spectrum2D(spectrum_name=old.spectrum_name, spectrum=new)
            result.append(item_new)

        return flatten_list(result)
