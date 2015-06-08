from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest

@dataset([DataSet("tcl")])
class TestTCL(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_tcl_01(self):
        """
        ID artemis v1: 0
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090722T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_tcl_02(self):
        """
        ID artemis v1: 8
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090722T120000",
                     walking_speed="0.83", max_duration_to_pt="600")

    def test_tcl_03(self):
        """
        ID artemis v1: 9
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090722T233000",
                     walking_speed="0.83", max_duration_to_pt="600")

    def test_tcl_04(self):
        """
        ID artemis v1: 10
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090723T001000",
                     walking_speed="0.83", max_duration_to_pt="600")

    def test_tcl_05(self):
        """
        ID artemis v1: 11
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090722T235900",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_tcl_06(self):
        """
        ID artemis v1: 12
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090723T004000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_tcl_07(self):
        """
        ID artemis v1: 13
        """
        self.journey(_from="stop_area:TCL:SA:5520",
                     to="stop_area:TCL:SA:5085", datetime="20090723T004400",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="240")
