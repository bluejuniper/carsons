import pytest
from numpy.testing import assert_array_almost_equal
from numpy import array
from carsons.carsons import convert_geometric_model, convert_geometric_model_to_shunt

# `carsons` implements the model entirely in SI metric units, however this
# conversion allows us to enter in impedance as ohm-per-mile in the test
# harness, which means we can lift matrices directly out of the ieee test
# networks.
OHM_PER_MILE_TO_OHM_PER_METER = 1 / 1_609.344
S_PER_MILE_TO_S_PER_METER = OHM_PER_MILE_TO_OHM_PER_METER 
OHM_PER_KILOMETER_TO_OHM_PER_METER = 1 / 1_000


class ACBN_geometry_line():
    """
    IEEE 13 Configuration 601 Line Geometry
    556,500 26/7 ACSR Phase, 4/0 6/1 ACSR Neutral
    """

    def __init__(self, ƒ=60):
        self.frequency = ƒ

    @property
    def resistance(self):
        return {
            'A': 0.000115575,
            'C': 0.000115575,
            'B': 0.000115575,
            'N': 0.000367852,
        }

    @property
    def geometric_mean_radius(self):
        return {
            'A': 0.00947938,
            'C': 0.00947938,
            'B': 0.00947938,
            'N': 0.00248107,
        }

    @property
    def outside_radius(self):
        return {
            'A': 0.0235458,
            'C': 0.0235458,
            'B': 0.0235458,
            'N': 0.0143002,
        }

    @property
    def wire_positions(self):
        return {
            'A': (0.762, 8.5344),
            'C': (2.1336, 8.5344),
            'B': (0, 8.5344),
            'N': (1.2192, 7.3152),
        }

    @property
    def phases(self):
        return [
            'A',
            'C',
            'B',
            'N',
        ]


def ACBN_line_phase_impedance_60Hz():
    """ IEEE 13 Configuration 601 Impedance Solution At 60Hz """
    return OHM_PER_MILE_TO_OHM_PER_METER * array([
            [0.3465 + 1.0179j, 0.1560 + 0.5017j, 0.1580 + 0.4236j],
            [0.1560 + 0.5017j, 0.3375 + 1.0478j, 0.1535 + 0.3849j],
            [0.1580 + 0.4236j, 0.1535 + 0.3849j, 0.3414 + 1.0348j]])


def ACBN_line_shunt_impedance_60Hz():
    """ IEEE 13 Configuration 601 Shunt Impedance Solution At 60Hz """
    return 1j * S_PER_MILE_TO_S_PER_METER * array([
            [6.2998,  -1.9958, -1.2595],
            [-1.9958,  5.9597, -0.7417],
            [-1.2595, -0.7417,  5.6386]])


def ACBN_line_phase_impedance_50Hz():
    """ IEEE 13 Configuration 601 Impedance Solution At 50Hz """
    return OHM_PER_KILOMETER_TO_OHM_PER_METER * array([
            [0.2101 + 0.5372j,  0.09171 + 0.2691j, 0.09295 + 0.2289j],
            [0.09171 + 0.2691j, 0.20460 + 0.552j,  0.09021 + 0.2085j],
            [0.09295 + 0.2289j, 0.09021 + 0.2085j, 0.207 + 0.5456j]])


class CBN_geometry_line():
    """ IEEE 13 Configuration 603 Line Geometry """

    def __init__(self, ƒ=60):
        self.frequency = ƒ
        self.outside_radius = {}        

    @property
    def resistance(self):
        return {
            'B': 0.000695936,
            'C': 0.000695936,
            'N': 0.000695936,
        }

    @property
    def geometric_mean_radius(self):
        return {
            'B': 0.00135941,
            'C': 0.00135941,
            'N': 0.00135941,
        }

    @property
    def wire_positions(self):
        return {
            'B': (2.1336, 8.5344),
            'C': (0, 8.5344),
            'N': (1.2192, 7.3152),
        }

    @property
    def phases(self):
        return [
            'B',
            'C',
            'N',
        ]


def CBN_line_phase_impedance_60Hz():
    """ IEEE 13 Configuration 603 Impedance Solution At 60Hz """
    return OHM_PER_MILE_TO_OHM_PER_METER * array([
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 1.3294 + 1.3471j, 0.2066 + 0.4591j],
            [0.0000 + 0.0000j, 0.2066 + 0.4591j, 1.3238 + 1.3569j]])


def CBN_line_phase_impedance_50Hz():
    """ IEEE 13 Configuration 603 Impedance Solution At 50Hz """
    return OHM_PER_KILOMETER_TO_OHM_PER_METER * array([
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 0.8128 + 0.7144j, 0.1153 + 0.2543j],
            [0.0000 + 0.0000j, 0.1153 + 0.2543j, 0.8097 + 0.7189j]])


class CN_geometry_line():
    """ IEEE 13 Configuration 605 Line Geometry"""

    def __init__(self, ƒ=60):
        self.frequency = ƒ
        self.outside_radius = {}        

    @property
    def resistance(self):
        return {
            'C': 0.000695936,
            'N': 0.000695936,
        }

    @property
    def geometric_mean_radius(self):
        return {
            'C': 0.00135941,
            'N': 0.00135941,
        }

    @property
    def wire_positions(self):
        return {
            'C': (0, 8.8392),
            'N': (0.1524, 7.3152),
        }

    @property
    def phases(self):
        return [
            'C',
            'N',
        ]


def CN_line_phase_impedance_60Hz():
    """ IEEE 13 Configuration 605 Impedance Solution At 60Hz """
    return OHM_PER_MILE_TO_OHM_PER_METER * array([
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 1.3292 + 1.3475j]])


def CN_line_phase_impedance_50Hz():
    """ IEEE 13 Configuration 605 Impedance Solution At 50Hz """
    return OHM_PER_KILOMETER_TO_OHM_PER_METER * array([
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.0000 + 0.0000j],
            [0.0000 + 0.0000j, 0.0000 + 0.0000j, 0.8127 + 0.7146j]])


@pytest.mark.parametrize(
    "line,frequency,expected_impedance",
    [(ACBN_geometry_line, 60, ACBN_line_phase_impedance_60Hz()),
     (CBN_geometry_line, 60, CBN_line_phase_impedance_60Hz()),
     (CN_geometry_line, 60, CN_line_phase_impedance_60Hz()),
     (ACBN_geometry_line, 50, ACBN_line_phase_impedance_50Hz()),
     (CBN_geometry_line, 50, CBN_line_phase_impedance_50Hz()),
     (CN_geometry_line, 50, CN_line_phase_impedance_50Hz())])
def test_converts_geometry_to_phase_impedance(
        line, frequency, expected_impedance):
    actual_impedance = convert_geometric_model(line(ƒ=frequency))
    assert_array_almost_equal(expected_impedance,
                              actual_impedance)


# def test_converts_geometry_to_shunt_impedance():
#     model = ACBN_geometry_line()

#     assert_array_almost_equal(
#         convert_geometric_model_to_shunt(model),
#         ACBN_line_shunt_impedance_60Hz(),
#         decimal=9
#     )