from typing import Dict, Optional
from ._data import Spectrum
from wai.spectralio.api import Spectrum as WaiSpectrum


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
