OK_FORMAT = True

test = {   'name': 'Task1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert shape == (159256, 23)\n'
                                               '>>> assert missing_values_per_column.sum() == 0\n'
                                               '>>> assert np.isclose(smoking_distribution[1], 0.437365)\n'
                                               '>>> assert len(smokers_over_40) == 25894\n'
                                               ">>> assert cholesterol_top_correlated.index[3] == 'height(cm)'\n"
                                               ">>> assert grouped.loc[1, 'group_size'] == 69653\n"
                                               ">>> assert np.isclose(grouped.loc[0, 'avg_age'], 46.5)\n"
                                               ">>> assert np.isclose(grouped.loc[0, 'std_age'], 12.2)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
