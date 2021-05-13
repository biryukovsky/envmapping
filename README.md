# EnvMapping

## Usage

```python
import threading
from dataclasses import dataclass
from envmapping import BaseEnvMapping, field, EnvType


_conf = threading.local()
_conf.config = None


@dataclass(frozen=True)
class Settings(BaseEnvMapping):
    my_field1 = field(env_type=EnvType.int, default=42)
    my_field2 = field(env_type=EnvType.string, default='fourty_two')
    my_field3 = field(env_type=EnvType.string, is_public=False, default='private_string') # will not be replaced with environment variable


def build_config():
    settings = Settings.create()
    _conf.config = settings
    return _conf.config

```