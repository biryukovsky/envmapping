from dataclasses import dataclass
from envmapping import field, EnvType, BaseEnvMapping

import pytest


@dataclass(frozen=True)
class Mapping(BaseEnvMapping):
    pub: str = field(EnvType.string)
    pub_with_env_name: str = field(EnvType.string, env_name='pub_env_name')
    pub_with_default: str = field(EnvType.string, default='public_default')
    priv: int = field(EnvType.int, default=42, is_public=False)
    priv_with_default: int = field(EnvType.int, default=321, is_public=False)


@pytest.fixture(scope='session')
def mapping():
    return Mapping
