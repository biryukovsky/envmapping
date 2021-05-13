import os
from unittest import mock

import envmapping


@mock.patch.dict(os.environ, {'INT_KEY': "42"})
def test_get_int():
    get_int = envmapping._get_int('INT_KEY')
    get_int_none = envmapping._get_int('NOT_EXISTENT')

    assert get_int == 42
    assert get_int_none is None


@mock.patch.dict(os.environ, {'STRING_KEY': 'test'})
def test_get_string():
    get_str = envmapping._get_string('STRING_KEY')
    assert get_str == 'test'


@mock.patch.dict(os.environ, {'BOOL_TRUE_KEY': '1', 'BOOL_FALSE_KEY': '0'})
def test_get_bool():
    get_true = envmapping._get_bool('BOOL_TRUE_KEY')
    get_false = envmapping._get_bool('BOOL_FALSE_KEY')
    get_bool_none = envmapping._get_bool('NOT_EXISTENT')

    assert get_true is True
    assert get_false is False
    assert get_bool_none is None


@mock.patch.dict(os.environ, {'LIST_KEY': 'i,am,testing,list'})
def test_get_list():
    get_list = envmapping._get_list('LIST_KEY')
    get_list_none = envmapping._get_list('NOT_EXISTENT')

    assert get_list == ['i', 'am', 'testing', 'list']
    assert get_list_none is None


@mock.patch.dict(os.environ, {'PRIV': '123', 'PUB_WITH_DEFAULT': 'from_env',
                              'PUB_ENV_NAME': 'env_var', 'PUB': 'test_value',
                              'PRIV_WITH_DEFAULT': '999', })
def test_base_envmapping(mapping):
    s = mapping.create()
    assert s.pub == 'test_value'
    assert s.pub_with_default == 'from_env'
    assert s.pub_with_env_name == 'env_var'
    assert s.priv == 42
    assert s.priv_with_default == 321
