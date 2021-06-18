# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.
import sys
import inginious_container_api.run_student


# Simply runs run_student with no cmd and ssh set to True
def ssh_student(cmd=None, memory_limit=0, hard_time_limit=0, time_limit=0, container=None, share_network=False, run_as_root=False):
    """
    If a command is specified, runs it in a student container.
    Then gives ssh access to that container to the student.
    :param cmd: command to be ran (as a string, with parameters) before launching the ssh server.
    :param memory_limit: memory limit in megabytes. By default it is 0, which means that it will be the same as the current
                       container (NB: it does not count in the "host" container memory limit!).
    :param hard_time_limit: hard time limit. By default it is 0, which means that it will be the same as the current
                       container (NB: it *does* count in the "host" container *hard* timeout!).
    :param time_limit: time limit in seconds. By default it is 0, which means that it will be the same as the current
                       container (NB: it does not count in the "host" container timeout!).
    :param container: container to use. Must be present in the current agent. By default it is None, meaning the current
                      container type will be used.
    :param share_network: share the network with the host container if True. Default is False.
    :param run_as_root: If set to True, try to give root access to the student via ssh. Default is False. This feature is still in Beta and should not be used for now.
    """
    inginious_container_api.run_student.run_student(cmd=cmd, container=container, time_limit=time_limit,
                hard_time_limit=hard_time_limit, memory_limit=memory_limit,
                share_network=share_network,
                stdin=sys.stdin.fileno(), stdout=sys.stdout.fileno(), stderr=sys.stderr.fileno(),
                signal_handler_callback=inginious_container_api.run_student._hack_signals, ssh=True, run_as_root=run_as_root)
