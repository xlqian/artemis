from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("fr-pdl", scenario='destineo')])
class TestDestineo(ArtemisTestFixture):
    """
    test for destineo with their custom scenario
    """
    def test_destineo_01(self):
        """
        we want to go at the bss north station from the bss south station
        all pt solution are way too long, only 3 non_pt solutions must be returned
        """
        self.journey(_from="poi:TRANSP44_202",
                     to="poi:TRANSP44_369", datetime="20141109T180000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['bss'],
                     min_nb_journeys=3)

    def test_destineo_02(self):
        """
        we go to "Pouzauges" from "La Mothe-Achard" nothing special with this one
        """
        self.journey(_from="admin:85152",
                     to="admin:85182", datetime="20141203T121000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['bss'],
                     min_nb_journeys=3)

    def test_destineo_03(self):
        """
        we go to "Nantes" from "Treillieres"
        we must have a journey with car a departure, also know as P+R and tram train
        and we also check the sort by departure date (and not time), since normaly pure pt journey must be before journey with an alternative fallback
        """
        self.journey(_from="-1.585760091193374;47.29129921981793",
                     to="-1.544638559;47.21411767", datetime="20141201T090000",
                     first_section_mode=['walking', 'car'],
                     min_nb_journeys=3)

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1525", raises=AssertionError)
    def test_destineo_04(self):
        """
        we go to "Pazanne-Mairie-(Ste) (Sainte-Pazanne)" from "gare de Ste-Pazanne (Sainte-Pazanne)"
        there is a non_pt_walk solution, all PT solutions must be filtered since they are way longer than the non pt
        """
        self.journey(_from='stop_area:SNC:SA:SAOCE87481226',
                     to='stop_area:SNC:SA:SAOCE87328625', datetime='20141204T101500',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3)

    def test_destineo_05(self):
        """
        we go from "rue JEAN GORIN (Nantes)" to "15 rue ADOLPHE MOITIE (Nantes)"
        """
        self.journey(_from='-1.5288823896877313;47.2093118677334',
                     to='-1.554597505;47.22280345', datetime='20141111T111000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3, max_nb_journeys=3)

    def test_destineo_06(self):
        """
        we go from "11 boulevard DE L'EGALITE (Nantes)" to "Pompidou (Nantes)"
        """
        self.journey(_from='-1.587547422;47.20738048',
                     to='stop_area:NAN:SA:PPDO', datetime='20141111T111000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3)
