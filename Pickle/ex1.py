import bz2
import pickle

dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}


def do_pickle(data, file_name):
    compressed_file = bz2.BZ2File(file_name, 'wb')
    # outfile = open(filename,'wb')
    pickle.dump(data, compressed_file)
    compressed_file.close()


def do_unpickle(compressed_file):
    sfile = bz2.BZ2File(compressed_file, 'rb')
    new_dict = pickle.load(sfile)
    sfile.close()
    return new_dict


do_pickle(data=dogs_dict, file_name='dogs.pickle')
value = do_unpickle(compressed_file='dogs.pickle')

print(value)
