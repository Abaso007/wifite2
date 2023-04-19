#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class Attack(object):
    '''Contains functionality common to all attacks.'''

    target_wait = 60

    def __init__(self, target):
        self.target = target

    def run(self):
        raise Exception('Unimplemented method: run')

    def wait_for_target(self, airodump):
        '''Waits for target to appear in airodump.'''
        start_time = time.time()
        targets = airodump.get_targets(apply_filter=False)
        while len(targets) == 0:
            # Wait for target to appear in airodump.
            if int(time.time() - start_time) > Attack.target_wait:
                raise Exception('Target did not appear after %d seconds, stopping' % Attack.target_wait)
            time.sleep(1)
            targets = airodump.get_targets()
            continue

        airodump_target = next(
            (t for t in targets if t.bssid == self.target.bssid), None
        )
        if airodump_target is None:
            raise Exception(f'Could not find target ({self.target.bssid}) in airodump')

        return airodump_target

