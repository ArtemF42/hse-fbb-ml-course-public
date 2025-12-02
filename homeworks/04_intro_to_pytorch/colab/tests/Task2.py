OK_FORMAT = True

test = {   'name': 'Task2',
    'points': 5,
    'suites': [   {   'cases': [{'code': '>>> model = MLPClassifier(2, 3)\n>>> x = torch.randn(1, 2)\n>>> assert model(x).shape == (1, 3)\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
