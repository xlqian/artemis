from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario


@dataset([DataSet("idfm")])
class IdfM(object):


        def test_IdfM_0(self):
            """
            /v1/coverage/stif/journeys?from=2.3344;48.8686&to=2.395775;48.881221999999994&datetime=20160623T190000
            """
            self.journey(_from="2.3344;48.8686", to="2.395775;48.881221999999994", datetime="20160623T190000")


        def test_IdfM_1(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8579&to=2.363038;48.855154999999996&datetime=20151203T210000
            """
            self.journey(_from="2.3494;48.8579", to="2.363038;48.855154999999996", datetime="20151203T210000")


        def test_IdfM_2(self):
            """
            /v1/coverage/stif/journeys?from=2.3358;48.8722&to=2.3425990000000003;48.874043&datetime=20151203T210000
            """
            self.journey(_from="2.3358;48.8722", to="2.3425990000000003;48.874043", datetime="20151203T210000")


        def test_IdfM_3(self):
            """
            /v1/coverage/stif/journeys?from=2.3126;48.883&to=2.322147;48.883035&datetime=20151203T210000
            """
            self.journey(_from="2.3126;48.883", to="2.322147;48.883035", datetime="20151203T210000")


        def test_IdfM_4(self):
            """
            /v1/coverage/stif/journeys?from=2.2963;48.803000000000004&to=2.394357;48.833560999999996&datetime=20160225T190000
            """
            self.journey(_from="2.2963;48.803000000000004", to="2.394357;48.833560999999996", datetime="20160225T190000")


        def test_IdfM_5(self):
            """
            /v1/coverage/stif/journeys?from=2.3412;48.83&to=2.312592;48.901918&datetime=20160225T190000
            """
            self.journey(_from="2.3412;48.83", to="2.312592;48.901918", datetime="20160225T190000")


        def test_IdfM_6(self):
            """
            /v1/coverage/stif/journeys?from=2.3521;48.8453&to=2.3712299999999997;48.877635&datetime=20160623T190000
            """
            self.journey(_from="2.3521;48.8453", to="2.3712299999999997;48.877635", datetime="20160623T190000")


        def test_IdfM_7(self):
            """
            /v1/coverage/stif/journeys?from=2.9308;49.0362&to=2.343961;48.869546&datetime=20180802T180000
            """
            self.journey(_from="2.9308;49.0362", to="2.343961;48.869546", datetime="20180802T180000")


        def test_IdfM_8(self):
            """
            /v1/coverage/stif/journeys?from=2.3044;48.9055&to=2.303043;48.902815000000004&datetime=20151203T210000
            """
            self.journey(_from="2.3044;48.9055", to="2.303043;48.902815000000004", datetime="20151203T210000")


        def test_IdfM_9(self):
            """
            /v1/coverage/stif/journeys?from=2.3576;48.873999999999995&to=2.2989919999999997;48.849756&datetime=20160623T190000
            """
            self.journey(_from="2.3576;48.873999999999995", to="2.2989919999999997;48.849756", datetime="20160623T190000")


        def test_IdfM_10(self):
            """
            /v1/coverage/stif/journeys?from=2.0568;48.7847&to=2.297605;48.880331&datetime=20160225T190000
            """
            self.journey(_from="2.0568;48.7847", to="2.297605;48.880331", datetime="20160225T190000")


        def test_IdfM_11(self):
            """
            /v1/coverage/stif/journeys?from=2.2527;48.8434&to=2.415858;48.6474&datetime=20160225T190000
            """
            self.journey(_from="2.2527;48.8434", to="2.415858;48.6474", datetime="20160225T190000")


        def test_IdfM_12(self):
            """
            /v1/coverage/stif/journeys?from=2.3971;48.8237&to=2.3466810000000002;48.837171999999995&datetime=20160225T190000
            """
            self.journey(_from="2.3971;48.8237", to="2.3466810000000002;48.837171999999995", datetime="20160225T190000")


        def test_IdfM_13(self):
            """
            /v1/coverage/stif/journeys?from=2.3971;48.8479&to=2.407993;48.843446&datetime=20151203T210000
            """
            self.journey(_from="2.3971;48.8479", to="2.407993;48.843446", datetime="20151203T210000")


        def test_IdfM_14(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.8462&to=2.406677;48.87672&datetime=20160623T190000
            """
            self.journey(_from="2.3262;48.8462", to="2.406677;48.87672", datetime="20160623T190000")


        def test_IdfM_15(self):
            """
            /v1/coverage/stif/journeys?from=2.5852;48.8522&to=2.598768;48.849463&datetime=20160623T190000
            """
            self.journey(_from="2.5852;48.8522", to="2.598768;48.849463", datetime="20160623T190000")


        def test_IdfM_16(self):
            """
            /v1/coverage/stif/journeys?from=2.303;48.8992&to=2.383508;48.885723999999996&datetime=20160225T190000
            """
            self.journey(_from="2.303;48.8992", to="2.383508;48.885723999999996", datetime="20160225T190000")


        def test_IdfM_17(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.9748&to=2.3658189999999997;48.951377&datetime=20151203T210000
            """
            self.journey(_from="2.3453;48.9748", to="2.3658189999999997;48.951377", datetime="20151203T210000")


        def test_IdfM_18(self):
            """
            /v1/coverage/stif/journeys?from=2.3263;48.7535&to=2.318103;48.760733&datetime=20151203T210000
            """
            self.journey(_from="2.3263;48.7535", to="2.318103;48.760733", datetime="20151203T210000")


        def test_IdfM_19(self):
            """
            /v1/coverage/stif/journeys?from=2.299;48.8605&to=2.315342;48.852458&datetime=20160623T190000
            """
            self.journey(_from="2.299;48.8605", to="2.315342;48.852458", datetime="20160623T190000")


        def test_IdfM_20(self):
            """
            /v1/coverage/stif/journeys?from=2.3017;48.8201&to=2.3330580000000003;48.84077&datetime=20160623T190000
            """
            self.journey(_from="2.3017;48.8201", to="2.3330580000000003;48.84077", datetime="20160623T190000")


        def test_IdfM_21(self):
            """
            /v1/coverage/stif/journeys?from=2.3889;48.8444&to=2.247074;48.926165000000005&datetime=20160225T190000
            """
            self.journey(_from="2.3889;48.8444", to="2.247074;48.926165000000005", datetime="20160225T190000")


        def test_IdfM_22(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8561&to=2.3221540000000003;48.857855&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8561", to="2.3221540000000003;48.857855", datetime="20151203T210000")


        def test_IdfM_23(self):
            """
            /v1/coverage/stif/journeys?from=2.4028;49.0062&to=2.40276;49.008016&datetime=20151203T210000
            """
            self.journey(_from="2.4028;49.0062", to="2.40276;49.008016", datetime="20151203T210000")


        def test_IdfM_24(self):
            """
            /v1/coverage/stif/journeys?from=2.2854;48.8596&to=2.286714;48.86414&datetime=20151203T210000
            """
            self.journey(_from="2.2854;48.8596", to="2.286714;48.86414", datetime="20151203T210000")


        def test_IdfM_25(self):
            """
            /v1/coverage/stif/journeys?from=2.1925;48.9297&to=2.238955;48.891087&datetime=20160225T190000
            """
            self.journey(_from="2.1925;48.9297", to="2.238955;48.891087", datetime="20160225T190000")


        def test_IdfM_26(self):
            """
            /v1/coverage/stif/journeys?from=3.1802;48.9078&to=3.2061830000000002;48.90851&datetime=20151203T210000
            """
            self.journey(_from="3.1802;48.9078", to="3.2061830000000002;48.90851", datetime="20151203T210000")


        def test_IdfM_27(self):
            """
            /v1/coverage/stif/journeys?from=2.4926;48.9&to=2.391659;48.857843&datetime=20160225T190000
            """
            self.journey(_from="2.4926;48.9", to="2.391659;48.857843", datetime="20160225T190000")


        def test_IdfM_28(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8516&to=2.343962;48.874043&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8516", to="2.343962;48.874043", datetime="20160623T190000")


        def test_IdfM_29(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8552&to=2.3494080000000004;48.844366&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8552", to="2.3494080000000004;48.844366", datetime="20160623T190000")


        def test_IdfM_30(self):
            """
            /v1/coverage/stif/journeys?from=2.2677;48.8282&to=2.371245;48.899218&datetime=20160225T190000
            """
            self.journey(_from="2.2677;48.8282", to="2.371245;48.899218", datetime="20160225T190000")


        def test_IdfM_31(self):
            """
            /v1/coverage/stif/journeys?from=2.7855;48.8543&to=2.769429;48.887614&datetime=20180802T180000
            """
            self.journey(_from="2.7855;48.8543", to="2.769429;48.887614", datetime="20180802T180000")


        def test_IdfM_32(self):
            """
            /v1/coverage/stif/journeys?from=2.4107;48.8542&to=2.57088;49.004199&datetime=20160225T190000
            """
            self.journey(_from="2.4107;48.8542", to="2.57088;49.004199", datetime="20160225T190000")


        def test_IdfM_33(self):
            """
            /v1/coverage/stif/journeys?from=2.3712;48.8704&to=2.375316;48.871339&datetime=20151203T210000
            """
            self.journey(_from="2.3712;48.8704", to="2.375316;48.871339", datetime="20151203T210000")


        def test_IdfM_34(self):
            """
            /v1/coverage/stif/journeys?from=2.254;48.8893&to=2.3452889999999997;48.653721999999995&datetime=20160225T190000
            """
            self.journey(_from="2.254;48.8893", to="2.3452889999999997;48.653721999999995", datetime="20160225T190000")


        def test_IdfM_35(self):
            """
            /v1/coverage/stif/journeys?from=2.1993;48.9459&to=2.215696;48.921640000000004&datetime=20160623T190000
            """
            self.journey(_from="2.1993;48.9459", to="2.215696;48.921640000000004", datetime="20160623T190000")


        def test_IdfM_36(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.7949&to=2.348044;48.838971&datetime=20160623T190000
            """
            self.journey(_from="2.3644;48.7949", to="2.348044;48.838971", datetime="20160623T190000")


        def test_IdfM_37(self):
            """
            /v1/coverage/stif/journeys?from=2.0653;48.9663&to=2.342597;48.858755&datetime=20160225T190000
            """
            self.journey(_from="2.0653;48.9663", to="2.342597;48.858755", datetime="20160225T190000")


        def test_IdfM_38(self):
            """
            /v1/coverage/stif/journeys?from=2.2635;48.9145&to=2.3739209999999997;48.829073&datetime=20160225T190000
            """
            self.journey(_from="2.2635;48.9145", to="2.3739209999999997;48.829073", datetime="20160225T190000")


        def test_IdfM_39(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8659&to=2.3494029999999997;48.823683&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8659", to="2.3494029999999997;48.823683", datetime="20160623T190000")


        def test_IdfM_40(self):
            """
            /v1/coverage/stif/journeys?from=2.2117;48.8902&to=2.193946;48.892838&datetime=20160623T190000
            """
            self.journey(_from="2.2117;48.8902", to="2.193946;48.892838", datetime="20160623T190000")


        def test_IdfM_41(self):
            """
            /v1/coverage/stif/journeys?from=2.3371;48.8399&to=2.343957;48.836273&datetime=20151203T210000
            """
            self.journey(_from="2.3371;48.8399", to="2.343957;48.836273", datetime="20151203T210000")


        def test_IdfM_42(self):
            """
            /v1/coverage/stif/journeys?from=2.8984;48.9545&to=2.876582;48.960001&datetime=20151203T210000
            """
            self.journey(_from="2.8984;48.9545", to="2.876582;48.960001", datetime="20151203T210000")


        def test_IdfM_43(self):
            """
            /v1/coverage/stif/journeys?from=2.3781;48.891999999999996&to=3.013129;48.557287&datetime=20180802T180000
            """
            self.journey(_from="2.3781;48.891999999999996", to="3.013129;48.557287", datetime="20180802T180000")


        def test_IdfM_44(self):
            """
            /v1/coverage/stif/journeys?from=2.3058;48.8597&to=2.3071650000000004;48.854255&datetime=20160623T190000
            """
            self.journey(_from="2.3058;48.8597", to="2.3071650000000004;48.854255", datetime="20160623T190000")


        def test_IdfM_45(self):
            """
            /v1/coverage/stif/journeys?from=2.2377;48.8434&to=2.292211;48.813783&datetime=20160225T190000
            """
            self.journey(_from="2.2377;48.8434", to="2.292211;48.813783", datetime="20160225T190000")


        def test_IdfM_46(self):
            """
            /v1/coverage/stif/journeys?from=2.4691;48.775&to=2.341218;48.659118&datetime=20160225T190000
            """
            self.journey(_from="2.4691;48.775", to="2.341218;48.659118", datetime="20160225T190000")


        def test_IdfM_47(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.8435&to=2.341236;48.881237&datetime=20160623T190000
            """
            self.journey(_from="2.3644;48.8435", to="2.341236;48.881237", datetime="20160623T190000")


        def test_IdfM_48(self):
            """
            /v1/coverage/stif/journeys?from=2.3999;48.8794&to=2.333057;48.851561&datetime=20160623T190000
            """
            self.journey(_from="2.3999;48.8794", to="2.333057;48.851561", datetime="20160623T190000")


        def test_IdfM_49(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8839&to=2.32488;48.856057&datetime=20160623T190000
            """
            self.journey(_from="2.3508;48.8839", to="2.32488;48.856057", datetime="20160623T190000")


        def test_IdfM_50(self):
            """
            /v1/coverage/stif/journeys?from=2.3849;48.9019&to=2.53;48.685033000000004&datetime=20160225T190000
            """
            self.journey(_from="2.3849;48.9019", to="2.53;48.685033000000004", datetime="20160225T190000")


        def test_IdfM_51(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.8677&to=2.326238;48.881237&datetime=20160623T190000
            """
            self.journey(_from="2.3644;48.8677", to="2.326238;48.881237", datetime="20160623T190000")


        def test_IdfM_52(self):
            """
            /v1/coverage/stif/journeys?from=2.1411;48.8145&to=2.0512490000000003;48.80534&datetime=20160225T190000
            """
            self.journey(_from="2.1411;48.8145", to="2.0512490000000003;48.80534", datetime="20160225T190000")


        def test_IdfM_53(self):
            """
            /v1/coverage/stif/journeys?from=2.3903;48.8408&to=2.440488;48.7454&datetime=20160225T190000
            """
            self.journey(_from="2.3903;48.8408", to="2.440488;48.7454", datetime="20160225T190000")


        def test_IdfM_54(self):
            """
            /v1/coverage/stif/journeys?from=2.0095;48.5229&to=2.403938;48.867729&datetime=20180802T180000
            """
            self.journey(_from="2.0095;48.5229", to="2.403938;48.867729", datetime="20180802T180000")


        def test_IdfM_55(self):
            """
            /v1/coverage/stif/journeys?from=2.6256;48.5383&to=2.5866;48.596795&datetime=20151203T210000
            """
            self.journey(_from="2.6256;48.5383", to="2.5866;48.596795", datetime="20151203T210000")


        def test_IdfM_56(self):
            """
            /v1/coverage/stif/journeys?from=2.4121;48.8416&to=2.409355;48.843445&datetime=20151203T210000
            """
            self.journey(_from="2.4121;48.8416", to="2.409355;48.843445", datetime="20151203T210000")


        def test_IdfM_57(self):
            """
            /v1/coverage/stif/journeys?from=2.5598;48.6616&to=2.559758;48.658001&datetime=20151203T210000
            """
            self.journey(_from="2.5598;48.6616", to="2.559758;48.658001", datetime="20151203T210000")


        def test_IdfM_58(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8327&to=2.342594;48.828179999999996&datetime=20151203T210000
            """
            self.journey(_from="2.344;48.8327", to="2.342594;48.828179999999996", datetime="20151203T210000")


        def test_IdfM_59(self):
            """
            /v1/coverage/stif/journeys?from=2.1109999999999998;48.836000000000006&to=2.1151150000000003;48.83246&datetime=20151203T210000
            """
            self.journey(_from="2.1109999999999998;48.836000000000006", to="2.1151150000000003;48.83246", datetime="20151203T210000")


        def test_IdfM_60(self):
            """
            /v1/coverage/stif/journeys?from=2.3113;48.83&to=2.316716;48.82638&datetime=20151203T210000
            """
            self.journey(_from="2.3113;48.83", to="2.316716;48.82638", datetime="20151203T210000")


        def test_IdfM_61(self):
            """
            /v1/coverage/stif/journeys?from=2.314;48.8318&to=2.322163;48.829078&datetime=20151203T210000
            """
            self.journey(_from="2.314;48.8318", to="2.322163;48.829078", datetime="20151203T210000")


        def test_IdfM_62(self):
            """
            /v1/coverage/stif/journeys?from=2.3562;48.8309&to=2.3534900000000003;48.828179&datetime=20151203T210000
            """
            self.journey(_from="2.3562;48.8309", to="2.3534900000000003;48.828179", datetime="20151203T210000")


        def test_IdfM_63(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8219&to=2.326248;48.833575&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8219", to="2.326248;48.833575", datetime="20151203T210000")


        def test_IdfM_64(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.9685&to=2.304423;48.879434&datetime=20160225T190000
            """
            self.journey(_from="2.3194;48.9685", to="2.304423;48.879434", datetime="20160225T190000")


        def test_IdfM_65(self):
            """
            /v1/coverage/stif/journeys?from=2.2471;48.91&to=2.3235189999999997;48.85156&datetime=20160225T190000
            """
            self.journey(_from="2.2471;48.91", to="2.3235189999999997;48.85156", datetime="20160225T190000")


        def test_IdfM_66(self):
            """
            /v1/coverage/stif/journeys?from=2.3971;48.856&to=2.3889419999999997;48.865938&datetime=20151203T210000
            """
            self.journey(_from="2.3971;48.856", to="2.3889419999999997;48.865938", datetime="20151203T210000")


        def test_IdfM_67(self):
            """
            /v1/coverage/stif/journeys?from=2.306;48.6159&to=2.307312;48.609654&datetime=20151203T210000
            """
            self.journey(_from="2.306;48.6159", to="2.307312;48.609654", datetime="20151203T210000")


        def test_IdfM_68(self):
            """
            /v1/coverage/stif/journeys?from=3.2302;48.4982&to=3.2922860000000003;48.561577&datetime=20180802T180000
            """
            self.journey(_from="3.2302;48.4982", to="3.2922860000000003;48.561577", datetime="20180802T180000")


        def test_IdfM_69(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.9865&to=2.334421;48.841669&datetime=20160225T190000
            """
            self.journey(_from="2.3194;48.9865", to="2.334421;48.841669", datetime="20160225T190000")


        def test_IdfM_70(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.6744&to=2.3520830000000004;48.676203&datetime=20151203T210000
            """
            self.journey(_from="2.3467;48.6744", to="2.3520830000000004;48.676203", datetime="20151203T210000")


        def test_IdfM_71(self):
            """
            /v1/coverage/stif/journeys?from=2.3985;48.8686&to=2.398482;48.865034&datetime=20151203T210000
            """
            self.journey(_from="2.3985;48.8686", to="2.398482;48.865034", datetime="20151203T210000")


        def test_IdfM_72(self):
            """
            /v1/coverage/stif/journeys?from=2.8255;48.7669&to=2.9095400000000002;48.857321&datetime=20160225T190000
            """
            self.journey(_from="2.8255;48.7669", to="2.9095400000000002;48.857321", datetime="20160225T190000")


        def test_IdfM_73(self):
            """
            /v1/coverage/stif/journeys?from=2.3890000000000002;48.8839&to=2.290827;48.838063&datetime=20160225T190000
            """
            self.journey(_from="2.3890000000000002;48.8839", to="2.290827;48.838063", datetime="20160225T190000")


        def test_IdfM_74(self):
            """
            /v1/coverage/stif/journeys?from=2.3671;48.8273&to=2.3466869999999997;48.867748&datetime=20160623T190000
            """
            self.journey(_from="2.3671;48.8273", to="2.3466869999999997;48.867748", datetime="20160623T190000")


        def test_IdfM_75(self):
            """
            /v1/coverage/stif/journeys?from=2.9175;48.9517&to=2.886152;48.960855&datetime=20180802T180000
            """
            self.journey(_from="2.9175;48.9517", to="2.886152;48.960855", datetime="20180802T180000")


        def test_IdfM_76(self):
            """
            /v1/coverage/stif/journeys?from=2.4353;48.8767&to=2.414845;48.868621000000005&datetime=20160623T190000
            """
            self.journey(_from="2.4353;48.8767", to="2.414845;48.868621000000005", datetime="20160623T190000")


        def test_IdfM_77(self):
            """
            /v1/coverage/stif/journeys?from=2.3017;48.8327&to=2.301732;48.829074&datetime=20151203T210000
            """
            self.journey(_from="2.3017;48.8327", to="2.301732;48.829074", datetime="20151203T210000")


        def test_IdfM_78(self):
            """
            /v1/coverage/stif/journeys?from=2.359;48.8632&to=2.327608;48.847064&datetime=20160623T190000
            """
            self.journey(_from="2.359;48.8632", to="2.327608;48.847064", datetime="20160623T190000")


        def test_IdfM_79(self):
            """
            /v1/coverage/stif/journeys?from=2.235;48.8308&to=2.243153;48.834436&datetime=20151203T210000
            """
            self.journey(_from="2.235;48.8308", to="2.243153;48.834436", datetime="20151203T210000")


        def test_IdfM_80(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8615&to=2.28532;48.893815000000004&datetime=20160623T190000
            """
            self.journey(_from="2.3453;48.8615", to="2.28532;48.893815000000004", datetime="20160623T190000")


        def test_IdfM_81(self):
            """
            /v1/coverage/stif/journeys?from=2.2363;48.8434&to=2.241788;48.836234000000005&datetime=20151203T210000
            """
            self.journey(_from="2.2363;48.8434", to="2.241788;48.836234000000005", datetime="20151203T210000")


        def test_IdfM_82(self):
            """
            /v1/coverage/stif/journeys?from=2.2377;48.8443&to=2.241788;48.836234000000005&datetime=20151203T210000
            """
            self.journey(_from="2.2377;48.8443", to="2.241788;48.836234000000005", datetime="20151203T210000")


        def test_IdfM_83(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.83&to=2.363027;48.832674&datetime=20151203T210000
            """
            self.journey(_from="2.3467;48.83", to="2.363027;48.832674", datetime="20151203T210000")


        def test_IdfM_84(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8758&to=2.361668;48.840767&datetime=20160623T190000
            """
            self.journey(_from="2.3494;48.8758", to="2.361668;48.840767", datetime="20160623T190000")


        def test_IdfM_85(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.83&to=2.32625;48.825482&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.83", to="2.32625;48.825482", datetime="20151203T210000")


        def test_IdfM_86(self):
            """
            /v1/coverage/stif/journeys?from=3.2302;48.4982&to=3.141924;48.479107&datetime=20160225T190000
            """
            self.journey(_from="3.2302;48.4982", to="3.141924;48.479107", datetime="20160225T190000")


        def test_IdfM_87(self):
            """
            /v1/coverage/stif/journeys?from=2.2649;48.8479&to=2.275823;48.853343&datetime=20151203T210000
            """
            self.journey(_from="2.2649;48.8479", to="2.275823;48.853343", datetime="20151203T210000")


        def test_IdfM_88(self):
            """
            /v1/coverage/stif/journeys?from=2.9703;48.9226&to=2.6126139999999998;48.888999&datetime=20180802T180000
            """
            self.journey(_from="2.9703;48.9226", to="2.6126139999999998;48.888999", datetime="20180802T180000")


        def test_IdfM_89(self):
            """
            /v1/coverage/stif/journeys?from=2.2798;48.9747&to=2.3262389999999997;48.874041999999996&datetime=20160225T190000
            """
            self.journey(_from="2.2798;48.9747", to="2.3262389999999997;48.874041999999996", datetime="20160225T190000")


        def test_IdfM_90(self):
            """
            /v1/coverage/stif/journeys?from=2.3916;48.7805&to=2.387507;48.794896&datetime=20160623T190000
            """
            self.journey(_from="2.3916;48.7805", to="2.387507;48.794896", datetime="20160623T190000")


        def test_IdfM_91(self):
            """
            /v1/coverage/stif/journeys?from=2.5233;48.6994&to=2.372566;48.838966&datetime=20160225T190000
            """
            self.journey(_from="2.5233;48.6994", to="2.372566;48.838966", datetime="20160225T190000")


        def test_IdfM_92(self):
            """
            /v1/coverage/stif/journeys?from=2.3835;48.8749&to=2.236189;48.909969&datetime=20160225T190000
            """
            self.journey(_from="2.3835;48.8749", to="2.236189;48.909969", datetime="20160225T190000")


        def test_IdfM_93(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8776&to=2.346691;48.887532&datetime=20151203T210000
            """
            self.journey(_from="2.3453;48.8776", to="2.346691;48.887532", datetime="20151203T210000")


        def test_IdfM_94(self):
            """
            /v1/coverage/stif/journeys?from=2.2029;48.5952&to=2.3534900000000003;48.828179&datetime=20160225T190000
            """
            self.journey(_from="2.2029;48.5952", to="2.3534900000000003;48.828179", datetime="20160225T190000")


        def test_IdfM_95(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.8147&to=2.338507;48.814690999999996&datetime=20151203T210000
            """
            self.journey(_from="2.3467;48.8147", to="2.338507;48.814690999999996", datetime="20151203T210000")


        def test_IdfM_96(self):
            """
            /v1/coverage/stif/journeys?from=2.3263;48.8237&to=2.34396;48.858755&datetime=20160623T190000
            """
            self.journey(_from="2.3263;48.8237", to="2.34396;48.858755", datetime="20160623T190000")


        def test_IdfM_97(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8668&to=2.282609;48.878526&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8668", to="2.282609;48.878526", datetime="20160623T190000")


        def test_IdfM_98(self):
            """
            /v1/coverage/stif/journeys?from=2.4627;48.9369&to=2.305792;48.871340999999994&datetime=20160225T190000
            """
            self.journey(_from="2.4627;48.9369", to="2.305792;48.871340999999994", datetime="20160225T190000")


        def test_IdfM_99(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.7769&to=2.354834;48.776920000000004&datetime=20151203T210000
            """
            self.journey(_from="2.3494;48.7769", to="2.354834;48.776920000000004", datetime="20151203T210000")


        def test_IdfM_100(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8363&to=2.356266;48.963069&datetime=20160225T190000
            """
            self.journey(_from="2.3508;48.8363", to="2.356266;48.963069", datetime="20160225T190000")


        def test_IdfM_101(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.7571&to=2.320824;48.759834000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.7571", to="2.320824;48.759834000000005", datetime="20151203T210000")


        def test_IdfM_102(self):
            """
            /v1/coverage/stif/journeys?from=2.2949;48.873999999999995&to=2.961871;48.683482&datetime=20180802T180000
            """
            self.journey(_from="2.2949;48.873999999999995", to="2.961871;48.683482", datetime="20180802T180000")


        def test_IdfM_103(self):
            """
            /v1/coverage/stif/journeys?from=2.2895;48.7904&to=2.274541;48.789494&datetime=20160623T190000
            """
            self.journey(_from="2.2895;48.7904", to="2.274541;48.789494", datetime="20160623T190000")


        def test_IdfM_104(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8273&to=2.3766689999999997;48.859648&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8273", to="2.3766689999999997;48.859648", datetime="20160623T190000")


        def test_IdfM_105(self):
            """
            /v1/coverage/stif/journeys?from=2.3399;48.883&to=2.337145;48.884834000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3399;48.883", to="2.337145;48.884834000000005", datetime="20151203T210000")


        def test_IdfM_106(self):
            """
            /v1/coverage/stif/journeys?from=2.408;48.8758&to=2.424413;48.883902&datetime=20160623T190000
            """
            self.journey(_from="2.408;48.8758", to="2.424413;48.883902", datetime="20160623T190000")


        def test_IdfM_107(self):
            """
            /v1/coverage/stif/journeys?from=2.3535;48.8498&to=2.352132;48.841668&datetime=20160623T190000
            """
            self.journey(_from="2.3535;48.8498", to="2.352132;48.841668", datetime="20160623T190000")


        def test_IdfM_108(self):
            """
            /v1/coverage/stif/journeys?from=2.588;48.8783&to=2.579793;48.870188&datetime=20160623T190000
            """
            self.journey(_from="2.588;48.8783", to="2.579793;48.870188", datetime="20160623T190000")


        def test_IdfM_109(self):
            """
            /v1/coverage/stif/journeys?from=2.2608;48.8452&to=2.2581279999999997;48.840742&datetime=20151203T210000
            """
            self.journey(_from="2.2608;48.8452", to="2.2581279999999997;48.840742", datetime="20151203T210000")


        def test_IdfM_110(self):
            """
            /v1/coverage/stif/journeys?from=2.8999;48.852&to=2.915002;48.858193&datetime=20180802T180000
            """
            self.journey(_from="2.8999;48.852", to="2.915002;48.858193", datetime="20180802T180000")


        def test_IdfM_111(self):
            """
            /v1/coverage/stif/journeys?from=2.4651;48.793&to=2.57532;48.790162&datetime=20160225T190000
            """
            self.journey(_from="2.4651;48.793", to="2.57532;48.790162", datetime="20160225T190000")


        def test_IdfM_112(self):
            """
            /v1/coverage/stif/journeys?from=2.3726;48.8444&to=2.536135;48.86128&datetime=20160225T190000
            """
            self.journey(_from="2.3726;48.8444", to="2.536135;48.86128", datetime="20160225T190000")


        def test_IdfM_113(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8345&to=2.3466810000000002;48.837171999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3453;48.8345", to="2.3466810000000002;48.837171999999995", datetime="20151203T210000")


        def test_IdfM_114(self):
            """
            /v1/coverage/stif/journeys?from=2.2594;48.8866&to=2.45725;48.929735&datetime=20160225T190000
            """
            self.journey(_from="2.2594;48.8866", to="2.45725;48.929735", datetime="20160225T190000")


        def test_IdfM_115(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8866&to=2.346692;48.890229&datetime=20151203T210000
            """
            self.journey(_from="2.3494;48.8866", to="2.346692;48.890229", datetime="20151203T210000")


        def test_IdfM_116(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8354&to=2.328973;48.830878000000006&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8354", to="2.328973;48.830878000000006", datetime="20151203T210000")


        def test_IdfM_117(self):
            """
            /v1/coverage/stif/journeys?from=2.3099;48.8776&to=2.305788;48.877635999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3099;48.8776", to="2.305788;48.877635999999995", datetime="20151203T210000")


        def test_IdfM_118(self):
            """
            /v1/coverage/stif/journeys?from=1.7168;48.9902&to=1.7112779999999999;48.991036&datetime=20151203T210000
            """
            self.journey(_from="1.7168;48.9902", to="1.7112779999999999;48.991036", datetime="20151203T210000")


        def test_IdfM_119(self):
            """
            /v1/coverage/stif/journeys?from=2.3331;48.8695&to=2.3098799999999997;48.87404&datetime=20160623T190000
            """
            self.journey(_from="2.3331;48.8695", to="2.3098799999999997;48.87404", datetime="20160623T190000")


        def test_IdfM_120(self):
            """
            /v1/coverage/stif/journeys?from=1.8243;48.6373&to=1.822932;48.634574&datetime=20151203T210000
            """
            self.journey(_from="1.8243;48.6373", to="1.822932;48.634574", datetime="20151203T210000")


        def test_IdfM_121(self):
            """
            /v1/coverage/stif/journeys?from=2.2036;48.8713&to=2.0501259999999997;48.76397&datetime=20160225T190000
            """
            self.journey(_from="2.2036;48.8713", to="2.0501259999999997;48.76397", datetime="20160225T190000")


        def test_IdfM_122(self):
            """
            /v1/coverage/stif/journeys?from=2.3876;48.8471&to=2.383477;48.852451&datetime=20151203T210000
            """
            self.journey(_from="2.3876;48.8471", to="2.383477;48.852451", datetime="20151203T210000")


        def test_IdfM_123(self):
            """
            /v1/coverage/stif/journeys?from=2.6587;49.0498&to=2.3425979999999997;48.869546&datetime=20180802T180000
            """
            self.journey(_from="2.6587;49.0498", to="2.3425979999999997;48.869546", datetime="20180802T180000")


        def test_IdfM_124(self):
            """
            /v1/coverage/stif/journeys?from=2.7733;49.0207&to=2.3425990000000003;48.874942&datetime=20180802T180000
            """
            self.journey(_from="2.7733;49.0207", to="2.3425990000000003;48.874942", datetime="20180802T180000")


        def test_IdfM_125(self):
            """
            /v1/coverage/stif/journeys?from=2.2867;48.8929&to=2.399713;48.759818&datetime=20160225T190000
            """
            self.journey(_from="2.2867;48.8929", to="2.399713;48.759818", datetime="20160225T190000")


        def test_IdfM_126(self):
            """
            /v1/coverage/stif/journeys?from=2.4721;48.8713&to=2.371214;48.854254&datetime=20160225T190000
            """
            self.journey(_from="2.4721;48.8713", to="2.371214;48.854254", datetime="20160225T190000")


        def test_IdfM_127(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.848&to=2.326237;48.883035&datetime=20160623T190000
            """
            self.journey(_from="2.3262;48.848", to="2.326237;48.883035", datetime="20160623T190000")


        def test_IdfM_128(self):
            """
            /v1/coverage/stif/journeys?from=2.3794;48.839&to=2.3507740000000004;48.859654&datetime=20160623T190000
            """
            self.journey(_from="2.3794;48.839", to="2.3507740000000004;48.859654", datetime="20160623T190000")


        def test_IdfM_129(self):
            """
            /v1/coverage/stif/journeys?from=2.4475;48.8515&to=2.323509;48.886632&datetime=20160225T190000
            """
            self.journey(_from="2.4475;48.8515", to="2.323509;48.886632", datetime="20160225T190000")


        def test_IdfM_130(self):
            """
            /v1/coverage/stif/journeys?from=2.416;48.7679&to=2.369783;48.749939000000005&datetime=20160623T190000
            """
            self.journey(_from="2.416;48.7679", to="2.369783;48.749939000000005", datetime="20160623T190000")


        def test_IdfM_131(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8659&to=2.3535009999999996;48.862351000000004&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8659", to="2.3535009999999996;48.862351000000004", datetime="20160623T190000")


        def test_IdfM_132(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8138&to=2.4775110000000002;48.855072&datetime=20160225T190000
            """
            self.journey(_from="2.3617;48.8138", to="2.4775110000000002;48.855072", datetime="20160225T190000")


        def test_IdfM_133(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.8803&to=2.350773;48.854258&datetime=20160623T190000
            """
            self.journey(_from="2.3262;48.8803", to="2.350773;48.854258", datetime="20160623T190000")


        def test_IdfM_134(self):
            """
            /v1/coverage/stif/journeys?from=2.2731;48.8237&to=2.255431;48.823654&datetime=20160623T190000
            """
            self.journey(_from="2.2731;48.8237", to="2.255431;48.823654", datetime="20160623T190000")


        def test_IdfM_135(self):
            """
            /v1/coverage/stif/journeys?from=2.3167;48.8767&to=2.338509;48.865949&datetime=20160623T190000
            """
            self.journey(_from="2.3167;48.8767", to="2.338509;48.865949", datetime="20160623T190000")


        def test_IdfM_136(self):
            """
            /v1/coverage/stif/journeys?from=2.329;48.8794&to=2.367131;48.862348&datetime=20160623T190000
            """
            self.journey(_from="2.329;48.8794", to="2.367131;48.862348", datetime="20160623T190000")


        def test_IdfM_137(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8758&to=2.214525;48.843402000000005&datetime=20160623T190000
            """
            self.journey(_from="2.3276;48.8758", to="2.214525;48.843402000000005", datetime="20160623T190000")


        def test_IdfM_138(self):
            """
            /v1/coverage/stif/journeys?from=2.3099;48.873999999999995&to=2.333056;48.869547&datetime=20160623T190000
            """
            self.journey(_from="2.3099;48.873999999999995", to="2.333056;48.869547", datetime="20160623T190000")


        def test_IdfM_139(self):
            """
            /v1/coverage/stif/journeys?from=2.3671;48.8408&to=2.373932;48.844361&datetime=20151203T210000
            """
            self.journey(_from="2.3671;48.8408", to="2.373932;48.844361", datetime="20151203T210000")


        def test_IdfM_140(self):
            """
            /v1/coverage/stif/journeys?from=2.258;48.8992&to=2.266213;48.902798&datetime=20151203T210000
            """
            self.journey(_from="2.258;48.8992", to="2.266213;48.902798", datetime="20151203T210000")


        def test_IdfM_141(self):
            """
            /v1/coverage/stif/journeys?from=2.0627;48.9475&to=2.032825;48.923997&datetime=20160225T190000
            """
            self.journey(_from="2.0627;48.9475", to="2.032825;48.923997", datetime="20160225T190000")


        def test_IdfM_142(self):
            """
            /v1/coverage/stif/journeys?from=2.3017;48.848&to=2.303085;48.842563&datetime=20151203T210000
            """
            self.journey(_from="2.3017;48.848", to="2.303085;48.842563", datetime="20151203T210000")


        def test_IdfM_143(self):
            """
            /v1/coverage/stif/journeys?from=2.9619;48.6835&to=3.0760509999999996;48.689992&datetime=20160225T190000
            """
            self.journey(_from="2.9619;48.6835", to="3.0760509999999996;48.689992", datetime="20160225T190000")


        def test_IdfM_144(self):
            """
            /v1/coverage/stif/journeys?from=2.2880000000000003;48.91&to=2.2908180000000002;48.847955&datetime=20160225T190000
            """
            self.journey(_from="2.2880000000000003;48.91", to="2.2908180000000002;48.847955", datetime="20160225T190000")


        def test_IdfM_145(self):
            """
            /v1/coverage/stif/journeys?from=2.4217;48.8794&to=2.364408;48.867745&datetime=20160623T190000
            """
            self.journey(_from="2.4217;48.8794", to="2.364408;48.867745", datetime="20160623T190000")


        def test_IdfM_146(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8758&to=2.285343;48.871333&datetime=20160623T190000
            """
            self.journey(_from="2.3481;48.8758", to="2.285343;48.871333", datetime="20160623T190000")


        def test_IdfM_147(self):
            """
            /v1/coverage/stif/journeys?from=2.4858;48.8793&to=2.481672;48.880247&datetime=20151203T210000
            """
            self.journey(_from="2.4858;48.8793", to="2.481672;48.880247", datetime="20151203T210000")


        def test_IdfM_148(self):
            """
            /v1/coverage/stif/journeys?from=2.3208;48.8291&to=2.38211;48.847056&datetime=20160225T190000
            """
            self.journey(_from="2.3208;48.8291", to="2.38211;48.847056", datetime="20160225T190000")


        def test_IdfM_149(self):
            """
            /v1/coverage/stif/journeys?from=2.3385;48.8147&to=2.346677;48.814690999999996&datetime=20151203T210000
            """
            self.journey(_from="2.3385;48.8147", to="2.346677;48.814690999999996", datetime="20151203T210000")


        def test_IdfM_150(self):
            """
            /v1/coverage/stif/journeys?from=2.2663;48.8282&to=2.444921;48.909064&datetime=20160225T190000
            """
            self.journey(_from="2.2663;48.8282", to="2.444921;48.909064", datetime="20160225T190000")


        def test_IdfM_151(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8794&to=2.354866;48.866847&datetime=20160623T190000
            """
            self.journey(_from="2.344;48.8794", to="2.354866;48.866847", datetime="20160623T190000")


        def test_IdfM_152(self):
            """
            /v1/coverage/stif/journeys?from=2.1694;48.8874&to=2.1885630000000003;48.868551000000004&datetime=20160623T190000
            """
            self.journey(_from="2.1694;48.8874", to="2.1885630000000003;48.868551000000004", datetime="20160623T190000")


        def test_IdfM_153(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8471&to=2.352131;48.838071&datetime=20160623T190000
            """
            self.journey(_from="2.3181;48.8471", to="2.352131;48.838071", datetime="20160623T190000")


        def test_IdfM_154(self):
            """
            /v1/coverage/stif/journeys?from=2.4951;48.8173&to=2.499192;48.817274&datetime=20151203T210000
            """
            self.journey(_from="2.4951;48.8173", to="2.499192;48.817274", datetime="20151203T210000")


        def test_IdfM_155(self):
            """
            /v1/coverage/stif/journeys?from=2.3521;48.8381&to=2.3371459999999997;48.794008000000005&datetime=20160623T190000
            """
            self.journey(_from="2.3521;48.8381", to="2.3371459999999997;48.794008000000005", datetime="20160623T190000")


        def test_IdfM_156(self):
            """
            /v1/coverage/stif/journeys?from=2.3576;48.8309&to=2.364389;48.832673&datetime=20151203T210000
            """
            self.journey(_from="2.3576;48.8309", to="2.364389;48.832673", datetime="20151203T210000")


        def test_IdfM_157(self):
            """
            /v1/coverage/stif/journeys?from=2.1006;48.7299&to=2.338508;48.851561&datetime=20180802T180000
            """
            self.journey(_from="2.1006;48.7299", to="2.338508;48.851561", datetime="20180802T180000")


        def test_IdfM_158(self):
            """
            /v1/coverage/stif/journeys?from=2.374;48.9685&to=2.346683;48.847064&datetime=20160225T190000
            """
            self.journey(_from="2.374;48.9685", to="2.346683;48.847064", datetime="20160225T190000")


        def test_IdfM_159(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.8803&to=2.346685;48.855158&datetime=20160623T190000
            """
            self.journey(_from="2.3262;48.8803", to="2.346685;48.855158", datetime="20160623T190000")


        def test_IdfM_160(self):
            """
            /v1/coverage/stif/journeys?from=2.1493;48.4395&to=2.306088;48.397431&datetime=20160225T190000
            """
            self.journey(_from="2.1493;48.4395", to="2.306088;48.397431", datetime="20160225T190000")


        def test_IdfM_161(self):
            """
            /v1/coverage/stif/journeys?from=2.3549;48.8327&to=2.34805;48.865949&datetime=20160623T190000
            """
            self.journey(_from="2.3549;48.8327", to="2.34805;48.865949", datetime="20160623T190000")


        def test_IdfM_162(self):
            """
            /v1/coverage/stif/journeys?from=2.3412;48.8606&to=2.256944;48.730131&datetime=20160225T190000
            """
            self.journey(_from="2.3412;48.8606", to="2.256944;48.730131", datetime="20160225T190000")


        def test_IdfM_163(self):
            """
            /v1/coverage/stif/journeys?from=2.3399;48.8686&to=2.490697;48.712071&datetime=20160225T190000
            """
            self.journey(_from="2.3399;48.8686", to="2.490697;48.712071", datetime="20160225T190000")


        def test_IdfM_164(self):
            """
            /v1/coverage/stif/journeys?from=2.2881;48.8533&to=2.282624;48.865037&datetime=20151203T210000
            """
            self.journey(_from="2.2881;48.8533", to="2.282624;48.865037", datetime="20151203T210000")


        def test_IdfM_165(self):
            """
            /v1/coverage/stif/journeys?from=2.6771;48.95&to=2.36576;48.848859999999995&datetime=20180802T180000
            """
            self.journey(_from="2.6771;48.95", to="2.36576;48.848859999999995", datetime="20180802T180000")


        def test_IdfM_166(self):
            """
            /v1/coverage/stif/journeys?from=2.2853;48.8803&to=2.3548459999999998;48.811992&datetime=20160225T190000
            """
            self.journey(_from="2.2853;48.8803", to="2.3548459999999998;48.811992", datetime="20160225T190000")


        def test_IdfM_167(self):
            """
            /v1/coverage/stif/journeys?from=2.6866;48.9446&to=2.640172;48.935691999999996&datetime=20180802T180000
            """
            self.journey(_from="2.6866;48.9446", to="2.640172;48.935691999999996", datetime="20180802T180000")


        def test_IdfM_168(self):
            """
            /v1/coverage/stif/journeys?from=2.3905;49.0026&to=2.3603810000000003;49.001737&datetime=20160225T190000
            """
            self.journey(_from="2.3905;49.0026", to="2.3603810000000003;49.001737", datetime="20160225T190000")


        def test_IdfM_169(self):
            """
            /v1/coverage/stif/journeys?from=2.3208;48.891999999999996&to=2.36849;48.856952&datetime=20160623T190000
            """
            self.journey(_from="2.3208;48.891999999999996", to="2.36849;48.856952", datetime="20160623T190000")


        def test_IdfM_170(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.8893&to=2.2662150000000003;48.901897999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3262;48.8893", to="2.2662150000000003;48.901897999999996", datetime="20160623T190000")


        def test_IdfM_171(self):
            """
            /v1/coverage/stif/journeys?from=2.1858;48.8766&to=2.1721340000000002;48.890111&datetime=20160623T190000
            """
            self.journey(_from="2.1858;48.8766", to="2.1721340000000002;48.890111", datetime="20160623T190000")


        def test_IdfM_172(self):
            """
            /v1/coverage/stif/journeys?from=2.3385;48.8273&to=2.3943119999999998;48.793993&datetime=20160225T190000
            """
            self.journey(_from="2.3385;48.8273", to="2.3943119999999998;48.793993", datetime="20160225T190000")


        def test_IdfM_173(self):
            """
            /v1/coverage/stif/journeys?from=2.3249;48.8758&to=2.3426009999999997;48.895625&datetime=20160623T190000
            """
            self.journey(_from="2.3249;48.8758", to="2.3426009999999997;48.895625", datetime="20160623T190000")


        def test_IdfM_174(self):
            """
            /v1/coverage/stif/journeys?from=2.3208;48.891999999999996&to=2.204873;48.886556&datetime=20160225T190000
            """
            self.journey(_from="2.3208;48.891999999999996", to="2.204873;48.886556", datetime="20160225T190000")


        def test_IdfM_175(self):
            """
            /v1/coverage/stif/journeys?from=2.3739;48.8614&to=2.382119;48.857847&datetime=20151203T210000
            """
            self.journey(_from="2.3739;48.8614", to="2.382119;48.857847", datetime="20151203T210000")


        def test_IdfM_176(self):
            """
            /v1/coverage/stif/journeys?from=2.2323;48.8362&to=2.7786869999999997;48.855204&datetime=20180802T180000
            """
            self.journey(_from="2.2323;48.8362", to="2.7786869999999997;48.855204", datetime="20180802T180000")


        def test_IdfM_177(self):
            """
            /v1/coverage/stif/journeys?from=2.224;48.8884&to=2.380732;48.82997&datetime=20160225T190000
            """
            self.journey(_from="2.224;48.8884", to="2.380732;48.82997", datetime="20160225T190000")


        def test_IdfM_178(self):
            """
            /v1/coverage/stif/journeys?from=2.2839;48.901&to=2.270408;48.826361999999996&datetime=20160225T190000
            """
            self.journey(_from="2.2839;48.901", to="2.270408;48.826361999999996", datetime="20160225T190000")


        def test_IdfM_179(self):
            """
            /v1/coverage/stif/journeys?from=2.6315;48.8467&to=2.8181279999999997;48.846951000000004&datetime=20160225T190000
            """
            self.journey(_from="2.6315;48.8467", to="2.8181279999999997;48.846951000000004", datetime="20160225T190000")


        def test_IdfM_180(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.865&to=2.339872;48.867748&datetime=20151203T210000
            """
            self.journey(_from="2.3467;48.865", to="2.339872;48.867748", datetime="20151203T210000")


        def test_IdfM_181(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.919&to=2.354861;48.852459&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.919", to="2.354861;48.852459", datetime="20160623T190000")


        def test_IdfM_182(self):
            """
            /v1/coverage/stif/journeys?from=2.3045;48.8309&to=2.3085400000000003;48.833572&datetime=20151203T210000
            """
            self.journey(_from="2.3045;48.8309", to="2.3085400000000003;48.833572", datetime="20151203T210000")


        def test_IdfM_183(self):
            """
            /v1/coverage/stif/journeys?from=2.4543;48.8344&to=2.384793;48.80389&datetime=20160225T190000
            """
            self.journey(_from="2.4543;48.8344", to="2.384793;48.80389", datetime="20160225T190000")


        def test_IdfM_184(self):
            """
            /v1/coverage/stif/journeys?from=2.0829;49.0006&to=2.309882;48.869543&datetime=20160225T190000
            """
            self.journey(_from="2.0829;49.0006", to="2.309882;48.869543", datetime="20160225T190000")


        def test_IdfM_185(self):
            """
            /v1/coverage/stif/journeys?from=2.2430000000000003;48.891999999999996&to=2.3194150000000002;48.894725&datetime=20160225T190000
            """
            self.journey(_from="2.2430000000000003;48.891999999999996", to="2.3194150000000002;48.894725", datetime="20160225T190000")


        def test_IdfM_186(self):
            """
            /v1/coverage/stif/journeys?from=2.4393;48.8362&to=2.3657630000000003;48.853356&datetime=20160623T190000
            """
            self.journey(_from="2.4393;48.8362", to="2.3657630000000003;48.853356", datetime="20160623T190000")


        def test_IdfM_187(self):
            """
            /v1/coverage/stif/journeys?from=2.2936;48.812&to=2.383507;48.884825&datetime=20160225T190000
            """
            self.journey(_from="2.2936;48.812", to="2.383507;48.884825", datetime="20160225T190000")


        def test_IdfM_188(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8363&to=2.353493;48.837171999999995&datetime=20151203T210000
            """
            self.journey(_from="2.344;48.8363", to="2.353493;48.837171999999995", datetime="20151203T210000")


        def test_IdfM_189(self):
            """
            /v1/coverage/stif/journeys?from=2.3303;48.8264&to=2.331697;48.833576&datetime=20151203T210000
            """
            self.journey(_from="2.3303;48.8264", to="2.331697;48.833576", datetime="20151203T210000")


        def test_IdfM_190(self):
            """
            /v1/coverage/stif/journeys?from=2.3589;48.785&to=2.429817;48.856919&datetime=20160225T190000
            """
            self.journey(_from="2.3589;48.785", to="2.429817;48.856919", datetime="20160225T190000")


        def test_IdfM_191(self):
            """
            /v1/coverage/stif/journeys?from=2.2908;48.8381&to=2.279963;48.808382&datetime=20160225T190000
            """
            self.journey(_from="2.2908;48.8381", to="2.279963;48.808382", datetime="20160225T190000")


        def test_IdfM_192(self):
            """
            /v1/coverage/stif/journeys?from=2.8984;48.9608&to=2.914704;48.949923&datetime=20151203T210000
            """
            self.journey(_from="2.8984;48.9608", to="2.914704;48.949923", datetime="20151203T210000")


        def test_IdfM_193(self):
            """
            /v1/coverage/stif/journeys?from=2.6983;49.0398&to=2.338509;48.892928000000005&datetime=20180802T180000
            """
            self.journey(_from="2.6983;49.0398", to="2.338509;48.892928000000005", datetime="20180802T180000")


        def test_IdfM_194(self):
            """
            /v1/coverage/stif/journeys?from=2.8061;48.5844&to=2.660984;48.56873&datetime=20160225T190000
            """
            self.journey(_from="2.8061;48.5844", to="2.660984;48.56873", datetime="20160225T190000")


        def test_IdfM_195(self):
            """
            /v1/coverage/stif/journeys?from=2.5414;48.8262&to=2.5305400000000002;48.824419&datetime=20151203T210000
            """
            self.journey(_from="2.5414;48.8262", to="2.5305400000000002;48.824419", datetime="20151203T210000")


        def test_IdfM_196(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.7598&to=2.361636;48.77512&datetime=20160623T190000
            """
            self.journey(_from="2.3181;48.7598", to="2.361636;48.77512", datetime="20160623T190000")


        def test_IdfM_197(self):
            """
            /v1/coverage/stif/journeys?from=2.363;48.8525&to=2.36713;48.86055&datetime=20151203T210000
            """
            self.journey(_from="2.363;48.8525", to="2.36713;48.86055", datetime="20151203T210000")


        def test_IdfM_198(self):
            """
            /v1/coverage/stif/journeys?from=2.2962;48.8812&to=2.397;48.766115&datetime=20160225T190000
            """
            self.journey(_from="2.2962;48.8812", to="2.397;48.766115", datetime="20160225T190000")


        def test_IdfM_199(self):
            """
            /v1/coverage/stif/journeys?from=2.2771;48.8929&to=2.2648099999999998;48.929775&datetime=20160225T190000
            """
            self.journey(_from="2.2771;48.8929", to="2.2648099999999998;48.929775", datetime="20160225T190000")


        def test_IdfM_200(self):
            """
            /v1/coverage/stif/journeys?from=2.363;48.8677&to=2.3562279999999998;48.865947999999996&datetime=20151203T210000
            """
            self.journey(_from="2.363;48.8677", to="2.3562279999999998;48.865947999999996", datetime="20151203T210000")


        def test_IdfM_201(self):
            """
            /v1/coverage/stif/journeys?from=2.6219;48.8449&to=2.704489;48.404033&datetime=20180802T180000
            """
            self.journey(_from="2.6219;48.8449", to="2.704489;48.404033", datetime="20180802T180000")


        def test_IdfM_202(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8992&to=2.264805;48.933372&datetime=20160225T190000
            """
            self.journey(_from="2.3453;48.8992", to="2.264805;48.933372", datetime="20160225T190000")


        def test_IdfM_203(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.9406&to=2.279897;48.865935&datetime=20160225T190000
            """
            self.journey(_from="2.3453;48.9406", to="2.279897;48.865935", datetime="20160225T190000")


        def test_IdfM_204(self):
            """
            /v1/coverage/stif/journeys?from=2.359;48.8659&to=2.3698509999999997;48.853355&datetime=20151203T210000
            """
            self.journey(_from="2.359;48.8659", to="2.3698509999999997;48.853355", datetime="20151203T210000")


        def test_IdfM_205(self):
            """
            /v1/coverage/stif/journeys?from=2.8779;48.9555&to=2.884776;48.959962&datetime=20151203T210000
            """
            self.journey(_from="2.8779;48.9555", to="2.884776;48.959962", datetime="20151203T210000")


        def test_IdfM_206(self):
            """
            /v1/coverage/stif/journeys?from=2.2362;48.8911&to=2.260782;48.886607&datetime=20151203T210000
            """
            self.journey(_from="2.2362;48.8911", to="2.260782;48.886607", datetime="20151203T210000")


        def test_IdfM_207(self):
            """
            /v1/coverage/stif/journeys?from=2.2321;48.8866&to=2.301702;48.871340000000004&datetime=20160623T190000
            """
            self.journey(_from="2.2321;48.8866", to="2.301702;48.871340000000004", datetime="20160623T190000")


        def test_IdfM_208(self):
            """
            /v1/coverage/stif/journeys?from=2.2732;48.776&to=2.320797;48.839869&datetime=20160225T190000
            """
            self.journey(_from="2.2732;48.776", to="2.320797;48.839869", datetime="20160225T190000")


        def test_IdfM_209(self):
            """
            /v1/coverage/stif/journeys?from=2.3589;48.8363&to=2.330333;48.846165&datetime=20160623T190000
            """
            self.journey(_from="2.3589;48.8363", to="2.330333;48.846165", datetime="20160623T190000")


        def test_IdfM_210(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8704&to=2.353503;48.869545&datetime=20151203T210000
            """
            self.journey(_from="2.3494;48.8704", to="2.353503;48.869545", datetime="20151203T210000")


        def test_IdfM_211(self):
            """
            /v1/coverage/stif/journeys?from=2.3331;48.8327&to=2.339872;48.878539&datetime=20160623T190000
            """
            self.journey(_from="2.3331;48.8327", to="2.339872;48.878539", datetime="20160623T190000")


        def test_IdfM_212(self):
            """
            /v1/coverage/stif/journeys?from=2.3480000000000003;48.8624&to=2.343961;48.86505&datetime=20151203T210000
            """
            self.journey(_from="2.3480000000000003;48.8624", to="2.343961;48.86505", datetime="20151203T210000")


        def test_IdfM_213(self):
            """
            /v1/coverage/stif/journeys?from=2.4161;48.8228&to=2.455514;48.774162&datetime=20160623T190000
            """
            self.journey(_from="2.4161;48.8228", to="2.455514;48.774162", datetime="20160623T190000")


        def test_IdfM_214(self):
            """
            /v1/coverage/stif/journeys?from=2.483;48.8542&to=2.720543;48.737608&datetime=20180802T180000
            """
            self.journey(_from="2.483;48.8542", to="2.720543;48.737608", datetime="20180802T180000")


        def test_IdfM_215(self):
            """
            /v1/coverage/stif/journeys?from=2.3589;48.8516&to=2.343962;48.87764&datetime=20160623T190000
            """
            self.journey(_from="2.3589;48.8516", to="2.343962;48.87764", datetime="20160623T190000")


        def test_IdfM_216(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8552&to=2.350773;48.854258&datetime=20151203T210000
            """
            self.journey(_from="2.3453;48.8552", to="2.350773;48.854258", datetime="20151203T210000")


        def test_IdfM_217(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8615&to=2.3807560000000003;48.856947999999996&datetime=20160623T190000
            """
            self.journey(_from="2.344;48.8615", to="2.3807560000000003;48.856947999999996", datetime="20160623T190000")


        def test_IdfM_218(self):
            """
            /v1/coverage/stif/journeys?from=2.3957;48.8399&to=2.387556;48.843457&datetime=20151203T210000
            """
            self.journey(_from="2.3957;48.8399", to="2.387556;48.843457", datetime="20151203T210000")


        def test_IdfM_219(self):
            """
            /v1/coverage/stif/journeys?from=2.6145;48.9798&to=2.6485939999999997;48.972539000000005&datetime=20151203T210000
            """
            self.journey(_from="2.6145;48.9798", to="2.6485939999999997;48.972539000000005", datetime="20151203T210000")


        def test_IdfM_220(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.883&to=2.3180560000000003;48.883034&datetime=20151203T210000
            """
            self.journey(_from="2.3262;48.883", to="2.3180560000000003;48.883034", datetime="20151203T210000")


        def test_IdfM_221(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.8794&to=2.346684;48.848863&datetime=20160623T190000
            """
            self.journey(_from="2.3194;48.8794", to="2.346684;48.848863", datetime="20160623T190000")


        def test_IdfM_222(self):
            """
            /v1/coverage/stif/journeys?from=2.2279;48.9513&to=2.378002;48.822777&datetime=20160225T190000
            """
            self.journey(_from="2.2279;48.9513", to="2.378002;48.822777", datetime="20160225T190000")


        def test_IdfM_223(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.873999999999995&to=2.331693;48.870446&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.873999999999995", to="2.331693;48.870446", datetime="20151203T210000")


        def test_IdfM_224(self):
            """
            /v1/coverage/stif/journeys?from=2.3426;48.8785&to=2.369843;48.840765000000005&datetime=20160623T190000
            """
            self.journey(_from="2.3426;48.8785", to="2.369843;48.840765000000005", datetime="20160623T190000")


        def test_IdfM_225(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8776&to=2.323513;48.871344&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8776", to="2.323513;48.871344", datetime="20151203T210000")


        def test_IdfM_226(self):
            """
            /v1/coverage/stif/journeys?from=2.3726;48.8426&to=2.46659;48.847891&datetime=20160623T190000
            """
            self.journey(_from="2.3726;48.8426", to="2.46659;48.847891", datetime="20160623T190000")


        def test_IdfM_227(self):
            """
            /v1/coverage/stif/journeys?from=2.3303;48.8938&to=2.3248729999999997;48.887531&datetime=20151203T210000
            """
            self.journey(_from="2.3303;48.8938", to="2.3248729999999997;48.887531", datetime="20151203T210000")


        def test_IdfM_228(self):
            """
            /v1/coverage/stif/journeys?from=2.3235;48.891999999999996&to=2.327599;48.892927&datetime=20151203T210000
            """
            self.journey(_from="2.3235;48.891999999999996", to="2.327599;48.892927", datetime="20151203T210000")


        def test_IdfM_229(self):
            """
            /v1/coverage/stif/journeys?from=2.4955;48.9558&to=2.5105310000000003;48.944953999999996&datetime=20160623T190000
            """
            self.journey(_from="2.4955;48.9558", to="2.5105310000000003;48.944953999999996", datetime="20160623T190000")


        def test_IdfM_230(self):
            """
            /v1/coverage/stif/journeys?from=2.7895;48.848&to=2.785031;48.803021&datetime=20180802T180000
            """
            self.journey(_from="2.7895;48.848", to="2.785031;48.803021", datetime="20180802T180000")


        def test_IdfM_231(self):
            """
            /v1/coverage/stif/journeys?from=2.3767;48.8516&to=2.3644;48.854256&datetime=20151203T210000
            """
            self.journey(_from="2.3767;48.8516", to="2.3644;48.854256", datetime="20151203T210000")


        def test_IdfM_232(self):
            """
            /v1/coverage/stif/journeys?from=2.2376;48.8785&to=2.354857;48.842566999999995&datetime=20160225T190000
            """
            self.journey(_from="2.2376;48.8785", to="2.354857;48.842566999999995", datetime="20160225T190000")


        def test_IdfM_233(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8624&to=2.3466869999999997;48.865949&datetime=20151203T210000
            """
            self.journey(_from="2.3508;48.8624", to="2.3466869999999997;48.865949", datetime="20151203T210000")


        def test_IdfM_234(self):
            """
            /v1/coverage/stif/journeys?from=2.3086;48.7616&to=2.312652;48.780516&datetime=20160623T190000
            """
            self.journey(_from="2.3086;48.7616", to="2.312652;48.780516", datetime="20160623T190000")


        def test_IdfM_235(self):
            """
            /v1/coverage/stif/journeys?from=3.1210000000000004;48.9568&to=3.12887;48.93695&datetime=20180802T180000
            """
            self.journey(_from="3.1210000000000004;48.9568", to="3.12887;48.93695", datetime="20180802T180000")


        def test_IdfM_236(self):
            """
            /v1/coverage/stif/journeys?from=2.2144;48.9037&to=2.346686;48.862352&datetime=20160623T190000
            """
            self.journey(_from="2.2144;48.9037", to="2.346686;48.862352", datetime="20160623T190000")


        def test_IdfM_237(self):
            """
            /v1/coverage/stif/journeys?from=3.1305;48.9504&to=3.12887;48.93695&datetime=20180802T180000
            """
            self.journey(_from="3.1305;48.9504", to="3.12887;48.93695", datetime="20180802T180000")


        def test_IdfM_238(self):
            """
            /v1/coverage/stif/journeys?from=2.3235;48.8417&to=2.327609;48.83987&datetime=20151203T210000
            """
            self.journey(_from="2.3235;48.8417", to="2.327609;48.83987", datetime="20151203T210000")


        def test_IdfM_239(self):
            """
            /v1/coverage/stif/journeys?from=2.2935;48.8444&to=2.348046;48.847964000000005&datetime=20160623T190000
            """
            self.journey(_from="2.2935;48.8444", to="2.348046;48.847964000000005", datetime="20160623T190000")


        def test_IdfM_240(self):
            """
            /v1/coverage/stif/journeys?from=2.3549;48.8659&to=2.3521259999999997;48.821884000000004&datetime=20160623T190000
            """
            self.journey(_from="2.3549;48.8659", to="2.3521259999999997;48.821884000000004", datetime="20160623T190000")


        def test_IdfM_241(self):
            """
            /v1/coverage/stif/journeys?from=2.3358;48.8372&to=2.322163;48.829078&datetime=20151203T210000
            """
            self.journey(_from="2.3358;48.8372", to="2.322163;48.829078", datetime="20151203T210000")


        def test_IdfM_242(self):
            """
            /v1/coverage/stif/journeys?from=2.3521;48.8686&to=2.3575939999999997;48.872243&datetime=20151203T210000
            """
            self.journey(_from="2.3521;48.8686", to="2.3575939999999997;48.872243", datetime="20151203T210000")


        def test_IdfM_243(self):
            """
            /v1/coverage/stif/journeys?from=2.3562;48.8722&to=2.3521400000000003;48.868646000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3562;48.8722", to="2.3521400000000003;48.868646000000005", datetime="20151203T210000")


        def test_IdfM_244(self):
            """
            /v1/coverage/stif/journeys?from=2.2019;48.9801&to=2.231925;48.9909&datetime=20160225T190000
            """
            self.journey(_from="2.2019;48.9801", to="2.231925;48.9909", datetime="20160225T190000")


        def test_IdfM_245(self):
            """
            /v1/coverage/stif/journeys?from=2.4052;48.8264&to=2.38217;48.913602000000004&datetime=20160225T190000
            """
            self.journey(_from="2.4052;48.8264", to="2.38217;48.913602000000004", datetime="20160225T190000")


        def test_IdfM_246(self):
            """
            /v1/coverage/stif/journeys?from=2.3099;48.8453&to=2.303085;48.842563&datetime=20151203T210000
            """
            self.journey(_from="2.3099;48.8453", to="2.303085;48.842563", datetime="20151203T210000")


        def test_IdfM_247(self):
            """
            /v1/coverage/stif/journeys?from=2.55;48.9062&to=2.545834;48.899032&datetime=20160623T190000
            """
            self.journey(_from="2.55;48.9062", to="2.545834;48.899032", datetime="20160623T190000")


        def test_IdfM_248(self):
            """
            /v1/coverage/stif/journeys?from=2.4626;48.8956&to=2.401211;48.866831&datetime=20160225T190000
            """
            self.journey(_from="2.4626;48.8956", to="2.401211;48.866831", datetime="20160225T190000")


        def test_IdfM_249(self):
            """
            /v1/coverage/stif/journeys?from=2.2854;48.8462&to=2.285364;48.851549&datetime=20151203T210000
            """
            self.journey(_from="2.2854;48.8462", to="2.285364;48.851549", datetime="20151203T210000")


        def test_IdfM_250(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8417&to=2.323484;48.97566&datetime=20160225T190000
            """
            self.journey(_from="2.3181;48.8417", to="2.323484;48.97566", datetime="20160225T190000")


        def test_IdfM_251(self):
            """
            /v1/coverage/stif/journeys?from=2.2391;48.8416&to=2.319433;48.846164&datetime=20160623T190000
            """
            self.journey(_from="2.2391;48.8416", to="2.319433;48.846164", datetime="20160623T190000")


        def test_IdfM_252(self):
            """
            /v1/coverage/stif/journeys?from=2.3699;48.9721&to=2.3235189999999997;48.85156&datetime=20160225T190000
            """
            self.journey(_from="2.3699;48.9721", to="2.3235189999999997;48.85156", datetime="20160225T190000")


        def test_IdfM_253(self):
            """
            /v1/coverage/stif/journeys?from=2.2609;48.8371&to=2.207764;48.823609999999995&datetime=20160623T190000
            """
            self.journey(_from="2.2609;48.8371", to="2.207764;48.823609999999995", datetime="20160623T190000")


        def test_IdfM_254(self):
            """
            /v1/coverage/stif/journeys?from=2.3521;48.8471&to=2.350772;48.850660999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3521;48.8471", to="2.350772;48.850660999999995", datetime="20151203T210000")


        def test_IdfM_255(self):
            """
            /v1/coverage/stif/journeys?from=2.3930000000000002;48.8569&to=2.388931;48.855146999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3930000000000002;48.8569", to="2.388931;48.855146999999995", datetime="20151203T210000")


        def test_IdfM_256(self):
            """
            /v1/coverage/stif/journeys?from=2.3085;48.848&to=2.25256;48.909982&datetime=20160225T190000
            """
            self.journey(_from="2.3085;48.848", to="2.25256;48.909982", datetime="20160225T190000")


        def test_IdfM_257(self):
            """
            /v1/coverage/stif/journeys?from=2.2853;48.9109&to=2.255268;48.922574&datetime=20160623T190000
            """
            self.journey(_from="2.2853;48.9109", to="2.255268;48.922574", datetime="20160623T190000")


        def test_IdfM_258(self):
            """
            /v1/coverage/stif/journeys?from=2.3794;48.8569&to=2.375307;48.860548&datetime=20151203T210000
            """
            self.journey(_from="2.3794;48.8569", to="2.375307;48.860548", datetime="20151203T210000")


        def test_IdfM_259(self):
            """
            /v1/coverage/stif/journeys?from=2.3781;48.9703&to=2.3904099999999997;48.963958&datetime=20160623T190000
            """
            self.journey(_from="2.3781;48.9703", to="2.3904099999999997;48.963958", datetime="20160623T190000")


        def test_IdfM_260(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8309&to=2.313989;48.831775&datetime=20151203T210000
            """
            self.journey(_from="2.3181;48.8309", to="2.313989;48.831775", datetime="20151203T210000")


        def test_IdfM_261(self):
            """
            /v1/coverage/stif/journeys?from=2.4094;48.8641&to=2.410756;48.869523&datetime=20151203T210000
            """
            self.journey(_from="2.4094;48.8641", to="2.410756;48.869523", datetime="20151203T210000")


        def test_IdfM_262(self):
            """
            /v1/coverage/stif/journeys?from=2.3562;48.8659&to=2.333053;48.910913&datetime=20160623T190000
            """
            self.journey(_from="2.3562;48.8659", to="2.333053;48.910913", datetime="20160623T190000")


        def test_IdfM_263(self):
            """
            /v1/coverage/stif/journeys?from=2.3385;48.8516&to=2.3248830000000003;48.844366&datetime=20151203T210000
            """
            self.journey(_from="2.3385;48.8516", to="2.3248830000000003;48.844366", datetime="20151203T210000")


        def test_IdfM_264(self):
            """
            /v1/coverage/stif/journeys?from=2.363;48.8012&to=2.365748;48.827277&datetime=20160225T190000
            """
            self.journey(_from="2.363;48.8012", to="2.365748;48.827277", datetime="20160225T190000")


        def test_IdfM_265(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.8363&to=2.339872;48.87764&datetime=20160623T190000
            """
            self.journey(_from="2.3194;48.8363", to="2.339872;48.87764", datetime="20160623T190000")


        def test_IdfM_266(self):
            """
            /v1/coverage/stif/journeys?from=2.5252;48.8406&to=2.529233;48.838809999999995&datetime=20151203T210000
            """
            self.journey(_from="2.5252;48.8406", to="2.529233;48.838809999999995", datetime="20151203T210000")


        def test_IdfM_267(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.848&to=2.324882;48.850660999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3194;48.848", to="2.324882;48.850660999999995", datetime="20151203T210000")


        def test_IdfM_268(self):
            """
            /v1/coverage/stif/journeys?from=2.3249;48.8507&to=2.316707;48.847063&datetime=20151203T210000
            """
            self.journey(_from="2.3249;48.8507", to="2.316707;48.847063", datetime="20151203T210000")


        def test_IdfM_269(self):
            """
            /v1/coverage/stif/journeys?from=2.2854;48.8471&to=2.2908169999999997;48.848853999999996&datetime=20151203T210000
            """
            self.journey(_from="2.2854;48.8471", to="2.2908169999999997;48.848853999999996", datetime="20151203T210000")


        def test_IdfM_270(self):
            """
            /v1/coverage/stif/journeys?from=2.4095;48.9208&to=2.439459;48.906371&datetime=20160623T190000
            """
            self.journey(_from="2.4095;48.9208", to="2.439459;48.906371", datetime="20160623T190000")


        def test_IdfM_271(self):
            """
            /v1/coverage/stif/journeys?from=2.3767;48.9073&to=2.274416;48.888414000000004&datetime=20160225T190000
            """
            self.journey(_from="2.3767;48.9073", to="2.274416;48.888414000000004", datetime="20160225T190000")


        def test_IdfM_272(self):
            """
            /v1/coverage/stif/journeys?from=2.6454;48.6776&to=2.635613;48.858365&datetime=20180802T180000
            """
            self.journey(_from="2.6454;48.6776", to="2.635613;48.858365", datetime="20180802T180000")


        def test_IdfM_273(self):
            """
            /v1/coverage/stif/journeys?from=2.479;48.9144&to=2.390257;48.820974&datetime=20160225T190000
            """
            self.journey(_from="2.479;48.9144", to="2.390257;48.820974", datetime="20160225T190000")


        def test_IdfM_274(self):
            """
            /v1/coverage/stif/journeys?from=2.0916;48.8963&to=2.169579;48.838848&datetime=20160225T190000
            """
            self.journey(_from="2.0916;48.8963", to="2.169579;48.838848", datetime="20160225T190000")


        def test_IdfM_275(self):
            """
            /v1/coverage/stif/journeys?from=2.3208;48.8884&to=2.341236;48.882135999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3208;48.8884", to="2.341236;48.882135999999996", datetime="20160623T190000")


        def test_IdfM_276(self):
            """
            /v1/coverage/stif/journeys?from=2.4994;48.8658&to=2.343961;48.869546&datetime=20160225T190000
            """
            self.journey(_from="2.4994;48.8658", to="2.343961;48.869546", datetime="20160225T190000")


        def test_IdfM_277(self):
            """
            /v1/coverage/stif/journeys?from=3.2937;48.5625&to=3.0760509999999996;48.689992&datetime=20180802T180000
            """
            self.journey(_from="3.2937;48.5625", to="3.0760509999999996;48.689992", datetime="20180802T180000")


        def test_IdfM_278(self):
            """
            /v1/coverage/stif/journeys?from=2.3576;48.8588&to=2.3494040000000003;48.828179&datetime=20160623T190000
            """
            self.journey(_from="2.3576;48.8588", to="2.3494040000000003;48.828179", datetime="20160623T190000")


        def test_IdfM_279(self):
            """
            /v1/coverage/stif/journeys?from=2.3603;48.8354&to=2.692838;48.475112&datetime=20180802T180000
            """
            self.journey(_from="2.3603;48.8354", to="2.692838;48.475112", datetime="20180802T180000")


        def test_IdfM_280(self):
            """
            /v1/coverage/stif/journeys?from=2.1706;48.9459&to=2.3630240000000002;48.827278&datetime=20160225T190000
            """
            self.journey(_from="2.1706;48.9459", to="2.3630240000000002;48.827278", datetime="20160225T190000")


        def test_IdfM_281(self):
            """
            /v1/coverage/stif/journeys?from=2.3739;48.8462&to=2.391649;48.84885&datetime=20151203T210000
            """
            self.journey(_from="2.3739;48.8462", to="2.391649;48.84885", datetime="20151203T210000")


        def test_IdfM_282(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.9388&to=2.4326950000000003;48.936053&datetime=20160225T190000
            """
            self.journey(_from="2.3467;48.9388", to="2.4326950000000003;48.936053", datetime="20160225T190000")


        def test_IdfM_283(self):
            """
            /v1/coverage/stif/journeys?from=2.4053;48.8533&to=2.406637;48.847943&datetime=20151203T210000
            """
            self.journey(_from="2.4053;48.8533", to="2.406637;48.847943", datetime="20151203T210000")


        def test_IdfM_284(self):
            """
            /v1/coverage/stif/journeys?from=2.4053;48.856&to=2.4025540000000003;48.851541999999995&datetime=20151203T210000
            """
            self.journey(_from="2.4053;48.856", to="2.4025540000000003;48.851541999999995", datetime="20151203T210000")


        def test_IdfM_285(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8677&to=2.378089;48.928891&datetime=20160225T190000
            """
            self.journey(_from="2.3481;48.8677", to="2.378089;48.928891", datetime="20160225T190000")


        def test_IdfM_286(self):
            """
            /v1/coverage/stif/journeys?from=2.3535;48.7508&to=2.303097;48.824578&datetime=20160225T190000
            """
            self.journey(_from="2.3535;48.7508", to="2.303097;48.824578", datetime="20160225T190000")


        def test_IdfM_287(self):
            """
            /v1/coverage/stif/journeys?from=2.2991;48.7382&to=2.285396;48.820974&datetime=20160225T190000
            """
            self.journey(_from="2.2991;48.7382", to="2.285396;48.820974", datetime="20160225T190000")


        def test_IdfM_288(self):
            """
            /v1/coverage/stif/journeys?from=2.2771;48.8965&to=2.251236;48.8866&datetime=20160623T190000
            """
            self.journey(_from="2.2771;48.8965", to="2.251236;48.8866", datetime="20160623T190000")


        def test_IdfM_289(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.848&to=2.364229;48.539513&datetime=20180802T180000
            """
            self.journey(_from="2.3644;48.848", to="2.364229;48.539513", datetime="20180802T180000")


        def test_IdfM_290(self):
            """
            /v1/coverage/stif/journeys?from=2.2513;48.8219&to=2.364374;48.805695&datetime=20160225T190000
            """
            self.journey(_from="2.2513;48.8219", to="2.364374;48.805695", datetime="20160225T190000")


        def test_IdfM_291(self):
            """
            /v1/coverage/stif/journeys?from=2.1452;48.7983&to=2.371214;48.854254&datetime=20160225T190000
            """
            self.journey(_from="2.1452;48.7983", to="2.371214;48.854254", datetime="20160225T190000")


        def test_IdfM_292(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.883&to=2.326237;48.883035&datetime=20151203T210000
            """
            self.journey(_from="2.3181;48.883", to="2.326237;48.883035", datetime="20151203T210000")


        def test_IdfM_293(self):
            """
            /v1/coverage/stif/journeys?from=2.3917;48.8578&to=2.492642;48.900016&datetime=20160225T190000
            """
            self.journey(_from="2.3917;48.8578", to="2.492642;48.900016", datetime="20160225T190000")


        def test_IdfM_294(self):
            """
            /v1/coverage/stif/journeys?from=2.2675;48.9298&to=2.2389509999999997;48.892885&datetime=20160225T190000
            """
            self.journey(_from="2.2675;48.9298", to="2.2389509999999997;48.892885", datetime="20160225T190000")


        def test_IdfM_295(self):
            """
            /v1/coverage/stif/journeys?from=2.2512;48.9244&to=2.343959;48.853359000000005&datetime=20160225T190000
            """
            self.journey(_from="2.2512;48.9244", to="2.343959;48.853359000000005", datetime="20160225T190000")


        def test_IdfM_296(self):
            """
            /v1/coverage/stif/journeys?from=2.4477;48.9468&to=2.330332;48.855158&datetime=20160225T190000
            """
            self.journey(_from="2.4477;48.9468", to="2.330332;48.855158", datetime="20160225T190000")


        def test_IdfM_297(self):
            """
            /v1/coverage/stif/journeys?from=2.3371;48.8776&to=2.964743;49.019805&datetime=20180802T180000
            """
            self.journey(_from="2.3371;48.8776", to="2.964743;49.019805", datetime="20180802T180000")


        def test_IdfM_298(self):
            """
            /v1/coverage/stif/journeys?from=2.4530000000000003;48.8488&to=2.3752869999999997;48.833569&datetime=20160225T190000
            """
            self.journey(_from="2.4530000000000003;48.8488", to="2.3752869999999997;48.833569", datetime="20160225T190000")


        def test_IdfM_299(self):
            """
            /v1/coverage/stif/journeys?from=2.9419;48.93899999999999&to=2.944764;48.951566&datetime=20180802T180000
            """
            self.journey(_from="2.9419;48.93899999999999", to="2.944764;48.951566", datetime="20180802T180000")


        def test_IdfM_300(self):
            """
            /v1/coverage/stif/journeys?from=2.3303;48.8462&to=2.358942;48.836271&datetime=20160623T190000
            """
            self.journey(_from="2.3303;48.8462", to="2.358942;48.836271", datetime="20160623T190000")


        def test_IdfM_301(self):
            """
            /v1/coverage/stif/journeys?from=2.2648;48.9271&to=2.350781;48.883035&datetime=20160225T190000
            """
            self.journey(_from="2.2648;48.9271", to="2.350781;48.883035", datetime="20160225T190000")


        def test_IdfM_302(self):
            """
            /v1/coverage/stif/journeys?from=2.3399;48.8668&to=2.330333;48.846165&datetime=20160623T190000
            """
            self.journey(_from="2.3399;48.8668", to="2.330333;48.846165", datetime="20160623T190000")


        def test_IdfM_303(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8282&to=2.313989;48.832674&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8282", to="2.313989;48.832674", datetime="20151203T210000")


        def test_IdfM_304(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8821&to=2.3684990000000004;48.870442&datetime=20160623T190000
            """
            self.journey(_from="2.3481;48.8821", to="2.3684990000000004;48.870442", datetime="20160623T190000")


        def test_IdfM_305(self):
            """
            /v1/coverage/stif/journeys?from=2.4023;48.6537&to=2.32079;48.862351000000004&datetime=20160225T190000
            """
            self.journey(_from="2.4023;48.6537", to="2.32079;48.862351000000004", datetime="20160225T190000")


        def test_IdfM_306(self):
            """
            /v1/coverage/stif/journeys?from=2.423;48.8551&to=2.439464;48.909069&datetime=20160225T190000
            """
            self.journey(_from="2.423;48.8551", to="2.439464;48.909069", datetime="20160225T190000")


        def test_IdfM_307(self):
            """
            /v1/coverage/stif/journeys?from=2.5293;48.8649&to=2.508845;48.852331&datetime=20160623T190000
            """
            self.journey(_from="2.5293;48.8649", to="2.508845;48.852331", datetime="20160623T190000")


        def test_IdfM_308(self):
            """
            /v1/coverage/stif/journeys?from=2.5107;48.9791&to=2.782928;48.872274&datetime=20160225T190000
            """
            self.journey(_from="2.5107;48.9791", to="2.782928;48.872274", datetime="20160225T190000")


        def test_IdfM_309(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8426&to=2.356218;48.83807&datetime=20151203T210000
            """
            self.journey(_from="2.3617;48.8426", to="2.356218;48.83807", datetime="20151203T210000")


        def test_IdfM_310(self):
            """
            /v1/coverage/stif/journeys?from=2.1652;48.9342&to=2.1775830000000003;48.891917&datetime=20160225T190000
            """
            self.journey(_from="2.1652;48.9342", to="2.1775830000000003;48.891917", datetime="20160225T190000")


        def test_IdfM_311(self):
            """
            /v1/coverage/stif/journeys?from=2.3331;48.8534&to=2.319436;48.836271999999994&datetime=20160623T190000
            """
            self.journey(_from="2.3331;48.8534", to="2.319436;48.836271999999994", datetime="20160623T190000")


        def test_IdfM_312(self):
            """
            /v1/coverage/stif/journeys?from=3.0318;48.8306&to=2.37393;48.840764&datetime=20180802T180000
            """
            self.journey(_from="3.0318;48.8306", to="2.37393;48.840764", datetime="20180802T180000")


        def test_IdfM_313(self):
            """
            /v1/coverage/stif/journeys?from=2.3998;48.8399&to=2.720784;48.41567&datetime=20180802T180000
            """
            self.journey(_from="2.3998;48.8399", to="2.720784;48.41567", datetime="20180802T180000")


        def test_IdfM_314(self):
            """
            /v1/coverage/stif/journeys?from=2.3876;48.8767&to=2.391675;48.872231&datetime=20151203T210000
            """
            self.journey(_from="2.3876;48.8767", to="2.391675;48.872231", datetime="20151203T210000")


        def test_IdfM_315(self):
            """
            /v1/coverage/stif/journeys?from=2.2773;48.7958&to=2.3113080000000004;48.749041&datetime=20160225T190000
            """
            self.journey(_from="2.2773;48.7958", to="2.3113080000000004;48.749041", datetime="20160225T190000")


        def test_IdfM_316(self):
            """
            /v1/coverage/stif/journeys?from=2.5264;48.818999999999996&to=2.477531;48.862266&datetime=20160225T190000
            """
            self.journey(_from="2.5264;48.818999999999996", to="2.477531;48.862266", datetime="20160225T190000")


        def test_IdfM_317(self):
            """
            /v1/coverage/stif/journeys?from=2.5306;48.8442&to=2.519714;48.843322&datetime=20151203T210000
            """
            self.journey(_from="2.5306;48.8442", to="2.519714;48.843322", datetime="20151203T210000")


        def test_IdfM_318(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8704&to=2.356215;48.831776&datetime=20160623T190000
            """
            self.journey(_from="2.3494;48.8704", to="2.356215;48.831776", datetime="20160623T190000")


        def test_IdfM_319(self):
            """
            /v1/coverage/stif/journeys?from=2.4855;48.8011&to=2.455535;48.783155&datetime=20160623T190000
            """
            self.journey(_from="2.4855;48.8011", to="2.455535;48.783155", datetime="20160623T190000")


        def test_IdfM_320(self):
            """
            /v1/coverage/stif/journeys?from=2.4436;48.9513&to=2.367124;48.851557&datetime=20160225T190000
            """
            self.journey(_from="2.4436;48.9513", to="2.367124;48.851557", datetime="20160225T190000")


        def test_IdfM_321(self):
            """
            /v1/coverage/stif/journeys?from=2.2376;48.8875&to=2.3248860000000002;48.834474&datetime=20160225T190000
            """
            self.journey(_from="2.2376;48.8875", to="2.3248860000000002;48.834474", datetime="20160225T190000")


        def test_IdfM_322(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8803&to=2.275816;48.858739&datetime=20160623T190000
            """
            self.journey(_from="2.3481;48.8803", to="2.275816;48.858739", datetime="20160623T190000")


        def test_IdfM_323(self):
            """
            /v1/coverage/stif/journeys?from=2.5021;48.8631&to=2.279859;48.898309000000005&datetime=20160225T190000
            """
            self.journey(_from="2.5021;48.8631", to="2.279859;48.898309000000005", datetime="20160225T190000")


        def test_IdfM_324(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.8624&to=2.349417;48.881236&datetime=20160623T190000
            """
            self.journey(_from="2.3467;48.8624", to="2.349417;48.881236", datetime="20160623T190000")


        def test_IdfM_325(self):
            """
            /v1/coverage/stif/journeys?from=2.2389;48.8947&to=2.337145;48.897424&datetime=20160225T190000
            """
            self.journey(_from="2.2389;48.8947", to="2.337145;48.897424", datetime="20160225T190000")


        def test_IdfM_326(self):
            """
            /v1/coverage/stif/journeys?from=2.3835;48.8677&to=2.3807669999999996;48.869538&datetime=20151203T210000
            """
            self.journey(_from="2.3835;48.8677", to="2.3807669999999996;48.869538", datetime="20151203T210000")


        def test_IdfM_327(self):
            """
            /v1/coverage/stif/journeys?from=2.2553;48.8983&to=2.322148;48.877639&datetime=20160623T190000
            """
            self.journey(_from="2.2553;48.8983", to="2.322148;48.877639", datetime="20160623T190000")


        def test_IdfM_328(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8363&to=2.333055;48.876740999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3181;48.8363", to="2.333055;48.876740999999996", datetime="20160623T190000")


        def test_IdfM_329(self):
            """
            /v1/coverage/stif/journeys?from=2.4024;48.7436&to=2.413294;48.746321&datetime=20160623T190000
            """
            self.journey(_from="2.4024;48.7436", to="2.413294;48.746321", datetime="20160623T190000")


        def test_IdfM_330(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8668&to=2.372585;48.865944&datetime=20151203T210000
            """
            self.journey(_from="2.3617;48.8668", to="2.372585;48.865944", datetime="20151203T210000")


        def test_IdfM_331(self):
            """
            /v1/coverage/stif/journeys?from=2.1279;49.0357&to=1.901109;49.004506&datetime=20160225T190000
            """
            self.journey(_from="2.1279;49.0357", to="1.901109;49.004506", datetime="20160225T190000")


        def test_IdfM_332(self):
            """
            /v1/coverage/stif/journeys?from=2.1434;48.9063&to=2.067108;48.893508000000004&datetime=20160225T190000
            """
            self.journey(_from="2.1434;48.9063", to="2.067108;48.893508000000004", datetime="20160225T190000")


        def test_IdfM_333(self):
            """
            /v1/coverage/stif/journeys?from=2.3998;48.7913&to=2.34805;48.866848&datetime=20160225T190000
            """
            self.journey(_from="2.3998;48.7913", to="2.34805;48.866848", datetime="20160225T190000")


        def test_IdfM_334(self):
            """
            /v1/coverage/stif/journeys?from=2.2539;48.901&to=2.354858;48.845265000000005&datetime=20160225T190000
            """
            self.journey(_from="2.2539;48.901", to="2.354858;48.845265000000005", datetime="20160225T190000")


        def test_IdfM_335(self):
            """
            /v1/coverage/stif/journeys?from=2.2881;48.8695&to=2.4104970000000003;48.693265999999994&datetime=20160225T190000
            """
            self.journey(_from="2.2881;48.8695", to="2.4104970000000003;48.693265999999994", datetime="20160225T190000")


        def test_IdfM_336(self):
            """
            /v1/coverage/stif/journeys?from=2.3754;48.9775&to=2.3180560000000003;48.882135&datetime=20160225T190000
            """
            self.journey(_from="2.3754;48.9775", to="2.3180560000000003;48.882135", datetime="20160225T190000")


        def test_IdfM_337(self):
            """
            /v1/coverage/stif/journeys?from=2.3807;48.8453&to=2.388918;48.842557&datetime=20151203T210000
            """
            self.journey(_from="2.3807;48.8453", to="2.388918;48.842557", datetime="20151203T210000")


        def test_IdfM_338(self):
            """
            /v1/coverage/stif/journeys?from=2.329;48.8426&to=2.364387;48.829975&datetime=20160623T190000
            """
            self.journey(_from="2.329;48.8426", to="2.364387;48.829975", datetime="20160623T190000")


        def test_IdfM_339(self):
            """
            /v1/coverage/stif/journeys?from=2.3808;48.8686&to=2.417549;48.855129999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3808;48.8686", to="2.417549;48.855129999999996", datetime="20160623T190000")


        def test_IdfM_340(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8803&to=2.343962;48.87764&datetime=20151203T210000
            """
            self.journey(_from="2.3494;48.8803", to="2.343962;48.87764", datetime="20151203T210000")


        def test_IdfM_341(self):
            """
            /v1/coverage/stif/journeys?from=2.4216;48.8497&to=2.384824;48.836264&datetime=20160623T190000
            """
            self.journey(_from="2.4216;48.8497", to="2.384824;48.836264", datetime="20160623T190000")


        def test_IdfM_342(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.839&to=2.358955;48.866847&datetime=20160623T190000
            """
            self.journey(_from="2.3453;48.839", to="2.358955;48.866847", datetime="20160623T190000")


        def test_IdfM_343(self):
            """
            /v1/coverage/stif/journeys?from=2.4204;48.9253&to=2.279862;48.895610999999995&datetime=20160623T190000
            """
            self.journey(_from="2.4204;48.9253", to="2.279862;48.895610999999995", datetime="20160623T190000")


        def test_IdfM_344(self):
            """
            /v1/coverage/stif/journeys?from=2.65;48.9725&to=2.6668950000000002;49.054323&datetime=20180802T180000
            """
            self.journey(_from="2.65;48.9725", to="2.6668950000000002;49.054323", datetime="20180802T180000")


        def test_IdfM_345(self):
            """
            /v1/coverage/stif/journeys?from=2.3998;48.8632&to=2.4039349999999997;48.865031&datetime=20151203T210000
            """
            self.journey(_from="2.3998;48.8632", to="2.4039349999999997;48.865031", datetime="20151203T210000")


        def test_IdfM_346(self):
            """
            /v1/coverage/stif/journeys?from=2.3426;48.8659&to=2.39551;48.654606&datetime=20160225T190000
            """
            self.journey(_from="2.3426;48.8659", to="2.39551;48.654606", datetime="20160225T190000")


        def test_IdfM_347(self):
            """
            /v1/coverage/stif/journeys?from=2.2977;48.7472&to=2.203804;48.776844&datetime=20160225T190000
            """
            self.journey(_from="2.2977;48.7472", to="2.203804;48.776844", datetime="20160225T190000")


        def test_IdfM_348(self):
            """
            /v1/coverage/stif/journeys?from=2.3126;48.8803&to=2.316695;48.876739&datetime=20151203T210000
            """
            self.journey(_from="2.3126;48.8803", to="2.316695;48.876739", datetime="20151203T210000")


        def test_IdfM_349(self):
            """
            /v1/coverage/stif/journeys?from=2.3262;48.8327&to=2.333059;48.833576&datetime=20151203T210000
            """
            self.journey(_from="2.3262;48.8327", to="2.333059;48.833576", datetime="20151203T210000")


        def test_IdfM_350(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8821&to=2.349418;48.886632&datetime=20151203T210000
            """
            self.journey(_from="2.3481;48.8821", to="2.349418;48.886632", datetime="20151203T210000")


        def test_IdfM_351(self):
            """
            /v1/coverage/stif/journeys?from=2.3712;48.8183&to=2.356219;48.840768&datetime=20160623T190000
            """
            self.journey(_from="2.3712;48.8183", to="2.356219;48.840768", datetime="20160623T190000")


        def test_IdfM_352(self):
            """
            /v1/coverage/stif/journeys?from=3.2062;48.9085&to=2.880433;48.937501&datetime=20180802T180000
            """
            self.journey(_from="3.2062;48.9085", to="2.880433;48.937501", datetime="20180802T180000")


        def test_IdfM_353(self):
            """
            /v1/coverage/stif/journeys?from=2.0652;48.9942&to=2.0799819999999998;49.041019&datetime=20160225T190000
            """
            self.journey(_from="2.0652;48.9942", to="2.0799819999999998;49.041019", datetime="20160225T190000")


        def test_IdfM_354(self):
            """
            /v1/coverage/stif/journeys?from=2.2129;48.9414&to=2.222459;48.947726&datetime=20160623T190000
            """
            self.journey(_from="2.2129;48.9414", to="2.222459;48.947726", datetime="20160623T190000")


        def test_IdfM_355(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8866&to=2.326235;48.893826000000004&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8866", to="2.326235;48.893826000000004", datetime="20151203T210000")


        def test_IdfM_356(self):
            """
            /v1/coverage/stif/journeys?from=2.5083;48.6914&to=2.42163;48.850631&datetime=20160225T190000
            """
            self.journey(_from="2.5083;48.6914", to="2.42163;48.850631", datetime="20160225T190000")


        def test_IdfM_357(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.8776&to=2.360313;48.855156&datetime=20160623T190000
            """
            self.journey(_from="2.3644;48.8776", to="2.360313;48.855156", datetime="20160623T190000")


        def test_IdfM_358(self):
            """
            /v1/coverage/stif/journeys?from=3.0944;48.8239&to=2.3276220000000003;48.770626&datetime=20160225T190000
            """
            self.journey(_from="3.0944;48.8239", to="2.3276220000000003;48.770626", datetime="20160225T190000")


        def test_IdfM_359(self):
            """
            /v1/coverage/stif/journeys?from=2.7694;48.8876&to=2.777324;48.855209&datetime=20180802T180000
            """
            self.journey(_from="2.7694;48.8876", to="2.777324;48.855209", datetime="20180802T180000")


        def test_IdfM_360(self):
            """
            /v1/coverage/stif/journeys?from=2.2921;48.9307&to=2.075898;49.037413&datetime=20160225T190000
            """
            self.journey(_from="2.2921;48.9307", to="2.075898;49.037413", datetime="20160225T190000")


        def test_IdfM_361(self):
            """
            /v1/coverage/stif/journeys?from=2.8656;48.9565&to=2.838463;48.971865&datetime=20180802T180000
            """
            self.journey(_from="2.8656;48.9565", to="2.838463;48.971865", datetime="20180802T180000")


        def test_IdfM_362(self):
            """
            /v1/coverage/stif/journeys?from=2.3399;48.8839&to=2.3480529999999997;48.880337&datetime=20151203T210000
            """
            self.journey(_from="2.3399;48.8839", to="2.3480529999999997;48.880337", datetime="20151203T210000")


        def test_IdfM_363(self):
            """
            /v1/coverage/stif/journeys?from=2.6003;48.8773&to=2.688023;48.946346000000005&datetime=20180802T180000
            """
            self.journey(_from="2.6003;48.8773", to="2.688023;48.946346000000005", datetime="20180802T180000")


        def test_IdfM_364(self):
            """
            /v1/coverage/stif/journeys?from=2.299;48.8776&to=2.30306;48.879433&datetime=20151203T210000
            """
            self.journey(_from="2.299;48.8776", to="2.30306;48.879433", datetime="20151203T210000")


        def test_IdfM_365(self):
            """
            /v1/coverage/stif/journeys?from=2.3303;48.8731&to=2.3316939999999997;48.856957&datetime=20160623T190000
            """
            self.journey(_from="2.3303;48.8731", to="2.3316939999999997;48.856957", datetime="20160623T190000")


        def test_IdfM_366(self):
            """
            /v1/coverage/stif/journeys?from=2.3303;48.8956&to=2.330326;48.893827&datetime=20151203T210000
            """
            self.journey(_from="2.3303;48.8956", to="2.330326;48.893827", datetime="20151203T210000")


        def test_IdfM_367(self):
            """
            /v1/coverage/stif/journeys?from=2.374;48.8875&to=2.896985;48.952709000000006&datetime=20180802T180000
            """
            self.journey(_from="2.374;48.8875", to="2.896985;48.952709000000006", datetime="20180802T180000")


        def test_IdfM_368(self):
            """
            /v1/coverage/stif/journeys?from=2.2854;48.8453&to=2.2704590000000002;48.788593&datetime=20160225T190000
            """
            self.journey(_from="2.2854;48.8453", to="2.2704590000000002;48.788593", datetime="20160225T190000")


        def test_IdfM_369(self):
            """
            /v1/coverage/stif/journeys?from=2.2949;48.8785&to=2.303061;48.876736&datetime=20151203T210000
            """
            self.journey(_from="2.2949;48.8785", to="2.303061;48.876736", datetime="20151203T210000")


        def test_IdfM_370(self):
            """
            /v1/coverage/stif/journeys?from=2.1804;48.8667&to=2.181694;48.885628000000004&datetime=20160623T190000
            """
            self.journey(_from="2.1804;48.8667", to="2.181694;48.885628000000004", datetime="20160623T190000")


        def test_IdfM_371(self):
            """
            /v1/coverage/stif/journeys?from=2.3072;48.8749&to=2.303061;48.876736&datetime=20151203T210000
            """
            self.journey(_from="2.3072;48.8749", to="2.303061;48.876736", datetime="20151203T210000")


        def test_IdfM_372(self):
            """
            /v1/coverage/stif/journeys?from=2.3412;48.8749&to=2.339872;48.878539&datetime=20151203T210000
            """
            self.journey(_from="2.3412;48.8749", to="2.339872;48.878539", datetime="20151203T210000")


        def test_IdfM_373(self):
            """
            /v1/coverage/stif/journeys?from=2.3317;48.8677&to=2.326263;48.767029&datetime=20160225T190000
            """
            self.journey(_from="2.3317;48.8677", to="2.326263;48.767029", datetime="20160225T190000")


        def test_IdfM_374(self):
            """
            /v1/coverage/stif/journeys?from=2.3317;48.8731&to=2.331692;48.87764&datetime=20151203T210000
            """
            self.journey(_from="2.3317;48.8731", to="2.331692;48.87764", datetime="20151203T210000")


        def test_IdfM_375(self):
            """
            /v1/coverage/stif/journeys?from=2.2103;48.8947&to=2.240322;48.889289&datetime=20160623T190000
            """
            self.journey(_from="2.2103;48.8947", to="2.240322;48.889289", datetime="20160623T190000")


        def test_IdfM_376(self):
            """
            /v1/coverage/stif/journeys?from=2.3317;48.8731&to=2.304418;48.887527&datetime=20151203T210000
            """
            self.journey(_from="2.3317;48.8731", to="2.304418;48.887527", datetime="20151203T210000")


        def test_IdfM_377(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8794&to=2.337145;48.87764&datetime=20151203T210000
            """
            self.journey(_from="2.344;48.8794", to="2.337145;48.87764", datetime="20151203T210000")


        def test_IdfM_378(self):
            """
            /v1/coverage/stif/journeys?from=2.4026;48.8794&to=3.124989;48.950466999999996&datetime=20180802T180000
            """
            self.journey(_from="2.4026;48.8794", to="3.124989;48.950466999999996", datetime="20180802T180000")


        def test_IdfM_379(self):
            """
            /v1/coverage/stif/journeys?from=2.3916;48.8435&to=2.307163;48.856953000000004&datetime=20160623T190000
            """
            self.journey(_from="2.3916;48.8435", to="2.307163;48.856953000000004", datetime="20160623T190000")


        def test_IdfM_380(self):
            """
            /v1/coverage/stif/journeys?from=1.9477;48.8158&to=2.258139;48.833548&datetime=20160225T190000
            """
            self.journey(_from="1.9477;48.8158", to="2.258139;48.833548", datetime="20160225T190000")


        def test_IdfM_381(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8552&to=2.114801;48.902603000000006&datetime=20160225T190000
            """
            self.journey(_from="2.3181;48.8552", to="2.114801;48.902603000000006", datetime="20160225T190000")


        def test_IdfM_382(self):
            """
            /v1/coverage/stif/journeys?from=2.247;48.9415&to=2.328966;48.874043&datetime=20160623T190000
            """
            self.journey(_from="2.247;48.9415", to="2.328966;48.874043", datetime="20160623T190000")


        def test_IdfM_383(self):
            """
            /v1/coverage/stif/journeys?from=2.3481;48.8866&to=2.349417;48.883035&datetime=20151203T210000
            """
            self.journey(_from="2.3481;48.8866", to="2.349417;48.883035", datetime="20151203T210000")


        def test_IdfM_384(self):
            """
            /v1/coverage/stif/journeys?from=2.3331;48.8767&to=2.330329;48.872244&datetime=20151203T210000
            """
            self.journey(_from="2.3331;48.8767", to="2.330329;48.872244", datetime="20151203T210000")


        def test_IdfM_385(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.8803&to=2.330332;48.85246&datetime=20160623T190000
            """
            self.journey(_from="2.3194;48.8803", to="2.330332;48.85246", datetime="20160623T190000")


        def test_IdfM_386(self):
            """
            /v1/coverage/stif/journeys?from=2.6075;48.9529&to=2.611602;48.95285&datetime=20151203T210000
            """
            self.journey(_from="2.6075;48.9529", to="2.611602;48.95285", datetime="20151203T210000")


        def test_IdfM_387(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8606&to=2.352138;48.860553&datetime=20151203T210000
            """
            self.journey(_from="2.344;48.8606", to="2.352138;48.860553", datetime="20151203T210000")


        def test_IdfM_388(self):
            """
            /v1/coverage/stif/journeys?from=2.4474;48.785&to=2.331692;48.881237&datetime=20160225T190000
            """
            self.journey(_from="2.4474;48.785", to="2.331692;48.881237", datetime="20160225T190000")


        def test_IdfM_389(self):
            """
            /v1/coverage/stif/journeys?from=2.1819;48.8254&to=2.170867;48.861332&datetime=20160225T190000
            """
            self.journey(_from="2.1819;48.8254", to="2.170867;48.861332", datetime="20160225T190000")


        def test_IdfM_390(self):
            """
            /v1/coverage/stif/journeys?from=2.3426;48.8767&to=2.3480529999999997;48.879438&datetime=20151203T210000
            """
            self.journey(_from="2.3426;48.8767", to="2.3480529999999997;48.879438", datetime="20151203T210000")


        def test_IdfM_391(self):
            """
            /v1/coverage/stif/journeys?from=2.8309;48.8973&to=2.839065;48.896322&datetime=20151203T210000
            """
            self.journey(_from="2.8309;48.8973", to="2.839065;48.896322", datetime="20151203T210000")


        def test_IdfM_392(self):
            """
            /v1/coverage/stif/journeys?from=2.3194;48.873999999999995&to=2.322148;48.876740000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3194;48.873999999999995", to="2.322148;48.876740000000005", datetime="20151203T210000")


        def test_IdfM_393(self):
            """
            /v1/coverage/stif/journeys?from=2.3522;48.9019&to=2.339873;48.892928000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3522;48.9019", to="2.339873;48.892928000000005", datetime="20151203T210000")


        def test_IdfM_394(self):
            """
            /v1/coverage/stif/journeys?from=2.0302;48.906000000000006&to=2.09848;48.892678000000004&datetime=20160225T190000
            """
            self.journey(_from="2.0302;48.906000000000006", to="2.09848;48.892678000000004", datetime="20160225T190000")


        def test_IdfM_395(self):
            """
            /v1/coverage/stif/journeys?from=2.3154;48.8057&to=2.41759;48.880309999999994&datetime=20160225T190000
            """
            self.journey(_from="2.3154;48.8057", to="2.41759;48.880309999999994", datetime="20160225T190000")


        def test_IdfM_396(self):
            """
            /v1/coverage/stif/journeys?from=2.3685;48.8192&to=2.3657630000000003;48.853356&datetime=20160623T190000
            """
            self.journey(_from="2.3685;48.8192", to="2.3657630000000003;48.853356", datetime="20160623T190000")


        def test_IdfM_397(self):
            """
            /v1/coverage/stif/journeys?from=2.5704;48.9062&to=2.511732;48.89819&datetime=20160623T190000
            """
            self.journey(_from="2.5704;48.9062", to="2.511732;48.89819", datetime="20160623T190000")


        def test_IdfM_398(self):
            """
            /v1/coverage/stif/journeys?from=2.3344;48.8713&to=2.327603;48.873143&datetime=20151203T210000
            """
            self.journey(_from="2.3344;48.8713", to="2.327603;48.873143", datetime="20151203T210000")


        def test_IdfM_399(self):
            """
            /v1/coverage/stif/journeys?from=2.3549;48.8794&to=2.349417;48.881236&datetime=20151203T210000
            """
            self.journey(_from="2.3549;48.8794", to="2.349417;48.881236", datetime="20151203T210000")


        def test_IdfM_400(self):
            """
            /v1/coverage/stif/journeys?from=2.3754;48.9703&to=2.308482;48.933391&datetime=20160225T190000
            """
            self.journey(_from="2.3754;48.9703", to="2.308482;48.933391", datetime="20160225T190000")


        def test_IdfM_401(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.8552&to=2.326238;48.880337&datetime=20160623T190000
            """
            self.journey(_from="2.3467;48.8552", to="2.326238;48.880337", datetime="20160623T190000")


        def test_IdfM_402(self):
            """
            /v1/coverage/stif/journeys?from=2.3712;48.8695&to=2.369863;48.872240000000005&datetime=20151203T210000
            """
            self.journey(_from="2.3712;48.8695", to="2.369863;48.872240000000005", datetime="20151203T210000")


        def test_IdfM_403(self):
            """
            /v1/coverage/stif/journeys?from=2.4586;48.9243&to=2.35215;48.902819&datetime=20160225T190000
            """
            self.journey(_from="2.4586;48.9243", to="2.35215;48.902819", datetime="20160225T190000")


        def test_IdfM_404(self):
            """
            /v1/coverage/stif/journeys?from=2.3562;48.8659&to=2.357592;48.866847&datetime=20160623T190000
            """
            self.journey(_from="2.3562;48.8659", to="2.357592;48.866847", datetime="20160623T190000")


        def test_IdfM_405(self):
            """
            /v1/coverage/stif/journeys?from=3.1403;48.802&to=3.094328;48.820273&datetime=20151203T210000
            """
            self.journey(_from="3.1403;48.802", to="3.094328;48.820273", datetime="20151203T210000")


        def test_IdfM_406(self):
            """
            /v1/coverage/stif/journeys?from=2.3726;48.8722&to=2.363045;48.868644&datetime=20151203T210000
            """
            self.journey(_from="2.3726;48.8722", to="2.363045;48.868644", datetime="20151203T210000")


        def test_IdfM_407(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.8228&to=2.33987;48.84077&datetime=20160623T190000
            """
            self.journey(_from="2.3467;48.8228", to="2.33987;48.84077", datetime="20160623T190000")


        def test_IdfM_408(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8704&to=2.354867;48.869545&datetime=20151203T210000
            """
            self.journey(_from="2.3508;48.8704", to="2.354867;48.869545", datetime="20151203T210000")


        def test_IdfM_409(self):
            """
            /v1/coverage/stif/journeys?from=2.97;48.678000000000004&to=2.9932380000000003;48.796617&datetime=20160225T190000
            """
            self.journey(_from="2.97;48.678000000000004", to="2.9932380000000003;48.796617", datetime="20160225T190000")


        def test_IdfM_410(self):
            """
            /v1/coverage/stif/journeys?from=2.1745;49.0016&to=2.4274720000000003;49.066452000000005&datetime=20160225T190000
            """
            self.journey(_from="2.1745;49.0016", to="2.4274720000000003;49.066452000000005", datetime="20160225T190000")


        def test_IdfM_411(self):
            """
            /v1/coverage/stif/journeys?from=2.3617;48.8543&to=2.331691;48.883935&datetime=20160623T190000
            """
            self.journey(_from="2.3617;48.8543", to="2.331691;48.883935", datetime="20160623T190000")


        def test_IdfM_412(self):
            """
            /v1/coverage/stif/journeys?from=2.5798;48.8702&to=2.588013;48.878264&datetime=20160623T190000
            """
            self.journey(_from="2.5798;48.8702", to="2.588013;48.878264", datetime="20160623T190000")


        def test_IdfM_413(self):
            """
            /v1/coverage/stif/journeys?from=2.3249;48.8246&to=2.3071490000000003;48.880334000000005&datetime=20160225T190000
            """
            self.journey(_from="2.3249;48.8246", to="2.3071490000000003;48.880334000000005", datetime="20160225T190000")


        def test_IdfM_414(self):
            """
            /v1/coverage/stif/journeys?from=2.3657;48.7796&to=2.403959;48.883016&datetime=20160225T190000
            """
            self.journey(_from="2.3657;48.7796", to="2.403959;48.883016", datetime="20160225T190000")


        def test_IdfM_415(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8327&to=2.322163;48.82728&datetime=20151203T210000
            """
            self.journey(_from="2.3276;48.8327", to="2.322163;48.82728", datetime="20151203T210000")


        def test_IdfM_416(self):
            """
            /v1/coverage/stif/journeys?from=2.5497;48.8361&to=2.876582;48.960001&datetime=20180802T180000
            """
            self.journey(_from="2.5497;48.8361", to="2.876582;48.960001", datetime="20180802T180000")


        def test_IdfM_417(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8489&to=2.234819;48.912665999999994&datetime=20160225T190000
            """
            self.journey(_from="2.3494;48.8489", to="2.234819;48.912665999999994", datetime="20160225T190000")


        def test_IdfM_418(self):
            """
            /v1/coverage/stif/journeys?from=2.3494;48.8704&to=2.34803;48.775123&datetime=20160225T190000
            """
            self.journey(_from="2.3494;48.8704", to="2.34803;48.775123", datetime="20160225T190000")


        def test_IdfM_419(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8507&to=2.168473;48.763308&datetime=20160225T190000
            """
            self.journey(_from="2.3453;48.8507", to="2.168473;48.763308", datetime="20160225T190000")


        def test_IdfM_420(self):
            """
            /v1/coverage/stif/journeys?from=2.2853;48.8713&to=2.33305;48.935193&datetime=20160225T190000
            """
            self.journey(_from="2.2853;48.8713", to="2.33305;48.935193", datetime="20160225T190000")


        def test_IdfM_421(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.883&to=2.721987;48.924654&datetime=20180802T180000
            """
            self.journey(_from="2.3276;48.883", to="2.721987;48.924654", datetime="20180802T180000")


        def test_IdfM_422(self):
            """
            /v1/coverage/stif/journeys?from=2.3453;48.8659&to=2.54948;48.794709999999995&datetime=20160225T190000
            """
            self.journey(_from="2.3453;48.8659", to="2.54948;48.794709999999995", datetime="20160225T190000")


        def test_IdfM_423(self):
            """
            /v1/coverage/stif/journeys?from=2.3726;48.873999999999995&to=2.3794009999999997;48.866841&datetime=20151203T210000
            """
            self.journey(_from="2.3726;48.873999999999995", to="2.3794009999999997;48.866841", datetime="20151203T210000")


        def test_IdfM_424(self):
            """
            /v1/coverage/stif/journeys?from=2.3712;48.8722&to=2.3780419999999998;48.871338&datetime=20151203T210000
            """
            self.journey(_from="2.3712;48.8722", to="2.3780419999999998;48.871338", datetime="20151203T210000")


        def test_IdfM_425(self):
            """
            /v1/coverage/stif/journeys?from=2.2964;48.7346&to=2.3098919999999996;48.851558000000004&datetime=20160225T190000
            """
            self.journey(_from="2.2964;48.7346", to="2.3098919999999996;48.851558000000004", datetime="20160225T190000")


        def test_IdfM_426(self):
            """
            /v1/coverage/stif/journeys?from=2.3766;48.7769&to=2.37525;48.785908&datetime=20160623T190000
            """
            self.journey(_from="2.3766;48.7769", to="2.37525;48.785908", datetime="20160623T190000")


        def test_IdfM_427(self):
            """
            /v1/coverage/stif/journeys?from=2.3603;48.8713&to=2.4189529999999997;48.880309000000004&datetime=20160623T190000
            """
            self.journey(_from="2.3603;48.8713", to="2.4189529999999997;48.880309000000004", datetime="20160623T190000")


        def test_IdfM_428(self):
            """
            /v1/coverage/stif/journeys?from=2.2553;48.9334&to=2.2484900000000003;48.89739&datetime=20160623T190000
            """
            self.journey(_from="2.2553;48.9334", to="2.2484900000000003;48.89739", datetime="20160623T190000")


        def test_IdfM_429(self):
            """
            /v1/coverage/stif/journeys?from=2.2402;48.937&to=2.0949720000000003;49.052741999999995&datetime=20160225T190000
            """
            self.journey(_from="2.2402;48.937", to="2.0949720000000003;49.052741999999995", datetime="20160225T190000")


        def test_IdfM_430(self):
            """
            /v1/coverage/stif/journeys?from=2.2745;48.8614&to=2.286715;48.863240999999995&datetime=20151203T210000
            """
            self.journey(_from="2.2745;48.8614", to="2.286715;48.863240999999995", datetime="20151203T210000")


        def test_IdfM_431(self):
            """
            /v1/coverage/stif/journeys?from=2.329;48.8731&to=2.284011;48.842556&datetime=20160623T190000
            """
            self.journey(_from="2.329;48.8731", to="2.284011;48.842556", datetime="20160623T190000")


        def test_IdfM_432(self):
            """
            /v1/coverage/stif/journeys?from=2.3821;48.8623&to=2.386213;48.863240999999995&datetime=20151203T210000
            """
            self.journey(_from="2.3821;48.8623", to="2.386213;48.863240999999995", datetime="20151203T210000")


        def test_IdfM_433(self):
            """
            /v1/coverage/stif/journeys?from=2.3713;48.9721&to=2.380835;48.947775&datetime=20160623T190000
            """
            self.journey(_from="2.3713;48.9721", to="2.380835;48.947775", datetime="20160623T190000")


        def test_IdfM_434(self):
            """
            /v1/coverage/stif/journeys?from=3.2938;48.5679&to=2.353494;48.839869&datetime=20180802T180000
            """
            self.journey(_from="3.2938;48.5679", to="2.353494;48.839869", datetime="20180802T180000")


        def test_IdfM_435(self):
            """
            /v1/coverage/stif/journeys?from=2.3535;48.8695&to=2.357596;48.875840000000004&datetime=20151203T210000
            """
            self.journey(_from="2.3535;48.8695", to="2.357596;48.875840000000004", datetime="20151203T210000")


        def test_IdfM_436(self):
            """
            /v1/coverage/stif/journeys?from=2.3631;48.8803&to=2.361685;48.87494&datetime=20151203T210000
            """
            self.journey(_from="2.3631;48.8803", to="2.361685;48.87494", datetime="20151203T210000")


        def test_IdfM_437(self):
            """
            /v1/coverage/stif/journeys?from=2.785;48.803000000000004&to=2.367138;48.874039&datetime=20180802T180000
            """
            self.journey(_from="2.785;48.803000000000004", to="2.367138;48.874039", datetime="20180802T180000")


        def test_IdfM_438(self):
            """
            /v1/coverage/stif/journeys?from=2.3549;48.8426&to=2.29489;48.865942&datetime=20160623T190000
            """
            self.journey(_from="2.3549;48.8426", to="2.29489;48.865942", datetime="20160623T190000")


        def test_IdfM_439(self):
            """
            /v1/coverage/stif/journeys?from=2.3713;48.9343&to=2.42163;48.850631&datetime=20160225T190000
            """
            self.journey(_from="2.3713;48.9343", to="2.42163;48.850631", datetime="20160225T190000")


        def test_IdfM_440(self):
            """
            /v1/coverage/stif/journeys?from=2.3903;48.8363&to=2.3943630000000002;48.838957&datetime=20151203T210000
            """
            self.journey(_from="2.3903;48.8363", to="2.3943630000000002;48.838957", datetime="20151203T210000")


        def test_IdfM_441(self):
            """
            /v1/coverage/stif/journeys?from=2.2854;48.8515&to=2.28537;48.846154&datetime=20151203T210000
            """
            self.journey(_from="2.2854;48.8515", to="2.28537;48.846154", datetime="20151203T210000")


        def test_IdfM_442(self):
            """
            /v1/coverage/stif/journeys?from=2.299;48.8857&to=2.397199;48.930681&datetime=20160225T190000
            """
            self.journey(_from="2.299;48.8857", to="2.397199;48.930681", datetime="20160225T190000")


        def test_IdfM_443(self):
            """
            /v1/coverage/stif/journeys?from=2.3876;48.8596&to=2.380757;48.857848&datetime=20151203T210000
            """
            self.journey(_from="2.3876;48.8596", to="2.380757;48.857848", datetime="20151203T210000")


        def test_IdfM_444(self):
            """
            /v1/coverage/stif/journeys?from=2.3603;48.8911&to=2.327601;48.882135999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3603;48.8911", to="2.327601;48.882135999999996", datetime="20160623T190000")


        def test_IdfM_445(self):
            """
            /v1/coverage/stif/journeys?from=2.3344;48.8543&to=2.455518;48.775960999999995&datetime=20160225T190000
            """
            self.journey(_from="2.3344;48.8543", to="2.455518;48.775960999999995", datetime="20160225T190000")


        def test_IdfM_446(self):
            """
            /v1/coverage/stif/journeys?from=2.329;48.8839&to=2.345325;48.871345&datetime=20160623T190000
            """
            self.journey(_from="2.329;48.8839", to="2.345325;48.871345", datetime="20160623T190000")


        def test_IdfM_447(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8138&to=2.349397;48.802101&datetime=20160623T190000
            """
            self.journey(_from="2.3508;48.8138", to="2.349397;48.802101", datetime="20160623T190000")


        def test_IdfM_448(self):
            """
            /v1/coverage/stif/journeys?from=2.8132;48.9027&to=2.804976;48.897366&datetime=20180802T180000
            """
            self.journey(_from="2.8132;48.9027", to="2.804976;48.897366", datetime="20180802T180000")


        def test_IdfM_449(self):
            """
            /v1/coverage/stif/journeys?from=2.3331;48.8704&to=2.4666930000000002;48.887459&datetime=20160225T190000
            """
            self.journey(_from="2.3331;48.8704", to="2.4666930000000002;48.887459", datetime="20160225T190000")


        def test_IdfM_450(self):
            """
            /v1/coverage/stif/journeys?from=2.3699;48.8641&to=2.3739470000000003;48.864145&datetime=20151203T210000
            """
            self.journey(_from="2.3699;48.8641", to="2.3739470000000003;48.864145", datetime="20151203T210000")


        def test_IdfM_451(self):
            """
            /v1/coverage/stif/journeys?from=2.6274;48.8449&to=2.632791;48.842186&datetime=20151203T210000
            """
            self.journey(_from="2.6274;48.8449", to="2.632791;48.842186", datetime="20151203T210000")


        def test_IdfM_452(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.857&to=2.3521419999999997;48.874941&datetime=20160623T190000
            """
            self.journey(_from="2.3644;48.857", to="2.3521419999999997;48.874941", datetime="20160623T190000")


        def test_IdfM_453(self):
            """
            /v1/coverage/stif/journeys?from=2.3399;48.8785&to=2.313993;48.824581&datetime=20160623T190000
            """
            self.journey(_from="2.3399;48.8785", to="2.313993;48.824581", datetime="20160623T190000")


        def test_IdfM_454(self):
            """
            /v1/coverage/stif/journeys?from=2.3944;48.8776&to=2.386228;48.878529&datetime=20151203T210000
            """
            self.journey(_from="2.3944;48.8776", to="2.386228;48.878529", datetime="20151203T210000")


        def test_IdfM_455(self):
            """
            /v1/coverage/stif/journeys?from=2.3549;48.8668&to=2.33033;48.869546&datetime=20160623T190000
            """
            self.journey(_from="2.3549;48.8668", to="2.33033;48.869546", datetime="20160623T190000")


        def test_IdfM_456(self):
            """
            /v1/coverage/stif/journeys?from=2.5552;48.8684&to=2.545589;48.840579999999996&datetime=20160225T190000
            """
            self.journey(_from="2.5552;48.8684", to="2.545589;48.840579999999996", datetime="20160225T190000")


        def test_IdfM_457(self):
            """
            /v1/coverage/stif/journeys?from=2.3753;48.8731&to=2.3862240000000003;48.874032&datetime=20151203T210000
            """
            self.journey(_from="2.3753;48.8731", to="2.3862240000000003;48.874032", datetime="20151203T210000")


        def test_IdfM_458(self):
            """
            /v1/coverage/stif/journeys?from=2.2077;48.8515&to=2.237589;48.891985&datetime=20160623T190000
            """
            self.journey(_from="2.2077;48.8515", to="2.237589;48.891985", datetime="20160623T190000")


        def test_IdfM_459(self):
            """
            /v1/coverage/stif/journeys?from=2.6003;48.8773&to=2.688023;48.946346000000005&datetime=20160225T190000
            """
            self.journey(_from="2.6003;48.8773", to="2.688023;48.946346000000005", datetime="20160225T190000")


        def test_IdfM_460(self):
            """
            /v1/coverage/stif/journeys?from=2.915;48.8582&to=2.89994;48.851973&datetime=20180802T180000
            """
            self.journey(_from="2.915;48.8582", to="2.89994;48.851973", datetime="20180802T180000")


        def test_IdfM_461(self):
            """
            /v1/coverage/stif/journeys?from=2.3032;48.6321&to=2.150656;48.435949&datetime=20160225T190000
            """
            self.journey(_from="2.3032;48.6321", to="2.150656;48.435949", datetime="20160225T190000")


        def test_IdfM_462(self):
            """
            /v1/coverage/stif/journeys?from=2.2459;48.8299&to=2.2717419999999997;48.847945&datetime=20160623T190000
            """
            self.journey(_from="2.2459;48.8299", to="2.2717419999999997;48.847945", datetime="20160623T190000")


        def test_IdfM_463(self):
            """
            /v1/coverage/stif/journeys?from=2.3821;48.8677&to=2.376679;48.872238&datetime=20151203T210000
            """
            self.journey(_from="2.3821;48.8677", to="2.376679;48.872238", datetime="20151203T210000")


        def test_IdfM_464(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8453&to=2.318058;48.876739&datetime=20160623T190000
            """
            self.journey(_from="2.3276;48.8453", to="2.318058;48.876739", datetime="20160623T190000")


        def test_IdfM_465(self):
            """
            /v1/coverage/stif/journeys?from=2.3344;48.8624&to=2.341236;48.878539&datetime=20160623T190000
            """
            self.journey(_from="2.3344;48.8624", to="2.341236;48.878539", datetime="20160623T190000")


        def test_IdfM_466(self):
            """
            /v1/coverage/stif/journeys?from=2.2636;48.8479&to=2.26085;48.842543&datetime=20151203T210000
            """
            self.journey(_from="2.2636;48.8479", to="2.26085;48.842543", datetime="20151203T210000")


        def test_IdfM_467(self):
            """
            /v1/coverage/stif/journeys?from=1.9834;48.7755&to=2.220119;48.782257&datetime=20160225T190000
            """
            self.journey(_from="1.9834;48.7755", to="2.220119;48.782257", datetime="20160225T190000")


        def test_IdfM_468(self):
            """
            /v1/coverage/stif/journeys?from=2.1493;48.4368&to=2.4843490000000004;48.402735&datetime=20160225T190000
            """
            self.journey(_from="2.1493;48.4368", to="2.4843490000000004;48.402735", datetime="20160225T190000")


        def test_IdfM_469(self):
            """
            /v1/coverage/stif/journeys?from=2.3344;48.8237&to=2.487134;48.882937&datetime=20160225T190000
            """
            self.journey(_from="2.3344;48.8237", to="2.487134;48.882937", datetime="20160225T190000")


        def test_IdfM_470(self):
            """
            /v1/coverage/stif/journeys?from=2.3358;48.8336&to=2.324884;48.842568&datetime=20151203T210000
            """
            self.journey(_from="2.3358;48.8336", to="2.324884;48.842568", datetime="20151203T210000")


        def test_IdfM_471(self):
            """
            /v1/coverage/stif/journeys?from=3.2885;48.576&to=2.3371459999999997;48.851561&datetime=20180802T180000
            """
            self.journey(_from="3.2885;48.576", to="2.3371459999999997;48.851561", datetime="20180802T180000")


        def test_IdfM_472(self):
            """
            /v1/coverage/stif/journeys?from=2.3644;48.8668&to=2.361683;48.870443&datetime=20151203T210000
            """
            self.journey(_from="2.3644;48.8668", to="2.361683;48.870443", datetime="20151203T210000")


        def test_IdfM_473(self):
            """
            /v1/coverage/stif/journeys?from=2.5199;48.8991&to=2.513073;48.891892999999996&datetime=20160623T190000
            """
            self.journey(_from="2.5199;48.8991", to="2.513073;48.891892999999996", datetime="20160623T190000")


        def test_IdfM_474(self):
            """
            /v1/coverage/stif/journeys?from=2.3358;48.9541&to=2.350773;48.854258&datetime=20160225T190000
            """
            self.journey(_from="2.3358;48.9541", to="2.350773;48.854258", datetime="20160225T190000")


        def test_IdfM_475(self):
            """
            /v1/coverage/stif/journeys?from=2.7047;48.406000000000006&to=2.621909;48.844913&datetime=20180802T180200
            """
            self.journey(_from="2.7047;48.406000000000006", to="2.621909;48.844913", datetime="20180802T180200")


        def test_IdfM_476(self):
            """
            /v1/coverage/stif/journeys?from=2.3181;48.8821&to=2.375397;48.977453000000004&datetime=20160225T190000
            """
            self.journey(_from="2.3181;48.8821", to="2.375397;48.977453000000004", datetime="20160225T190000")


        def test_IdfM_477(self):
            """
            /v1/coverage/stif/journeys?from=2.344;48.8471&to=2.3466869999999997;48.867748&datetime=20160623T190000
            """
            self.journey(_from="2.344;48.8471", to="2.3466869999999997;48.867748", datetime="20160623T190000")


        def test_IdfM_478(self):
            """
            /v1/coverage/stif/journeys?from=3.4585;48.543&to=2.944569;48.37782&datetime=20180802T180000
            """
            self.journey(_from="3.4585;48.543", to="2.944569;48.37782", datetime="20180802T180000")


        def test_IdfM_479(self):
            """
            /v1/coverage/stif/journeys?from=2.3685;48.8641&to=2.369856;48.861447999999996&datetime=20151203T210000
            """
            self.journey(_from="2.3685;48.8641", to="2.369856;48.861447999999996", datetime="20151203T210000")


        def test_IdfM_480(self):
            """
            /v1/coverage/stif/journeys?from=2.2963;48.8471&to=2.2976240000000003;48.856051&datetime=20151203T210000
            """
            self.journey(_from="2.2963;48.8471", to="2.2976240000000003;48.856051", datetime="20151203T210000")


        def test_IdfM_481(self):
            """
            /v1/coverage/stif/journeys?from=2.5294;48.8838&to=2.544448;48.893639&datetime=20160623T190000
            """
            self.journey(_from="2.5294;48.8838", to="2.544448;48.893639", datetime="20160623T190000")


        def test_IdfM_482(self):
            """
            /v1/coverage/stif/journeys?from=2.3508;48.8911&to=2.364418;48.88573&datetime=20151203T210000
            """
            self.journey(_from="2.3508;48.8911", to="2.364418;48.88573", datetime="20151203T210000")


        def test_IdfM_483(self):
            """
            /v1/coverage/stif/journeys?from=2.1378;48.9521&to=2.328969;48.854259000000006&datetime=20160225T190000
            """
            self.journey(_from="2.1378;48.9521", to="2.328969;48.854259000000006", datetime="20160225T190000")


        def test_IdfM_484(self):
            """
            /v1/coverage/stif/journeys?from=2.3467;48.8318&to=2.328973;48.832676&datetime=20151203T210000
            """
            self.journey(_from="2.3467;48.8318", to="2.328973;48.832676", datetime="20151203T210000")


        def test_IdfM_485(self):
            """
            /v1/coverage/stif/journeys?from=2.2473;48.8236&to=2.277213;48.830861999999996&datetime=20160623T190000
            """
            self.journey(_from="2.2473;48.8236", to="2.277213;48.830861999999996", datetime="20160623T190000")


        def test_IdfM_486(self):
            """
            /v1/coverage/stif/journeys?from=2.3412;48.848&to=2.3630709999999997;48.918104&datetime=20160623T190000
            """
            self.journey(_from="2.3412;48.848", to="2.3630709999999997;48.918104", datetime="20160623T190000")


        def test_IdfM_487(self):
            """
            /v1/coverage/stif/journeys?from=2.3276;48.8839&to=2.341236;48.882135999999996&datetime=20160623T190000
            """
            self.journey(_from="2.3276;48.8839", to="2.341236;48.882135999999996", datetime="20160623T190000")


        def test_IdfM_488(self):
            """
            /v1/coverage/stif/journeys?from=3.1303;48.9432&to=2.3875919999999997;48.878528&datetime=20180802T180000
            """
            self.journey(_from="3.1303;48.9432", to="2.3875919999999997;48.878528", datetime="20180802T180000")


        def test_IdfM_489(self):
            """
            /v1/coverage/stif/journeys?from=2.2744;48.8704&to=2.3248740000000003;48.883035&datetime=20160623T190000
            """
            self.journey(_from="2.2744;48.8704", to="2.3248740000000003;48.883035", datetime="20160623T190000")


        def test_IdfM_490(self):
            """
            /v1/coverage/stif/journeys?from=2.2376;48.8902&to=2.23077;48.891979&datetime=20151203T210000
            """
            self.journey(_from="2.2376;48.8902", to="2.23077;48.891979", datetime="20151203T210000")


        def test_IdfM_491(self):
            """
            /v1/coverage/stif/journeys?from=2.3576;48.812&to=2.315295;48.960371&datetime=20160225T190000
            """
            self.journey(_from="2.3576;48.812", to="2.315295;48.960371", datetime="20160225T190000")


        def test_IdfM_492(self):
            """
            /v1/coverage/stif/journeys?from=2.3862;48.8785&to=2.394407;48.876726&datetime=20151203T210000
            """
            self.journey(_from="2.3862;48.8785", to="2.394407;48.876726", datetime="20151203T210000")


        def test_IdfM_493(self):
            """
            /v1/coverage/stif/journeys?from=2.3018;48.7562&to=2.357631;48.963069&datetime=20160225T190000
            """
            self.journey(_from="2.3018;48.7562", to="2.357631;48.963069", datetime="20160225T190000")


        def test_IdfM_494(self):
            """
            /v1/coverage/stif/journeys?from=2.2322;48.8767&to=2.341234;48.854259000000006&datetime=20160225T190000
            """
            self.journey(_from="2.2322;48.8767", to="2.341234;48.854259000000006", datetime="20160225T190000")


        def test_IdfM_495(self):
            """
            /v1/coverage/stif/journeys?from=2.2976;48.8713&to=2.33305;48.935193&datetime=20160225T190000
            """
            self.journey(_from="2.2976;48.8713", to="2.33305;48.935193", datetime="20160225T190000")


        def test_IdfM_496(self):
            """
            /v1/coverage/stif/journeys?from=2.3521;48.891999999999996&to=2.343964;48.892927&datetime=20151203T210000
            """
            self.journey(_from="2.3521;48.891999999999996", to="2.343964;48.892927", datetime="20151203T210000")


        def test_IdfM_497(self):
            """
            /v1/coverage/stif/journeys?from=2.4858;48.882&to=2.334422;48.823684&datetime=20160225T190000
            """
            self.journey(_from="2.4858;48.882", to="2.334422;48.823684", datetime="20160225T190000")


        def test_IdfM_498(self):
            """
            /v1/coverage/stif/journeys?from=2.8819999999999997;48.9591&to=2.35351;48.88843&datetime=20180802T180000
            """
            self.journey(_from="2.8819999999999997;48.9591", to="2.35351;48.88843", datetime="20180802T180000")


        def test_IdfM_499(self):
            """
            /v1/coverage/stif/journeys?from=2.5524;48.8451&to=2.5537549999999998;48.838766&datetime=20151203T210000
            """
            self.journey(_from="2.5524;48.8451", to="2.5537549999999998;48.838766", datetime="20151203T210000")


@set_scenario({"idfm": {"scenario": "new_default"}})
class TestIdfMNewDefault(IdfM, ArtemisTestFixture):
    pass


@set_scenario({"idfm": {"scenario": "experimental"}})
class TestIdfMExperimental(IdfM, ArtemisTestFixture):
    pass

