import numpy as np

from typing import Dict, Optional, Union, Any
from ._data import Spectrum
from wai.spectralio.api import Spectrum as WaiSpectrum
from wai.ma.core.matrix import Matrix


class Spectrum2D(Spectrum):

    def __init__(self, source: str = None, spectrum_name: str = None,
                 spectrum: WaiSpectrum = None, metadata: Dict = None):
        super().__init__(source=source, spectrum_name=spectrum_name, spectrum=spectrum, metadata=metadata)

    def has_metadata(self) -> bool:
        """
        Returns whether meta-data is present.

        :return: True if meta-data present
        :rtype: bool
        """
        return self._spectrum.sample_data is not None

    def get_metadata(self) -> Optional[Dict]:
        """
        Returns the meta-data.

        :return: the meta-data, None if not available
        :rtype: dict
        """
        if self._spectrum is not None:
            return self._spectrum.sample_data
        else:
            return None

    def set_metadata(self, metadata: Optional[Dict]):
        """
        Sets the meta-data to use.

        :param metadata: the new meta-data, can be None
        :type metadata: dict
        """
        self._spectrum.sample_data = metadata


def spectrum_to_matrix(sp: Union[Spectrum2D, WaiSpectrum], add_waveno: bool = True) -> Matrix:
    """
    Turns the spectrum into a wai.ma matrix.

    :param sp: the spectrum to convert
    :type sp: Spectrum2D or WaiSpectrum
    :param add_waveno: whether to include the wave numbers as first row
    :type add_waveno: bool
    :return: the matrix generated from the spectrum
    :rtype: Matrix
    """
    if isinstance(sp, Spectrum2D):
        sp = sp.spectrum
    if add_waveno:
        result = Matrix(np.array([np.asarray(sp.waves), np.asarray(sp.amplitudes)]))
    else:
        result = Matrix(np.asarray(sp.amplitudes))
    return result


def matrix_to_spectrum(matrix: Matrix, sample_id: str = None, sample_data: Dict[str, Any] = None) -> WaiSpectrum:
    """
    Turns the matrix back into a spectrum data structure.

    :param matrix: the matrix to convert
    :type matrix: Matrix
    :param sample_id: the sample ID to use
    :type sample_id: str
    :param sample_data: the sample data to use
    :type sample_data: dict
    :return: the generated spectrum
    :rtype: WaiSpectrum
    """
    w_new = [float(x) for x in matrix.data[0]]
    a_new = [float(x) for x in matrix.data[1]]
    result = WaiSpectrum(waves=w_new, amplitudes=a_new, sample_data=sample_data)
    if sample_id is not None:
        result.id = sample_id
    return result
