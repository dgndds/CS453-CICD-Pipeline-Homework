from dictionary import getDefinition


def test_getDefinition():
    actualDefinition = getDefinition("computer")
    expectedDefinition = "A person employed to prform computations; one who computes."
    assert actualDefinition == expectedDefinition
