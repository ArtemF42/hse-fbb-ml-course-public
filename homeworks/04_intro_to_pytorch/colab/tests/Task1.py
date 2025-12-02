OK_FORMAT = True

test = {   'name': 'Task1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> assert isinstance(X_train, torch.FloatTensor)\n'
                                               ">>> assert 0 <= X_train.min() and X_train.max() <= 1, 'признаки необходимо отмасштабировать'\n"
                                               '>>> assert isinstance(X_test, torch.FloatTensor)\n'
                                               ">>> assert 0 <= X_test.min() and X_test.max() <= 1, 'признаки необходимо отмасштабировать'\n"
                                               '>>> assert isinstance(train_dataset, torch.utils.data.Subset)\n'
                                               '>>> assert isinstance(val_dataset, torch.utils.data.Subset)\n'
                                               '>>> assert isinstance(test_dataset, TensorDataset)\n'
                                               '>>> assert isinstance(train_dataloader, DataLoader)\n'
                                               '>>> assert train_dataloader.batch_size == 256\n'
                                               ">>> assert isinstance(train_dataloader.sampler, torch.utils.data.RandomSampler), 'стоит использовать `shuffle=True`'\n"
                                               '>>> assert isinstance(val_dataloader, DataLoader)\n'
                                               '>>> assert val_dataloader.batch_size == 256\n'
                                               '>>> assert isinstance(test_dataloader, DataLoader)\n'
                                               '>>> assert test_dataloader.batch_size == 256\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
