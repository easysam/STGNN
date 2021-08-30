from glob import glob
import pandas as pd
from tqdm import tqdm


def extract_internet_traffic(
        raw_data_regex=r'C:\Users\hkrep\PycharmProjects\STPred\db\TelecomMI\sms-call-internet-mi-*.txt',
        target_data_path='db/TelecomMI/internet.csv',
        agg=True):
    """
    This func build a multivariate time series from the original cellular traffic dataset.
    The MI dataset has 100*100=10k grids, during two month.
    Args:
        raw_data_regex: str. REGEX data path, to be parsed by glob func.
        target_data_path: str. path to save.
        agg: bool. Whether to aggregate the data to 50*50 grids, to reduce computation in the subsequent graph model.

    Returns:
        None
    """
    files = sorted(glob(raw_data_regex))
    li = []
    for filename in tqdm(files):
        df = pd.read_csv(filename, sep='\t', header=None,
                         names=['id', 'ts', 'country', 'sms_in', 'sms_out', 'call_in', 'call_out', 'internet'],
                         usecols=['id', 'ts', 'internet'])
        li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    if agg:
        frame['agg_id'] = ((frame['id'] - 1) // 100 // 5) * 20 + ((frame['id'] - 1) % 100 // 5)
        agg_frame = frame.groupby(['ts', 'agg_id'])['internet'].sum().reset_index()
        agg_frame.rename(mapper={'agg_id': 'id'}, axis=1, inplace=True)
        agg_frame.to_csv(target_data_path, index=False)
    else:
        frame.to_csv(target_data_path, index=False)


def unstack_data(data_path='db/TelecomMI/internet.csv'):
    """
    Unstack data from "ts, id, internet_traffic_value as columns" to "ts as index, id as column"
    Args:
        data_path: the data file to which the func read and write

    Returns:
        None
    """
    df = pd.read_csv('db/TelecomMI/internet.csv', index_col=['ts', 'id'])
    df = df.unstack().droplevel(0, axis=1)  # drop the outer column level (internet)
    df.to_csv(data_path)


if __name__ == '__main__':
    extract_internet_traffic()
    unstack_data()
