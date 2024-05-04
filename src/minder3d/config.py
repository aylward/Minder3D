#!/usr/bin/env python3

"""
Helper utility to parse input parameters for a given run.
"""

import argparse


def parse_config() -> argparse.Namespace:
    """
    Parse command line arguments to configure the run.
    """

    parser = argparse.ArgumentParser(
        description='Enabling innovative AI for medical imaging.'
    )

    parser.add_argument(
        '--load-image', type=str, required=False, help='Path to image'
    )
    parser.add_argument(
        '--load-scene', type=str, required=False, help='Path to scene'
    )

    args = parser.parse_args()
    print(args)

    return args
