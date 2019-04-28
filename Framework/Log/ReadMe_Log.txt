import logging

Why do we need logger , when we have logging with full blown functionality

logging.basicConfig(
            filename = log_file_path,
            filemode = 'w',
            level = logging.DEBUG,
            format = '%(asctime)s %(message)s',
            datefmt = '%m/%d/%Y %I:%M:%S %p'
        )

With logging the configs are set for the whole module. 
To have different log params for different files, we can opt for logger.