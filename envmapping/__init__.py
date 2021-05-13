__version__ = '0.1.0'

import os
from dataclasses import dataclass, field as _field, fields, MISSING
from enum import unique, Enum
from typing import Optional, Any


def _get_int(env_key: str):
    val = os.environ.get(env_key)
    if val is None:
        return None
    return int(val)


def _get_bool(env_key: str):
    val = os.environ.get(env_key)
    if val is None:
        return None
    truthy = {'1', 'true', 'True'}
    falsy = {'0', 'false', 'False'}
    if val in truthy:
        return True
    if val in falsy:
        return False


def _get_list(env_key: str, delimiter: str = ','):
    val: str = os.environ.get(env_key)
    if val is None:
        return None
    return val.split(delimiter)


def _get_string(env_key: str):
    val = os.environ.get(env_key)
    return val


@unique
class EnvType(Enum):
    string = _get_string
    int = _get_int
    bool = _get_bool
    list = _get_list


def field(env_type: EnvType, is_public: bool = True,
          default: Any = MISSING, env_name: Optional[str] = ''):
    return _field(default=default,
                  metadata=dict(is_public=is_public,
                                env_type=env_type,
                                env_name=env_name))


public_int = field(EnvType.int, is_public=True)
public_str = field(EnvType.string, is_public=True)
public_bool = field(EnvType.bool, is_public=True)
public_list = field(EnvType.list, is_public=True)


@dataclass(frozen=True)
class BaseEnvMapping:
    @classmethod
    def create(cls):
        env = dict()
        for f in fields(cls):
            if f.metadata.get('is_public', False) is True:
                env_type = f.metadata.get('env_type', EnvType.string)
                env_name = (f.metadata.get('env_name', '') or f.name).upper()
                env[f.name] = env_type(env_name) or f.default
        return cls(**env)
