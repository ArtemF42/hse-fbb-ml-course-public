OK_FORMAT = True

test = {   'name': 'Task2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> assert 'BMI' in data.columns\n"
                                               ">>> assert 'BMI_category' in data.columns\n"
                                               ">>> assert data['BMI_category'].nunique() == 4\n"
                                               ">>> assert np.isclose(data['BMI'].iloc[0], 22.038, atol=0.001)\n"
                                               ">>> assert np.abs(data.groupby('BMI_category', observed=True).size()['Healthy'] - 92190) < 100\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
