from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
import sys

if sys.platform == 'win32':
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())
