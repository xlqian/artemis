from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


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
