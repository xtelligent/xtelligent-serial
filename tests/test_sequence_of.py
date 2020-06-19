from xtelligent_serial.sequence_of import SequenceOf, SequenceOfType

def test_sequence_of_syntax():
    s1 = SequenceOfType(int)
    s2 = SequenceOf[int]
    assert s1.type == s2().type
    assert s2().type == int
