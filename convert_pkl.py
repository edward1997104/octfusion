import pickle
if __name__ == '__main__':
    filename = 'compact_latent_16384_256_bior3.9_constant_h5_1.pkl'
    dataset_name = 'Thingi10K'
    filenames = []
    with open(filename, 'rb') as f:
        data = pickle.load(f)

        for name in data:
            filename = name.split('/')[1]
            print(f'filename: {filename}')
            filenames.append(filename)

    ### write it to Txt

    with open(f'{dataset_name}.txt', 'w') as f:
        for filename in filenames:
            f.write(f'{filename}\n')