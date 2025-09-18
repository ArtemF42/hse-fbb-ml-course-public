OK_FORMAT = True

test = {   'name': 'Task3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> assert np.isclose(cov_height_weight, np.cov(data['height(cm)'], data['weight(kg)'])[0, 1])\n"
                                               ">>> assert np.isclose(cov_height_waist, np.cov(data['height(cm)'], data['waist(cm)'])[0, 1])\n"
                                               ">>> assert np.isclose(corr_height_weight, np.corrcoef(data['height(cm)'], data['weight(kg)'])[0, 1])\n"
                                               ">>> assert np.isclose(corr_height_waist, np.corrcoef(data['height(cm)'], data['waist(cm)'])[0, 1])\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
