#!/usr/bin/env python3
""" Dynamically import the correct GPU Stats library based on the faceswap backend and the machine
being used. """

import platform

from lib.utils import get_backend

from ._base import set_exclude_devices

backend = get_backend()

if backend == "nvidia" and platform.system().lower() == "darwin":
    from .nvidia_apple import NvidiaAppleStats as GPUStats  # type:ignore
elif backend == "nvidia":
    from .nvidia import NvidiaStats as GPUStats  # type:ignore
elif backend == "amd":
    from .amd import AMDStats as GPUStats, setup_plaidml  # type:ignore
elif backend == "apple_silicon":
    from .apple_silicon import AppleSiliconStats as GPUStats  # type:ignore
elif backend == "directml":
    from .directml import DirectML as GPUStats  # type:ignore
elif backend == "cpu":
    from .cpu import CPUStats as GPUStats  # type:ignore
